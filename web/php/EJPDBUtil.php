<?php

require "EJPDBConfig.php";

$ejConn;

function EJConnectDB() {
    global $ejConn;
    global $ejServer;
    global $ejUsername;
    global $ejPassword;
    global $ejDBName;

    $server = $ejServer;
    $username = $ejUsername;
    $password = $ejPassword;
    $dbname = $ejDBName;

    if ($ejConn) {
        return true;
    }
    
    $ejConn = new mysqli($server, $username, $password, $dbname);
    if ($ejConn->connect_error) {
        W3LogFatal($ejConn->connect_error);
        return false;
    }

    return true;
}

function EJCloseDB() {
    global $ejConn;

    if ($ejConn) {
        $ejConn->close();
    }
}

function EJExecuteSQL($sql) {
    global $ejConn;

    if (!EJConnectDB()) {
        W3LogWarning("No DB connection when exectue SQL");
        return false;
    }

    if (!$ejConn->query($sql)) {
        W3LogWarning("Execute SQL failed");
        return false;
    }

    return true;
}

function EJReadTable($sql, $callback) {
    global $ejConn;

    if (!EJConnectDB()) {
        W3LogWarning("No DB connection when read table");
        return false;
    }

    $result = $ejConn->query($sql);
    if ($result->num_rows > 0) {
        for ($row = 0; $row < $result->num_rows; $row++) {
            $result->data_seek($row);
            $rowData = $result->fetch_assoc();
            $callback($rowData);
        }
    }

    return true;
}

function EJInsertBill(&$billParams) {
    global $ejConn;

    if (!EJConnectDB()) {
        W3LogWarning("No DB connection when insert bill");
        return false;
    }

    # First insert bill
    
    $columns = array ("PID", "Datetime", "Amount", "Currency", "Category", "PaymentMode", "Note");
    $size = sizeof($columns);

    $uselessParamCount = 3; # Match string, session, etc.
    $paramOffset = 1; # 0 is for the whole match string in reg                       
    if (sizeof($billParams) - $uselessParamCount != $size) {
        W3LogError("No enough fields for bill insert: require " .
                   strval($size) .
                   " but actual is " .
                   strval(sizeof($billParams) - $paramOffset));
        return false;
    }

    $billNote = EJDecodeURLString($billParams[W3GetAPIParamIndex("aidAddBill", "note") + $paramOffset]);
    $values = array($billParams[W3GetAPIParamIndex("aidAddBill", "owner") + $paramOffset],
                    W3MakeString($billParams[W3GetAPIParamIndex("aidAddBill", "datetime") + $paramOffset], true),
                    $billParams[W3GetAPIParamIndex("aidAddBill", "amount") + $paramOffset],
                    $billParams[W3GetAPIParamIndex("aidAddBill", "currency") + $paramOffset],
                    $billParams[W3GetAPIParamIndex("aidAddBill", "category") + $paramOffset],
                    $billParams[W3GetAPIParamIndex("aidAddBill", "paymentmode") + $paramOffset],
                    W3MakeString($billNote, true));
    $sql = "insert into bill (" . implode(",", $columns) . ") values (" . implode("," , $values) . ")";

    if (!$ejConn->query($sql)) {
        W3LogWarning("Execute bill insert SQL failed");
        return false;
    }

    // Then map bill to finance event

    $events = EJDecodeURLString($billParams[W3GetAPIParamIndex("aidAddBill", "event") + $paramOffset]);
    if (trim($events) == "") {
        return true;
    }
    
    $pid = $billParams[W3GetAPIParamIndex("aidAddBill", "owner") + $paramOffset];
    $maxIDSql = "select max(ID) from bill where bill.PID=" . $pid;
        
    EJReadTable($maxIDSql, function ($row) use ($events) {
        $billId = $row["max(ID)"];
        if (trim($billId) == "") {
            return;
        }

        // Support multiple events separated by ","
        $eventsArray = explode(",", $events);
        foreach ($eventsArray as $value) {
            $event = trim($value);

            $eventSql = "select financeevent.ID from financeevent where financeevent.Name like " .
                      W3MakeString($event, true);
    
            EJReadTable($eventSql, function ($row) use ($billId) {
                global $ejConn;
            
                $eventId = $row["ID"];
                if (trim($eventId) == "") {
                    return;
                }
                
                $insertSql = "insert into mapbillfinanceevent (Bill, Event) values (" .
                           $billId . "," . $eventId . ")";

                if (!$ejConn->query($insertSql)) {
                    W3LogError("Execute map bill and finance event insert SQL failed");
                }
            });
        }
    });

    return true;
}

function EJInsertDebt(&$debtParams, $fid) {
    global $ejConn;

    if (!EJConnectDB()) {
        W3LogWarning("No DB connection when insert debt");
        return false;
    }

    $columns = array ("Start", "End", "Amount", "Balance", "Note", "FID");
    $size = sizeof($columns);

    $uselessParamCount = 1; # Match string, session, etc.
    $paramOffset = 1; # 0 is for the whole match string in reg                       
    if (sizeof($debtParams) - $uselessParamCount != $size) {
        W3LogError("No enough fields for debt insert: require " .
                   strval($size) .
                   " but actual is " .
                   strval(sizeof($debtParams) - $paramOffset));
        return false;
    }

    $debtNote = EJDecodeURLString($debtParams[W3GetAPIParamIndex("aidAddDebt", "note") + $paramOffset]);
    $balanceVal = $debtParams[W3GetAPIParamIndex("aidAddDebt", "balance") + $paramOffset];
    if ($balanceVal == "") {
        $balanceVal = "0";
    }
    $values = array(W3MakeString($debtParams[W3GetAPIParamIndex("aidAddDebt", "start") + $paramOffset], true),
                    W3MakeString($debtParams[W3GetAPIParamIndex("aidAddDebt", "end") + $paramOffset], true),
                    $debtParams[W3GetAPIParamIndex("aidAddDebt", "amount") + $paramOffset],
                    $balanceVal,
                    W3MakeString($debtNote, true),
                    $fid);
    $sql = "insert into debt (" . implode(",", $columns) . ") values (" . implode("," , $values) . ")";
    if (!$ejConn->query($sql)) {
        W3LogWarning("Execute debt insert SQL failed");
        return false;
    }

    return true;
}

function EJInsertFinanceEvent(&$eventParams, $fid) {
    global $ejConn;

    if (!EJConnectDB()) {
        W3LogWarning("No DB connection when insert finance event");
        return false;
    }

    $columns = array ("Name", "Budget", "Note", "FID");
    $size = sizeof($columns);

    $uselessParamCount = 1; # Match string, session, etc.
    $paramOffset = 1; # 0 is for the whole match string in reg                       
    if (sizeof($eventParams) - $uselessParamCount != $size) {
        W3LogError("No enough fields for finance event insert: require " .
                   strval($size) .
                   " but actual is " .
                   strval(sizeof($eventParams) - $paramOffset));
        return false;
    }

    $eventName = EJDecodeURLString($eventParams[W3GetAPIParamIndex("aidAddFinanceEvent", "name") + $paramOffset]);
    $eventNote = EJDecodeURLString($eventParams[W3GetAPIParamIndex("aidAddFinanceEvent", "note") + $paramOffset]);
    $values = array(W3MakeString($eventName, true),
                    $eventParams[W3GetAPIParamIndex("aidAddFinanceEvent", "budget") + $paramOffset],
                    W3MakeString($eventNote, true),
                    $fid);
    $sql = "insert into financeevent (" . implode(",", $columns) . ") values (" . implode("," , $values) . ")";
    if (!$ejConn->query($sql)) {
        W3LogWarning("Execute finance event insert SQL failed");
        return false;
    }

    return true;
}

function EJInsertIncome(&$incomeParams) {
    global $ejConn;

    if (!EJConnectDB()) {
        W3LogWarning("No DB connection when insert income");
        return false;
    }

    $columns = array ("PID", "Datetime", "Amount", "Currency", "Category", "Note");
    $size = sizeof($columns);

    $uselessParamCount = 2; # Match string, session, etc.
    $paramOffset = 1; # 0 is for the whole match string in reg                       
    if (sizeof($incomeParams) - $uselessParamCount != $size) {
        W3LogError("No enough fields for income insert: require " .
                   strval($size) .
                   " but actual is " .
                   strval(sizeof($incomeParams) - $paramOffset));
        return false;
    }

    $incomeNote = EJDecodeURLString($incomeParams[W3GetAPIParamIndex("aidAddIncome", "note") + $paramOffset]);
    $values = array($incomeParams[W3GetAPIParamIndex("aidAddIncome", "owner") + $paramOffset],
                    W3MakeString($incomeParams[W3GetAPIParamIndex("aidAddIncome", "datetime") + $paramOffset], true),
                    $incomeParams[W3GetAPIParamIndex("aidAddIncome", "amount") + $paramOffset],
                    $incomeParams[W3GetAPIParamIndex("aidAddIncome", "currency") + $paramOffset],
                    $incomeParams[W3GetAPIParamIndex("aidAddIncome", "category") + $paramOffset],
                    W3MakeString($incomeNote, true));
    $sql = "insert into income (" . implode(",", $columns) . ") values (" . implode("," , $values) . ")";
    if (!$ejConn->query($sql)) {
        W3LogWarning("Execute income insert SQL failed");
        return false;
    }

    return true;
}

function EJInsertExchangeRate($date, $currency) {
    global $ejConn;

    if (!EJConnectDB()) {
        W3LogWarning("No DB connection when insert exchange rate");
        return false;
    }

    $sql = "insert into exchangerate (Datetime, Currency) values ('" . $date . "', " . $currency . ");";
    if (!$ejConn->query($sql)) {
        W3LogWarning("Execute exchange rate insert SQL failed");
        return false;
    }

    return true;
}

function EJInsertNote(&$noteParams, &$postParams, $fid) {
    global $ejConn;

    if (!EJConnectDB()) {
        W3LogWarning("No DB connection when insert note");
        return false;
    }

    $columns = array ("Title", "Tag", "Type", "Note", "Modified", "FID");
    $size = sizeof($columns);

    $uselessParamCount = 2; # Match string, session, etc.
    $paramOffset = 1; # 0 is for the whole match string in reg                       
    if (sizeof($noteParams) + sizeof($postParams) - $uselessParamCount != $size - 1) { # 1 for FID
        W3LogError("No enough fields for note insert: require " .
                   strval($size - 2) . # "Modified" not from param, also FID
                   " but actual is " .
                   strval(sizeof($noteParams) - $paramOffset + sizeof($postParams) - $paramOffset));
        return false;
    }

    date_default_timezone_set("Asia/Shanghai");
    $datetime = W3MakeString(date("Y-m-d H:i:s"), true);
    $values = array(W3MakeString($noteParams[W3GetAPIParamIndex("aidAddNote", "title") + $paramOffset], true),
                    $noteParams[W3GetAPIParamIndex("aidAddNote", "tag") + $paramOffset],
                    $noteParams[W3GetAPIParamIndex("aidAddNote", "type") + $paramOffset],
                    W3MakeString($postParams[W3GetAPIPostIndex("aidAddNote", "note") + $paramOffset]),
                    $datetime,
                    $fid);
    $sql = "insert into note (" . implode(",", $columns) . ") values (" . implode("," , $values) . ")";

    if (!$ejConn->query($sql)) {
        W3LogWarning("Execute note insert SQL failed");
        return false;
    }

    return true;
}

function EJUpdateNote(&$noteParams, &$postParams, $fid) {
    global $ejConn;

    if (!EJConnectDB()) {
        W3LogWarning("No DB connection when modify note");
        return false;
    }

    $uselessParamCount = 3; # Match string, session, etc.
    $paramOffset = 1; # 0 is for the whole match string in reg                       
    $columnCount = 2; # Note, ID
    if (sizeof($noteParams) + sizeof($postParams) - $uselessParamCount != $columnCount) {
        W3LogError("No enough fields for note modify: require " .
                   strval($columnCount) .
                   " but actual is " .
                   strval(sizeof($noteParams) - $paramOffset + sizeof($postParams) - $paramOffset));
        return false;
    }

    date_default_timezone_set("Asia/Shanghai");
    $datetime = W3MakeString(date("Y-m-d H:i:s"), true);
    $newNote = W3MakeString($postParams[W3GetAPIPostIndex("aidModifyNote", "note") + $paramOffset]);
    $id = $noteParams[W3GetAPIParamIndex("aidModifyNote", "id") + $paramOffset];

    $sql = "update note set Note=" . $newNote . ", Modified=" . $datetime . "  where ID=" . $id . " and FID=" . $fid;

    if (!$ejConn->query($sql)) {
        W3LogWarning("Execute note update SQL failed");
        return false;
    }

    return true;
}

function EJInsertCalendarEvent(&$eventParams, $fid) {
    global $ejConn;

    if (!EJConnectDB()) {
        W3LogWarning("No DB connection when insert calendar event");
        return false;
    }

    $columns = array ("Name", "Datetime", "RepeatMonth", "Note", "FID");
    $size = sizeof($columns);

    $uselessParamCount = 2; # Match string, session, etc.
    $paramOffset = 1; # 0 is for the whole match string in reg                       
    if (sizeof($eventParams) - $uselessParamCount != $size - 1) { # 1 for FID
        W3LogError("No enough fields for calendar event insert: require " .
                   strval($size - 1) . # 1 for FID
                   " but actual is " .
                   strval(sizeof($eventParams) - $paramOffset));
        return false;
    }

    $aid = "aidAddCalendarEvent";

    $eventName = EJDecodeURLString($eventParams[W3GetAPIParamIndex($aid, "name") + $paramOffset]);
    $eventNote = EJDecodeURLString($eventParams[W3GetAPIParamIndex($aid, "note") + $paramOffset]);
    $values = array(W3MakeString($eventName, true),
                    W3MakeString($eventParams[W3GetAPIParamIndex($aid, "datetime") + $paramOffset], true),
                    $eventParams[W3GetAPIParamIndex($aid, "repeatmonth") + $paramOffset],
                    W3MakeString($eventNote, true),
                    $fid);
    $sql = "insert into calendar (" . implode(",", $columns) . ") values (" . implode("," , $values) . ")";
    if (!$ejConn->query($sql)) {
        W3LogWarning("Execute calendar event insert SQL failed");
        return false;
    }

    return true;
}

function EJInsertJourney(&$journeyParams, $eventID) {
    global $ejConn;

    if (!EJConnectDB()) {
        W3LogWarning("No DB connection when insert journey");
        return false;
    }

    $columns = array ("Name", "Datetime", "Note");
    $size = sizeof($columns);

    $uselessParamCount = 4; # Match string, session, etc. And "Event" will be check later
    $paramOffset = 1; # 0 is for the whole match string in reg
    if (sizeof($journeyParams) - $uselessParamCount != $size) {
        W3LogError("No enough fields for journey insert: require " .
                   strval($size) .
                   " but actual is " .
                   strval(sizeof($journeyParams) - $paramOffset));
        return false;
    }

    $aid = "aidAddJourney";
    $journeyNote = EJDecodeURLString($journeyParams[W3GetAPIParamIndex($aid, "note") + $paramOffset]);
    $journeyName = EJDecodeURLString($journeyParams[W3GetAPIParamIndex($aid, "name") + $paramOffset]);
    $values = array(W3MakeString($journeyName, true),
                    W3MakeString($journeyParams[W3GetAPIParamIndex($aid, "datetime") + $paramOffset], true),
                    W3MakeString($journeyNote, true));

    if ($eventID != null) {
        array_push($columns, "Event");
        array_push($values, $eventID);
    }

    $sql = "insert into journey (" . implode(",", $columns) . ") values (" . implode("," , $values) . ")";

    if (!$ejConn->query($sql)) {
        W3LogWarning("Execute journey insert SQL failed");
        return false;
    }

    return true;
}

function EJInsertJourneyPlace(&$placeParams, $aid) {
    global $ejConn;

    $placeID = -1;

    if (!EJConnectDB()) {
        W3LogWarning("No DB connection when insert journey place");
        return $placeID;
    }

    $paramOffset = 1; # 0 is for the whole match string in reg
    $name = $placeParams[W3GetAPIParamIndex($aid, "name") + $paramOffset]; # This name will be Decode by client
    $latitude = $placeParams[W3GetAPIParamIndex($aid, "latitude") + $paramOffset];
    $longitude = $placeParams[W3GetAPIParamIndex($aid, "longitude") + $paramOffset];

    // First check whether the place is there already

    $querySql = "select ID as id from journeyplace where " .
              "Latitude=" . $latitude .
              " and Longitude=" . $longitude;
    EJReadTable($querySql, function ($row) use (&$placeID) {
        $placeID = $row["id"];
    });

    if ($placeID >= 0) {
        return $placeID;
    }

    // Then if not place existed, add a new one

    $columns = array ("Name", "Latitude", "Longitude");
    $values = array(W3MakeString($name), $latitude, $longitude);
    $insertSql = "insert into journeyplace (" . implode(",", $columns) . ") values (" . implode("," , $values) . ")";
    if (!$ejConn->query($insertSql)) {
        W3LogWarning("Execute journey place insert SQL failed");
        return $placeID;
    }

    // Return the new place ID

    $maxIDSql = "select max(ID) from journeyplace";
    EJReadTable($maxIDSql, function ($row) use (&$placeID) {
        $placeID = $row["max(ID)"];
    });

    return $placeID;
}

function EJInsertJourneyNote(&$noteParams, $placeID) {
    global $ejConn;

    if (!EJConnectDB()) {
        W3LogWarning("No DB connection when insert journey note");
        return false;
    }

    $aid = "aidAddJourneyPlace";
    $paramOffset = 1; # The first one is alway whole string from reg match
    $journeyID = $noteParams[W3GetAPIParamIndex($aid, "jid") + $paramOffset];
    $datetime = $noteParams[W3GetAPIParamIndex($aid, "datetime") + $paramOffset];
    $remark = $noteParams[W3GetAPIParamIndex($aid, "remark") + $paramOffset];
    $note = EJDecodeURLString($noteParams[W3GetAPIParamIndex($aid, "note") + $paramOffset]);

    $columns = array ("Journey", "Place", "Datetime", "Remark", "Note");
    $values = array($journeyID, $placeID, W3MakeString($datetime), $remark, W3MakeString($note));
    $insertSql = "insert into journeynote (" . implode(",", $columns) . ") values (" . implode("," , $values) . ")";
    if (!$ejConn->query($insertSql)) {
        W3LogWarning("Execute journey note insert SQL failed");
        return false;
    }

    return true;
}

function EJInsertPOI(&$noteParams, $placeID, $fid) {
    global $ejConn;

    if (!EJConnectDB()) {
        W3LogWarning("No DB connection when insert POI");
        return false;
    }

    $aid = "aidAddPOI";
    $paramOffset = 1; # The first one is alway whole string from reg match
    $note = EJDecodeURLString($noteParams[W3GetAPIParamIndex($aid, "note") + $paramOffset]);

    $columns = array ("FID", "Place", "Note");
    $values = array($fid, $placeID, W3MakeString($note));
    $insertSql = "insert into poi (" . implode(",", $columns) . ") values (" . implode("," , $values) . ")";
    if (!$ejConn->query($insertSql)) {
        W3LogWarning("Execute POI insert SQL failed");
        return false;
    }

    return true;
}

function EJGetPersonInfo($personName) {
    $sql = "select " .
         "person.ID, person.FID" .
         " from " .
         "person" .
         " where " .
         "person.Name = " . W3MakeString($personName);

    $personInfo = array();
    EJReadTable($sql, function ($row) use (&$personInfo) {
        $personInfo["ID"] = $row["ID"];
        $personInfo["FID"] = $row["FID"];
    });

    return $personInfo;
}

function EJGetEventInfo($eventName, $eventID) {
    $condition = "";
    if ($eventName != null) {
        $condition = "Name = " . W3MakeString($eventName);
    } else if ($eventID != null) {
        $condition = "ID = " . W3MakeString($eventID);
    } else {
        W3LogWarning("Neither of event name nor id is valid when try to get event info");
        return array();
    }

    $sql = "select " .
         "ID, FID, Name, Budget" .
         " from " .
         "financeevent" .
         " where " . $condition;

    $eventInfo = array();
    EJReadTable($sql, function ($row) use (&$eventInfo) {
        $eventInfo["ID"] = $row["ID"];
        $eventInfo["FID"] = $row["FID"];
        $eventInfo["Name"] = $row["Name"];
        $eventInfo["Budget"] = $row["Budget"];
    });

    return $eventInfo;
}

function EJMapJourneyToPerson(&$persons) {
    $result = false;

    $maxIDSql = "select max(ID) from journey";
    EJReadTable($maxIDSql, function ($row) use (&$persons, &$result) {
        global $ejConn;

        if (!EJConnectDB()) {
            W3LogWarning("No DB connection when map journey and person");
            return;
        }

        $journeyID = $row["max(ID)"];
        if (trim($journeyID) == "") {
            return;
        }

        foreach ($persons as $pid) {
            $insertSql = "insert into mapjourneyperson (Journey, Person) values (" . $journeyID . ", " . $pid . ")";
            if (!$ejConn->query($insertSql)) {
                W3LogWarning("Execute journey person insert SQL failed");
                return;
            }
        }

        $result = true;
    });

    return $result;
}

function EJReadSingleResultFromTable($aid, $sql) {
    return EJReadResultFromTable($aid, $sql, false);
}

function EJReadMultiResultFromTable($aid, $sql) {
    return EJReadResultFromTable($aid, $sql, true);
}

function EJReadResultFromTable($aid, $sql, $isResultArray) {
    $result = "{" . W3CreateSuccessfulResult(false) . "," . W3MakeString(w3ApiResultData) . ($isResultArray ? ":[" : ":{");
    EJReadTable($sql, function ($row) use (&$result, $aid, $isResultArray) {
        $apiDef = W3GetAPIDef($aid);
        $columns = $apiDef[w3ApiResult][w3ApiResultData];
        if ($isResultArray) {
            $result .= "{";
        }
        foreach ($columns as $value) {
            $resultForColumn = $row[$value[w3ApiDataValue]];
            $result .= W3MakeString($value[w3ApiDataValue]) . ":" . W3MakeString($resultForColumn) . ",";
        }
        if ($isResultArray) {
            $result = rtrim($result, ",") . "},";
        }
    });
    $result = rtrim($result, ",") . ($isResultArray ? "]}" : "}}");

    return $result;
}

 ?>
