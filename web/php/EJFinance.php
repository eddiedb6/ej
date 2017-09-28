<?php

function EJGetBill(&$filter) {
    if (!isset($filter) or sizeof($filter) != 3) {
        W3LogError("Get bill filter is not correct: " . var_dump($filter));
        return W3CreateFailedResult();
    }

    $sql = "select " .
         "bill.Datetime as datetime, bill.Amount as amount, bill.Currency as currencyID, bill.Note as note," .
         "person.Name as owner," .
         "currency.SID as currency," .
         "paymentmode.SID as paymentmode," .
         "billcategory.SID as category" .
         " from " .
         "bill, currency, paymentmode, billcategory, person" .
         " where " .
         "bill.Datetime >= '" . $filter[1] . "' and bill.Datetime <= '" . $filter[2] . "'" .
         " and " .
         "bill.PID = person.ID" . 
         " and " .
         "bill.Currency = currency.ID" .
         " and " .
         "bill.PaymentMode = paymentmode.ID" .
         " and " .
         "bill.Category = billcategory.ID" .
         " and " .
         "bill.PID in (select person.ID from person where person.FID=1)" . # [ED] PENDING: Handle FID
         " order by bill.Datetime asc";
    $result = "{" . W3CreateSuccessfulResult(false) . "," . W3MakeString(w3ApiResultData) . ":[";
    EJReadTable($sql, function ($row) use (&$result) {
        $apiDef = W3GetAPIDef("aidBill");
        $columns = $apiDef[w3ApiResult][w3ApiResultData];
        $result .= "{";
        foreach ($columns as $value) {
            $resultForColumn = $row[$value[w3ApiDataValue]];
            // Attach exchange rate
            if ($value[w3ApiDataValue] == "amount") {
                $date = explode(" ", $row["datetime"])[0];
                $resultForColumn .= "|" . EJGetExchangeRateString($date, $row["currencyID"]);
            }
            $result .= W3MakeString($value[w3ApiDataValue]) . ":" . W3MakeString($resultForColumn) . ",";
        }
        $result = rtrim($result, ",") . "},";
    });
    $result = rtrim($result, ",") . "]}";

    return $result;
}

function EJGetDebt(&$filter) {
    if (!isset($filter) or sizeof($filter) != 3) {
        W3LogError("Get debt filter is not correct: " . var_dump($filter));
        return W3CreateFailedResult();
    }

    $sql = "select " .
         "debt.Start as start, debt.End as end, " .
         "debt.Amount as amount, debt.Balance as balance, debt.Note as note" .
         " from " .
         "debt" .
         " where FID=1 and " . # [ED] PENDING: Handle FID
         "(debt.Start <= '" . $filter[2] . "' and debt.End >= '" . $filter[1] . "')" .
         " order by debt.Start asc";
    $result = "{" . W3CreateSuccessfulResult(false) . "," . W3MakeString(w3ApiResultData) . ":[";
    EJReadTable($sql, function ($row) use (&$result) {
        $apiDef = W3GetAPIDef("aidDebt");
        $columns = $apiDef[w3ApiResult][w3ApiResultData];
        $result .= "{";
        foreach ($columns as $value) {
            $result .= W3MakeString($value[w3ApiDataValue]) . ":" . W3MakeString($row[$value[w3ApiDataValue]]) . ",";
        }
        $result = rtrim($result, ",") . "},";
    });
    $result = rtrim($result, ",") . "]}";

    return $result;
}

function EJGetFinanceEvent(&$filter) {
    if (!isset($filter) or sizeof($filter) != 2) {
        W3LogError("Get finance event filter is not correct: " . var_dump($filter));
        return W3CreateFailedResult();
    }

    $sql = "select " .
         "financeevent.ID as id, " .
         "financeevent.Name as name, " .
         "financeevent.Budget as budget, " .
         "financeevent.Note as note " .
         "from financeevent " .
         "where FID=1"; # [ED] PENDING: Handle FID
    if ($filter[1] != "") {
        $sql .= " and financeevent.Name like " . W3MakeString($filter[1], true);
    }
    $sql .= " order by financeevent.Name asc";
    $result = "{" . W3CreateSuccessfulResult(false) . "," . W3MakeString(w3ApiResultData) . ":[";
    EJReadTable($sql, function ($row) use (&$result) {
        $apiDef = W3GetAPIDef("aidFinanceEvent");
        $columns = $apiDef[w3ApiResult][w3ApiResultData];
        $result .= "{";

        // Calculate event balance
        $sql = "select bill.Amount as amount, bill.Datetime as datetime, bill.Currency as currency from bill where ID in (select Bill from mapbillfinanceevent where Event =" . $row["id"] . ")";
        $amount = EJSumCurrency($sql);
        $budget = "";
        foreach ($columns as $value) {
            if ($value[w3ApiDataValue] == "budget") {
                $budget = $row["budget"];
            }

            if ($value[w3ApiDataValue] == "balance") {
                $balance = sprintf("%01.2f", floatval($budget) - $amount);
                $result .= W3MakeString($value[w3ApiDataValue]) . ":" . W3MakeString($balance) . ",";
            } else {
                $result .= W3MakeString($value[w3ApiDataValue]) . ":" . W3MakeString($row[$value[w3ApiDataValue]]) . ",";
            }
        }

        $result = rtrim($result, ",") . "},";
    });
    $result = rtrim($result, ",") . "]}";

    return $result;
}

function EJGetIncome(&$filter) {
    if (!isset($filter) or sizeof($filter) != 3) {
        W3LogError("Get income filter is not correct: " . var_dump($filter));
        return W3CreateFailedResult();
    }

    $sql = "select " .
         "income.Datetime as datetime, income.Amount as amount, income.Currency as currencyID, income.Note as note," .
         "person.Name as owner," .
         "currency.SID as currency," .
         "incomecategory.SID as category" .
         " from " .
         "income, currency, incomecategory, person" .
         " where " .
         "income.Datetime >= '" . $filter[1] . "' and income.Datetime <= '" . $filter[2] . "'" .
         " and " .
         "income.PID = person.ID" . 
         " and " .
         "income.Currency = currency.ID" .
         " and " .
         "income.Category = incomecategory.ID" .
         " and " .
         "income.PID in (select person.ID from person where person.FID=1)" . # [ED] PENDING: Handle FID
         " order by income.Datetime asc";
    $result = "{" . W3CreateSuccessfulResult(false) . "," . W3MakeString(w3ApiResultData) . ":[";
    EJReadTable($sql, function ($row) use (&$result) {
        $apiDef = W3GetAPIDef("aidIncome");
        $columns = $apiDef[w3ApiResult][w3ApiResultData];
        $result .= "{";
        foreach ($columns as $value) {
            $resultForColumn = $row[$value[w3ApiDataValue]];
            if ($value[w3ApiDataValue] == "amount") {
                // Attach exchange rate
                $date = explode(" ", $row["datetime"])[0];
                $resultForColumn .= "|" . EJGetExchangeRateString($date, $row["currencyID"]);
            }
            $result .= W3MakeString($value[w3ApiDataValue]) . ":" . W3MakeString($resultForColumn) . ",";
        }
        $result = rtrim($result, ",") . "},";
    });
    $result = rtrim($result, ",") . "]}";
    
    return $result;
}

function EJGetFinanceReport(&$filter) {
    if (!isset($filter) or sizeof($filter) != 2) {
        W3LogError("Get finance report filter is not correct: " . var_dump($filter));
        return W3CreateFailedResult();
    }

    $time = explode("-", $filter[1]);
    $year = intval($time[0]);
    $month = intval($time[1]);

    $report = array(
        "income" => 0.0,
        "deposit" => 0.0,
        "debt" => 0.0,
        "consume" => 0.0,
        "balance" => 0.0,
        "incomeyear" => 0.0,
        "deposityear" => 0.0,
        "debtyear" => 0.0,
        "consumeyear" => 0.0,
        "balanceyear" => 0.0,
        "category" => "",
        "categoryyear" => "",
        "scene" => "",
        "sceneyear" => "",
        "paymentmode" => "",
        "paymentmodeyear" => ""
    );
    
    EJCalculateFinanceReport($year, $month, $report);
    
    $result = "{" . W3CreateSuccessfulResult(false) . "," . W3MakeString(w3ApiResultData) . ": {";
    $result .= "income:" . strval($report["income"]) . ",";
    $result .= "deposit:" . strval($report["deposit"]) . ",";
    $result .= "debt:" . strval($report["debt"]) . ",";
    $result .= "consume:" . strval($report["consume"]) . ",";
    $result .= "balance:" . strval($report["balance"]) . ",";
    $result .= "incomeyear:" . strval($report["incomeyear"]) . ",";
    $result .= "deposityear:" . strval($report["deposityear"]) . ",";
    $result .= "debtyear:" . strval($report["debtyear"]) . ",";
    $result .= "consumeyear:" . strval($report["consumeyear"]) . ",";
    $result .= "balanceyear:" . strval($report["balanceyear"]) . ",";
    $result .= "category:" . W3MakeString($report["category"], true) . ",";
    $result .= "categoryyear:" . W3MakeString($report["categoryyear"], true) . ",";
    $result .= "scene:" . W3MakeString($report["scene"], true) . ",";
    $result .= "sceneyear:" . W3MakeString($report["sceneyear"], true) . ",";
    $result .= "paymentmode:" . W3MakeString($report["paymentmode"], true) . ",";
    $result .= "paymentmodeyear:" . W3MakeString($report["paymentmodeyear"], true);
    $result .= "}}";
    
    return $result;
}

function EJAddBill(&$parameters) {
    if (isset($parameters)) {
        if (EJInsertBill($parameters)) {
            return W3CreateSuccessfulResult();
        }
    } else {
        W3LogError("Add bill parameters is not correct: " . var_dump($parameters));
    }

    return W3CreateFailedResult();
}

function EJAddDebt(&$parameters) {
    if (isset($parameters)) {
        if (EJInsertDebt($parameters)) {
            return W3CreateSuccessfulResult();
        }
    } else {
        W3LogError("Add debt parameters is not correct: " . var_dump($parameters));
    }

    return W3CreateFailedResult();
}

function EJAddFinanceEvent(&$parameters) {
    if (isset($parameters)) {
        if (EJInsertFinanceEvent($parameters)) {
            return W3CreateSuccessfulResult();
        }
    } else {
        W3LogError("Add finance event parameters is not correct: " . var_dump($parameters));
    }

    return W3CreateFailedResult();
}

function EJAddIncome(&$parameters) {
    if (isset($parameters)) {
        if (EJInsertIncome($parameters)) {
            return W3CreateSuccessfulResult();
        }
    } else {
        W3LogError("Add income parameters is not correct: " . var_dump($parameters));
    }

    return W3CreateFailedResult();
}

function EJGetExchangeRate(&$filter) {
    if (!isset($filter) or sizeof($filter) != 3) {
        W3LogError("Get exchange rate filter is not correct: " . var_dump($filter));
        return W3CreateFailedResult();
    }
 
    $result = NULL;
    $rate = EJGetExchangeRateImpl($filter[2], $filter[1]);
    if ($rate != NULL) {
        $result = "{" . W3CreateSuccessfulResult(false) . "," .
                W3MakeString(w3ApiResultData) . ":" . $rate . "}";
    } else {
        $result = "{" . W3CreateFailedResult(false) . "}";
    }

    return $result;
}

 ?>