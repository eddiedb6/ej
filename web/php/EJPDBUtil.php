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
    
    $values = array($billParams[W3GetAPIParamIndex("aidAddBill", "owner") + $paramOffset],
                    W3MakeString($billParams[W3GetAPIParamIndex("aidAddBill", "datetime") + $paramOffset], true),
                    $billParams[W3GetAPIParamIndex("aidAddBill", "amount") + $paramOffset],
                    $billParams[W3GetAPIParamIndex("aidAddBill", "currency") + $paramOffset],
                    $billParams[W3GetAPIParamIndex("aidAddBill", "category") + $paramOffset],
                    $billParams[W3GetAPIParamIndex("aidAddBill", "paymentmode") + $paramOffset],
                    W3MakeString($billParams[W3GetAPIParamIndex("aidAddBill", "note") + $paramOffset], true));
    $sql = "insert into bill (" . implode(",", $columns) . ") values (" . implode("," , $values) . ")";

    if (!$ejConn->query($sql)) {
        W3LogWarning("Execute bill insert SQL failed");
        return false;
    }

    // Then map bill to finance event

    $events = $billParams[W3GetAPIParamIndex("aidAddBill", "event") + $paramOffset];
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

function EJInsertDebt(&$debtParams) {
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

    $balanceVal = $debtParams[W3GetAPIParamIndex("aidAddDebt", "balance") + $paramOffset];
    if ($balanceVal == "") {
        $balanceVal = "0";
    }
    $values = array(W3MakeString($debtParams[W3GetAPIParamIndex("aidAddDebt", "start") + $paramOffset], true),
                    W3MakeString($debtParams[W3GetAPIParamIndex("aidAddDebt", "end") + $paramOffset], true),
                    $debtParams[W3GetAPIParamIndex("aidAddDebt", "amount") + $paramOffset],
                    $balanceVal,
                    W3MakeString($debtParams[W3GetAPIParamIndex("aidAddDebt", "note") + $paramOffset], true),
                    1); # [ED] PENDING: Handle FID
    $sql = "insert into debt (" . implode(",", $columns) . ") values (" . implode("," , $values) . ")";
    if (!$ejConn->query($sql)) {
        W3LogWarning("Execute debt insert SQL failed");
        return false;
    }

    return true;
}

function EJInsertFinanceEvent(&$eventParams) {
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
    
    $values = array(W3MakeString($eventParams[W3GetAPIParamIndex("aidAddFinanceEvent", "name") + $paramOffset], true),
                    $eventParams[W3GetAPIParamIndex("aidAddFinanceEvent", "budget") + $paramOffset],
                    W3MakeString($eventParams[W3GetAPIParamIndex("aidAddFinanceEvent", "note") + $paramOffset], true),
                    1); # [ED] PENDING: Handle FID
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
    
    $values = array($incomeParams[W3GetAPIParamIndex("aidAddIncome", "owner") + $paramOffset],
                    W3MakeString($incomeParams[W3GetAPIParamIndex("aidAddIncome", "datetime") + $paramOffset], true),
                    $incomeParams[W3GetAPIParamIndex("aidAddIncome", "amount") + $paramOffset],
                    $incomeParams[W3GetAPIParamIndex("aidAddIncome", "currency") + $paramOffset],
                    $incomeParams[W3GetAPIParamIndex("aidAddIncome", "category") + $paramOffset],
                    W3MakeString($incomeParams[W3GetAPIParamIndex("aidAddIncome", "note") + $paramOffset], true));
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

function EJInsertNote(&$noteParams, &$postParams) {
    global $ejConn;

    if (!EJConnectDB()) {
        W3LogWarning("No DB connection when insert note");
        return false;
    }

    $columns = array ("Title", "Tag", "Note", "Modified");
    $size = sizeof($columns);

    $uselessParamCount = 2; # Match string, session, etc.
    $paramOffset = 1; # 0 is for the whole match string in reg                       
    if (sizeof($noteParams) + sizeof($postParams) - $uselessParamCount != $size) {
        W3LogError("No enough fields for note insert: require " .
                   strval($size - 1) . # "Modified" not from param
                   " but actual is " .
                   strval(sizeof($noteParams) - $paramOffset + sizeof($postParams) - $paramOffset));
        return false;
    }

    date_default_timezone_set("Asia/Shanghai");
    $datetime = W3MakeString(date("Y-m-d H:i:s"), true);
    $values = array(W3MakeString($noteParams[W3GetAPIParamIndex("aidAddNote", "title") + $paramOffset], true),
                    $noteParams[W3GetAPIParamIndex("aidAddNote", "tag") + $paramOffset],
                    W3MakeString($postParams[W3GetAPIPostIndex("aidAddNote", "note") + $paramOffset]),
                    $datetime);
    $sql = "insert into note (" . implode(",", $columns) . ") values (" . implode("," , $values) . ")";

    if (!$ejConn->query($sql)) {
        W3LogWarning("Execute note insert SQL failed");
        return false;
    }

    return true;
}

function EJInsertCalendarEvent(&$eventParams) {
    global $ejConn;

    if (!EJConnectDB()) {
        W3LogWarning("No DB connection when insert calendar event");
        return false;
    }

    $columns = array ("Name", "Datetime", "RepeatMonth", "Note");
    $size = sizeof($columns);

    $uselessParamCount = 2; # Match string, session, etc.
    $paramOffset = 1; # 0 is for the whole match string in reg                       
    if (sizeof($eventParams) - $uselessParamCount != $size) {
        W3LogError("No enough fields for calendar event insert: require " .
                   strval($size) .
                   " but actual is " .
                   strval(sizeof($eventParams) - $paramOffset));
        return false;
    }

    $aid = "aidAddCalendarEvent";
    $values = array(W3MakeString($eventParams[W3GetAPIParamIndex($aid, "name") + $paramOffset], true),
                    W3MakeString($eventParams[W3GetAPIParamIndex($aid, "datetime") + $paramOffset], true),
                    $eventParams[W3GetAPIParamIndex($aid, "repeatmonth") + $paramOffset],
                    W3MakeString($eventParams[W3GetAPIParamIndex($aid, "note") + $paramOffset], true));
    $sql = "insert into calendar (" . implode(",", $columns) . ") values (" . implode("," , $values) . ")";
    if (!$ejConn->query($sql)) {
        W3LogWarning("Execute calendar event insert SQL failed");
        return false;
    }

    return true;
}

function EJUpdateNote(&$noteParams, &$postParams) {
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

    $sql = "update note set Note=" . $newNote . ", Modified=" . $datetime . "  where ID=" . $id;

    if (!$ejConn->query($sql)) {
        W3LogWarning("Execute note update SQL failed");
        return false;
    }

    return true;
}

 ?>
