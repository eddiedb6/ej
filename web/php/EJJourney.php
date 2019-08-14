<?php

function EJCalculateJourneyEventBalance($eid, $budget) {
    $eventBillSql = "select " .
                  "bill.Amount as amount, bill.Datetime as datetime, bill.Currency as currency" .
                  " from " .
                  "bill" .
                  " where " .
                  "ID in (select Bill from mapbillfinanceevent where Event =" . $eid . ")";
    $amount = EJSumCurrency($eventBillSql);
    $balance = sprintf("%01.2f", floatval($budget) - $amount);

    return $balance;
}

function EJGetJourneyTravelers($jid) {
    $sql = "select person.Name as name" .
         " from "
         "person, mapjourneyperson"
         " where " .
         "mapjourneyperson.Person=person.ID" .
         " and " .
         "mapjourneyperson.Journey=" . $jid;
    $result = "";
    EJReadTable($sql, function ($row) use (&$result) {
        $result .= ($row["name"] . ", ");
    });
    $result = rtrim($result, ", ");

    return $result;
}

function EJGetJourney(&$journeyParams) {
    $aid = "aidJourney";
    return EJExecuteWithAuthenticatedFamily($aid, $journeyParams, function ($fid, $aid, &$journeyParams) {
        $paramOffset = 1; # The first one is the whole string from reg match
        $startDate = $journeyParams[W3GetAPIParamIndex($aid, "from") + $paramOffset];
        $endDate = $journeyParams[W3GetAPIParamIndex($aid, "to") + $paramOffset];

        $sql = "select " .
             "journey.Datetime as datetime, journey.Name as name, journey.Note as note, journey.ID as id," .
             "financeevent.Budget as budget, financeevent.Name as event, financeevent.ID as eid" .
             " from " .
             "journey, financeevent"
             " where " .
             "journey.Datetime >= '" . $startDate . "' and journey.Datetime <= '" . $endDate . "'" .
             " and " .
             "journey.Event = financeevent.ID" .
             " and " .
             "financeevent.FID = " . $fid .
             " order by journey.Datetime asc";

        $result = "{" . W3CreateSuccessfulResult(false) . "," . W3MakeString(w3ApiResultData) . ":[";
        EJReadTable($sql, function ($row) use (&$result, $aid) {
            $apiDef = W3GetAPIDef($aid);
            $columns = $apiDef[w3ApiResult][w3ApiResultData];
            $result .= "{";

            foreach ($columns as $value) {
                if ($value[w3ApiDataValue] == "balance") {
                    $balance = EJCalculateJourneyEventBalance($row["eid"], $row["budget"]);
                    $result .= W3MakeString($value[w3ApiDataValue]) . ":" . W3MakeString($balance) . ",";
                } else if ($value[w3ApiDataValue] == "traveler") {
                    $travelers = EJGetJourneyTravelers($row["id"]);
                    $result .= W3MakeString($value[w3ApiDataValue]) . ":" . W3MakeString($travelers) . ",";
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
        $eventStr = $parameters[W3GetAPIParamIndex($aid, "event") + $paramOffset];
        $travelerStr = $parameters[W3GetAPIParamIndex($aid, "traveler") + $paramOffset];
        $travelers = explode(",", $travelerStr);
        if (sizeof($travelers) <= 0) {
            W3LogError("No traveler of journey");
            return W3CreateFailedResult();
        }

        $eventID = null;
        if ($eventStr != "") {
            $eventFamilyID = null;
            if (!EJGetEventInfo(trim($eventStr), $eventID, $eventFamilyID)) {
                W3LogError("Event of journey is not existed: " . $eventStr);
                return W3CreateFailedResult();
            }

            if ($eventFamilyID != $familyID) {
                W3LogError("Event of journey is not in same family: " . $eventStr);
                return W3CreateFailedResult();
            }
        }

        $persons = array();
        foreach ($travelers as $personName) {
            $personFamilyID = null;
            $personID = null;
            if (!EJGetPersonInfo(trim($personName), $personID, $personFamilyID)) {
                W3LogError("Traveler of journey is not existed: " . $personName);
                return W3CreateFailedResult();
            }

            if ($personFamilyID != $familyID) {
                W3LogError("Traveler of journey is not in same family: " . $personName);
                return W3CreateFailedResult();
            }

            array_push($persons, $personID);
        }

        if (EJInsertJourney($parameters, $eventID)) {
            if (EJMapJourneyToPerson($persons)) {
                return W3CreateSuccessfulResult();
            }
        }

        return W3CreateFailedResult();
    });
}

 ?>
