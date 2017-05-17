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
    
    $columns = array ("PID", "Datetime", "Amount", "Currency", "Category", "Scene", "PaymentMode", "Note");
    $size = sizeof($columns);

    if (sizeof($bill) - 2 != $size) {
        W3LogError("No enough fields for bill insert: require " .
                   strval($size) .
                   " but actual is " .
                   strval(sizeof($bill) - 1));
        return false;
    }
    
    $values = array($bill[1],
                    W3MakeString($bill[2], true),
                    $bill[3],
                    $bill[4],
                    $bill[5],
                    $bill[6],
                    $bill[7],
                    W3MakeString($bill[8], true));
    $sql = "insert into bill (" . implode(",", $columns) . ") values (" . implode("," , $values) . ")";

    if (!$ejConn->query($sql)) {
        W3LogWarning("Execute bill insert SQL failed");
        return false;
    }

    // Then map bill to finance event

    $events = $bill[9];
    if (trim($events) == "") {
        return true;
    }
    
    $pid = $bill[1];
    $maxIDSql = "select max(ID) from bill where bill.PID=" . $pid;
        
    EJReadTable($maxIDSql, function ($row) use ($events) {
        $billId = $row["max(ID)"];
        if (trim($billId) == "") {
            return;
        }
        
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

    if (sizeof($debt) != $size) {
        W3LogError("No enough fields for debt insert: require " .
                   strval($size) .
                   " but actual is " .
                   strval(sizeof($debt) - 1));
        return false;
    }
    
    $values = array(W3MakeString($debt[1], true),
                    W3MakeString($debt[2], true),
                    $debt[3],
                    $debt[4],
                    W3MakeString($debt[5], true),
                    1); # TODO, handle FID
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

    if (sizeof($event) != $size) {
        W3LogError("No enough fields for finance event insert: require " .
                   strval($size) .
                   " but actual is " .
                   strval(sizeof($event) - 1));
        return false;
    }
    
    $values = array(W3MakeString($event[1], true),
                    $event[2],
                    W3MakeString($event[3], true),
                    1); # TODO, handle FID
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

    if (sizeof($income) - 1 != $size) {
        W3LogError("No enough fields for income insert: require " .
                   strval($size) .
                   " but actual is " .
                   strval(sizeof($income) - 1));
        return false;
    }
    
    $values = array($income[1],
                    W3MakeString($income[2], true),
                    $income[3],
                    $income[4],
                    $income[5],
                    W3MakeString($income[6], true));
    $sql = "insert into income (" . implode(",", $columns) . ") values (" . implode("," , $values) . ")";
    if (!$ejConn->query($sql)) {
        W3LogWarning("Execute income insert SQL failed");
        return false;
    }

    return true;
}

 ?>