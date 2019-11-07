<?php

function EJGetJourneyEventWithBalance($eid) {
    $eventInfo = EJGetEventInfo(null, trim($eid));
    if (sizeof($eventInfo) <= 0) {
        W3LogError("Event ID of journey is not existed: " . $eid);
        return null;
    }

    $eventBillSql = "select " .
                  "bill.Amount as amount, bill.Datetime as datetime, bill.Currency as currency" .
                  " from " .
                  "bill" .
                  " where " .
                  "ID in (select Bill from mapbillfinanceevent where Event =" . $eid . ")";
    $amount = EJSumCurrency($eventBillSql);
    $balance = sprintf("%01.2f", floatval($eventInfo["Budget"]) - $amount);
    $eventInfo["Balance"] = $balance;

    return $eventInfo;
}

function EJGetJourneyTravelers($jid) {
    $sql = "select " .
         "person.Name as name, person.FID as family" .
         " from " .
         "person, mapjourneyperson" .
         " where " .
         "mapjourneyperson.Person = person.ID" .
         " and " .
         "mapjourneyperson.Journey=" . $jid;
    $result = array();
    EJReadTable($sql, function ($row) use (&$result) {
        $result[$row["name"]] = $row["family"];
    });

    return $result;
}

function EJGetJourney(&$journeyParams) {
    $aid = "aidJourney";
    return EJExecuteWithAuthenticatedFamily($aid, $journeyParams, function ($fid, $aid, &$journeyParams) {
        $paramOffset = 1; # The first one is the whole string from reg match
        $startDate = $journeyParams[W3GetAPIParamIndex($aid, "from") + $paramOffset];
        $endDate = $journeyParams[W3GetAPIParamIndex($aid, "to") + $paramOffset];

        $sql = "select " .
             "journey.Datetime as datetime, journey.Name as name, journey.Note as note, journey.ID as id, journey.Event as eid" .
             " from " .
             "journey" .
             " where " .
             "journey.Datetime >= '" . $startDate . "' and journey.Datetime <= '" . $endDate . "'" .
             " order by journey.Datetime asc";

        $result = "{" . W3CreateSuccessfulResult(false) . "," . W3MakeString(w3ApiResultData) . ":[";
        EJReadTable($sql, function ($row) use (&$result, $aid, $fid) {
            $travelers = EJGetJourneyTravelers($row["id"]);
            if (sizeof($travelers) <= 0) {
                W3LogWarning("Journey traveler should not be empty");
                return;
            }

            $travelerStr = "";
            foreach ($travelers as $personName => $personFID) {
                if ($personFID != $fid) {
                    return;
                }
                $travelerStr .= $personName . ", ";
            }
            $travelerStr = rtrim($travelerStr, ", ");

            $eventName = "";
            $eventBalance = "";
            if ($row["eid"] != "") {
                $eventInfo = EJGetJourneyEventWithBalance($row["eid"]);
                if ($eventInfo != null) {
                    $eventName = $eventInfo["Name"];
                    $eventBalance = $eventInfo["Balance"];
                }
            }

            $apiDef = W3GetAPIDef($aid);
            $columns = $apiDef[w3ApiResult][w3ApiResultData];
            $result .= "{";
            foreach ($columns as $value) {
                if ($value[w3ApiDataValue] == "balance") {
                    $result .= W3MakeString($value[w3ApiDataValue]) . ":" . W3MakeString($eventBalance) . ",";
                } else if ($value[w3ApiDataValue] == "event") {
                    $result .= W3MakeString($value[w3ApiDataValue]) . ":" . W3MakeString($eventName) . ",";
                } else if ($value[w3ApiDataValue] == "traveler") {
                    $result .= W3MakeString($value[w3ApiDataValue]) . ":" . W3MakeString($travelerStr) . ",";
                } else {
                    $result .= W3MakeString($value[w3ApiDataValue]) . ":" . W3MakeString($row[$value[w3ApiDataValue]]) . ",";
                }
            }
            $result = rtrim($result, ",") . "},";
        });
        $result = rtrim($result, ",") . "]}";

        return $result;
    });
}

function EJAddJourney(&$parameters) {
    $aid = "aidAddJourney";
    return EJExecuteWithAuthenticatedFamily($aid, $parameters, function ($familyID, $aid, &$parameters) {
        $paramOffset = 1; # The first one is alway whole string from reg match
        $eventStr = EJDecodeURLString($parameters[W3GetAPIParamIndex($aid, "event") + $paramOffset]);
        $travelerStr = EJDecodeURLString($parameters[W3GetAPIParamIndex($aid, "traveler") + $paramOffset]);
        $travelers = explode(",", $travelerStr);
        if (sizeof($travelers) <= 0) {
            W3LogError("No traveler of journey");
            return W3CreateFailedResult();
        }

        $eventID = null;
        if ($eventStr != "") {
            $eventInfo = EJGetEventInfo(trim($eventStr), null);
            if (sizeof($eventInfo) <= 0) {
                W3LogError("Event of journey is not existed: " . $eventStr);
                return W3CreateFailedResult();
            }

            $eventFamilyID = $eventInfo["FID"];
            if ($eventFamilyID != $familyID) {
                W3LogError("Event of journey is not in same family: " . $eventStr);
                return W3CreateFailedResult();
            }
            $eventID = $eventInfo["ID"];
        }

        $persons = array();
        foreach ($travelers as $personName) {
            $personInfo = EJGetPersonInfo(trim($personName));
            if (sizeof($personInfo) <= 0) {
                W3LogError("Traveler of journey is not existed: " . $personName);
                return W3CreateFailedResult();
            }

            if ($personInfo["FID"] != $familyID) {
                W3LogError("Traveler of journey is not in same family: " . $personName);
                return W3CreateFailedResult();
            }

            array_push($persons, $personInfo["ID"]);
        }

        if (EJInsertJourney($parameters, $eventID)) {
            if (EJMapJourneyToPerson($persons)) {
                return W3CreateSuccessfulResult();
            }
        }

        return W3CreateFailedResult();
    });
}

function EJAddJourneyPlace(&$parameters) {
    $aid = "aidAddJourneyPlace";
    return EJExecuteWithAuthentication($aid, $parameters, function ($session, $aid, &$parameters) {
        $placeID = EJInsertJourneyPlace($parameters, $aid);
        if ($placeID < 0) {
            W3LogError("Failed to get journey place ID");
            return W3CreateFailedResult();
        }

        if (EJInsertJourneyNote($parameters, $placeID)) {
            return W3CreateSuccessfulResult();
        }

        return W3CreateFailedResult();
    });
}

function EJGetJourneyPlace(&$journeyParams) {
    $aid = "aidJourneyPlace";
    return EJExecuteWithAuthentication($aid, $journeyParams, function ($session, $aid, &$journeyParams) {
        $paramOffset = 1; # The first one is the whole string from reg match
        $jid = $journeyParams[W3GetAPIParamIndex($aid, "jid") + $paramOffset];

        $sql = "select " .
             "journeynote.Datetime as datetime, journeynote.Remark as remark, journeynote.Note as note, " .
             "journeyplace.Name as name, journeyplace.Latitude as latitude, journeyplace.Longitude as longitude" .
             " from " .
             "journeynote, journeyplace" .
             " where " .
             "journeynote.Place=journeyplace.ID" .
             " and " .
             "journeynote.Journey=" . $jid .
             " order by journeynote.Datetime asc";

        return EJReadMultiResultFromTable($aid, $sql);
    });
}

function EJGetAllPlace(&$params) {
    $aid = "aidAllPlace";
    return EJExecuteWithAuthenticatedFamily($aid, $params, function ($fid, $aid, &$params) {
        $sqlJourney = "select " .
                    "journey.ID" .
                    " from " .
                    "journey, mapjourneyperson, person" .
                    " where " .
                    "journey.ID=mapjourneyperson.Journey" .
                    " and " .
                    "mapjourneyperson.Person=person.ID" .
                    " and " .
                    "person.FID=" . $fid;
        $sqlPlace = "select " .
             "journeynote.Datetime as datetime, journeynote.Remark as remark, journeynote.Note as note, " .
             "journeyplace.Name as name, journeyplace.Latitude as latitude, journeyplace.Longitude as longitude, journeyplace.ID as placeid" .
             " from " .
             "journeynote, journeyplace" .
             " where " .
             "journeynote.Place=journeyplace.ID" .
             " and " .
             "journeynote.Journey in (" . $sqlJourney . ")" .
             " order by journeynote.Datetime asc";

        $result = "{" . W3CreateSuccessfulResult(false) . "," . W3MakeString(w3ApiResultData) . ":[";
        $places = array();
        EJReadTable($sqlPlace, function ($row) use (&$places, &$result, $aid) {
            if (in_array($row["placeid"], $places)) {
                return;
            }
            array_push($places, $row["placeid"]);

            $apiDef = W3GetAPIDef($aid);
            $columns = $apiDef[w3ApiResult][w3ApiResultData];
            $result .= "{";
            foreach ($columns as $value) {
                $resultForColumn = $row[$value[w3ApiDataValue]];
                $result .= W3MakeString($value[w3ApiDataValue]) . ":" . W3MakeString($resultForColumn) . ",";
            }
            $result = rtrim($result, ",") . "},";
        });
        $result = rtrim($result, ",") . "]}";

        return $result;
    });
}

function EJAddPOI(&$parameters) {
    $aid = "aidAddPOI";
    return EJExecuteWithAuthenticatedFamily($aid, $parameters, function ($fid, $aid, &$parameters) {
        $placeID = EJInsertJourneyPlace($parameters, $aid);
        if ($placeID < 0) {
            W3LogError("Failed to get POI place ID");
            return W3CreateFailedResult();
        }

        if (EJInsertPOI($parameters, $placeID, $fid)) {
            return W3CreateSuccessfulResult();
        }

        return W3CreateFailedResult();
    });
}

function EJGetAllPOI(&$params) {
    $aid = "aidAllPOI";
    return EJExecuteWithAuthenticatedFamily($aid, $params, function ($fid, $aid, &$params) {
        $paramOffset = 1; # The first one is the whole string from reg match
        $jid = $params[W3GetAPIParamIndex($aid, "jid") + $paramOffset];

        $sql = "select " .
             "poi.ID as poiid, poi.Note as note, " .
             "journeyplace.Name as name, journeyplace.Latitude as latitude, journeyplace.Longitude as longitude" .
             " from " .
             "poi, journeyplace" .
             " where " .
             "poi.Place=journeyplace.ID" .
             " and " .
             "poi.FID=" . $fid .
             " order by poi.ID asc";

        return EJReadMultiResultFromTable($aid, $sql);
    });
}

function EJAddPOIToJourney(&$parameters) {
    $aid = "aidAddPOIToJourney";
    return EJExecuteWithAuthentication($aid, $parameters, function ($session, $aid, &$parameters) {
        $paramOffset = 1; # The first one is the whole string from reg match
        $poiID = $parameters[W3GetAPIParamIndex($aid, "poi") + $paramOffset];

        $sql = "select journeyplace.ID as id from poi, journeyplace where poi.Place=journeyplace.ID and poi.ID=" . $poiID;
        $placeID = NULL;
        EJReadTable($sql, function ($row) use (&$placeID) {
            $placeID = $row["id"];
        });
        if ($placeID == NULL) {
            W3LogError("Failed to get POI place when add POI to journey");
            return W3CreateFailedResult();
        }

        // Mock "aidAddJourneyPlace"
        $jid = $parameters[W3GetAPIParamIndex($aid, "journey") + $paramOffset];
        $datetime = $parameters[W3GetAPIParamIndex($aid, "datetime") + $paramOffset];
        $remark = $parameters[W3GetAPIParamIndex($aid, "remark") + $paramOffset];
        $note = $parameters[W3GetAPIParamIndex($aid, "note") + $paramOffset]; // It's mock and no decode here
        $mockParams = array(
            "Whold regex string",
            $jid,
            "name",
            $datetime,
            "latitude",
            "longitude",
            $remark,
            $note,
            $session
        );
        if (!EJInsertJourneyNote($mockParams, $placeID)) {
            return W3CreateFailedResult();
        }

        // Remove POI because it's already in journey
        $sql = "delete from poi where ID=" . $poiID;
        if (!EJExecuteSQL($sql)) {
            return W3CreateFailedResult();
        }

        return W3CreateSuccessfulResult();
    });
}

 ?>
