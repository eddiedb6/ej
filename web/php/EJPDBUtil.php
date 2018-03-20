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

function EJInsertBill(&$bill) {
    global $ejConn;

    if (!EJConnectDB()) {
        W3LogWarning("No DB connection when insert bill");
        return false;
    }

    # First insert bill
    
    $columns = array ("PID", "Datetime", "Amount", "Currency", "Category", "PaymentMode", "Note");
    $size = sizeof($columns);

    if (sizeof($bill) - 3 != $size) {
        W3LogError("No enough fields for bill insert: require " .
                   strval($size) .
                   " but actual is " .
                   strval(sizeof($bill) - 1));
        return false;
    }
    
    $values = array($bill[W3GetAPIParamIndex("aidAddBill", "owner") + 1],
                    W3MakeString($bill[W3GetAPIParamIndex("aidAddBill", "datetime") + 1], true),
                    $bill[W3GetAPIParamIndex("aidAddBill", "amount") + 1],
                    $bill[W3GetAPIParamIndex("aidAddBill", "currency") + 1],
                    $bill[W3GetAPIParamIndex("aidAddBill", "category") + 1],
                    $bill[W3GetAPIParamIndex("aidAddBill", "paymentmode") + 1],
                    W3MakeString($bill[W3GetAPIParamIndex("aidAddBill", "note") + 1], true));
    $sql = "insert into bill (" . implode(",", $columns) . ") values (" . implode("," , $values) . ")";

    if (!$ejConn->query($sql)) {
        W3LogWarning("Execute bill insert SQL failed");
        return false;
    }

    // Then map bill to finance event

    $events = $bill[W3GetAPIParamIndex("aidAddBill", "event") + 1];
    if (trim($events) == "") {
        return true;
    }
    
    $pid = $bill[W3GetAPIParamIndex("aidAddBill", "owner") + 1];
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

function EJInsertDebt(&$debt) {
    global $ejConn;

    if (!EJConnectDB()) {
        W3LogWarning("No DB connection when insert debt");
        return false;
    }

    $columns = array ("Start", "End", "Amount", "Balance", "Note", "FID");
    $size = sizeof($columns);

    if (sizeof($debt) - 1 != $size) {
        W3LogError("No enough fields for debt insert: require " .
                   strval($size) .
                   " but actual is " .
                   strval(sizeof($debt) - 1));
        return false;
    }
    
    $values = array(W3MakeString($debt[W3GetAPIParamIndex("aidAddDebt", "start") + 1], true),
                    W3MakeString($debt[W3GetAPIParamIndex("aidAddDebt", "end") + 1], true),
                    $debt[W3GetAPIParamIndex("aidAddDebt", "amount") + 1],
                    $debt[W3GetAPIParamIndex("aidAddDebt", "balance") + 1],
                    W3MakeString($debt[W3GetAPIParamIndex("aidAddDebt", "note") + 1], true),
                    1); # [ED] PENDING: Handle FID
    $sql = "insert into debt (" . implode(",", $columns) . ") values (" . implode("," , $values) . ")";
    if (!$ejConn->query($sql)) {
        W3LogWarning("Execute debt insert SQL failed");
        return false;
    }

    return true;
}

function EJInsertFinanceEvent(&$event) {
    global $ejConn;

    if (!EJConnectDB()) {
        W3LogWarning("No DB connection when insert finance event");
        return false;
    }

    $columns = array ("Name", "Budget", "Note", "FID");
    $size = sizeof($columns);

    if (sizeof($event) -1 != $size) {
        W3LogError("No enough fields for finance event insert: require " .
                   strval($size) .
                   " but actual is " .
                   strval(sizeof($event) - 1));
        return false;
    }
    
    $values = array(W3MakeString($event[W3GetAPIParamIndex("aidAddFinanceEvent", "name") + 1], true),
                    $event[W3GetAPIParamIndex("aidAddFinanceEvent", "budget") + 1],
                    W3MakeString($event[W3GetAPIParamIndex("aidAddFinanceEvent", "note") + 1], true),
                    1); # [ED] PENDING: Handle FID
    $sql = "insert into financeevent (" . implode(",", $columns) . ") values (" . implode("," , $values) . ")";
    if (!$ejConn->query($sql)) {
        W3LogWarning("Execute finance event insert SQL failed");
        return false;
    }

    return true;
}

function EJInsertIncome(&$income) {
    global $ejConn;

    if (!EJConnectDB()) {
        W3LogWarning("No DB connection when insert income");
        return false;
    }

    $columns = array ("PID", "Datetime", "Amount", "Currency", "Category", "Note");
    $size = sizeof($columns);

    if (sizeof($income) - 2 != $size) {
        W3LogError("No enough fields for income insert: require " .
                   strval($size) .
                   " but actual is " .
                   strval(sizeof($income) - 1));
        return false;
    }
    
    $values = array($income[W3GetAPIParamIndex("aidAddIncome", "owner") + 1],
                    W3MakeString($income[W3GetAPIParamIndex("aidAddIncome", "datetime") + 1], true),
                    $income[W3GetAPIParamIndex("aidAddIncome", "amount") + 1],
                    $income[W3GetAPIParamIndex("aidAddIncome", "currency") + 1],
                    $income[W3GetAPIParamIndex("aidAddIncome", "category") + 1],
                    W3MakeString($income[W3GetAPIParamIndex("aidAddIncome", "note") + 1], true));
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

function EJInsertNote(&$note) {
    global $ejConn;

    if (!EJConnectDB()) {
        W3LogWarning("No DB connection when insert note");
        return false;
    }

    $columns = array ("Title", "Tag", "Note", "Modified");
    $size = sizeof($columns);

    if (sizeof($note) - 1 != $size) {
        W3LogError("No enough fields for note insert: require " .
                   strval($size - 1) .
                   " but actual is " .
                   strval(sizeof($note) - 2));
        return false;
    }

    $datetime = '2018-03-20';
    $values = array(W3MakeString($note[W3GetAPIParamIndex("aidAddNote", "title") + 1], true),
                    $note[W3GetAPIParamIndex("aidAddNote", "tag") + 1],
                    W3MakeString($note[W3GetAPIParamIndex("aidAddNote", "note") + 1], true),
                    W3MakeString($datetime, true));
    $sql = "insert into note (" . implode(",", $columns) . ") values (" . implode("," , $values) . ")";

    if (!$ejConn->query($sql)) {
        W3LogWarning("Execute note insert SQL failed");
        return false;
    }

    return true;
}

function EJUpdateNote(&$note) {
    global $ejConn;

    if (!EJConnectDB()) {
        W3LogWarning("No DB connection when modify note");
        return false;
    }

    if (sizeof($note) - 1 != 3) {
        W3LogError("No enough fields for note modify: require 2 but actual is " . strval(sizeof($note) - 2));
        return false;
    }

    $datetime = W3MakeString('2018-03-20', true);
    $newNote = W3MakeString($note[W3GetAPIParamIndex("aidModifyNote", "note") + 1], true);
    $id = $note[W3GetAPIParamIndex("aidModifyNote", "id") + 1];

    $sql = "update note set Note=" . $newNote . ", Modified=" . $datetime . "  where ID=" . $id;

    return var_dump($note) . " " . $sql;
    
    if (!$ejConn->query($sql)) {
        W3LogWarning("Execute note update SQL failed");
        return false;
    }

    return true;
}

 ?>
