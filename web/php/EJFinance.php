<?php

function EJGetBill(&$billParams) {
    $aid = "aidBill";
    return EJExecuteWithAuthenticatedFamily($aid, $billParams, function ($fid, $aid, &$billParams) {
        $paramOffset = 1; # The first one is the whole string from reg match
        $startDate = $billParams[W3GetAPIParamIndex($aid, "from") + $paramOffset];
        $endDate = $billParams[W3GetAPIParamIndex($aid, "to") + $paramOffset];

        $sql = "select " .
             "bill.Datetime as datetime, bill.Amount as amount, bill.Currency as currencyID, bill.Note as note," .
             "person.Name as owner," .
             "currency.SID as currency," .
             "paymentmode.SID as paymentmode," .
             "billcategory.SID as category" .
             " from " .
             "bill, currency, paymentmode, billcategory, person" .
             " where " .
             "bill.Datetime >= '" . $startDate . "' and bill.Datetime <= '" . $endDate . "'" .
             " and " .
             "bill.PID = person.ID" .
             " and " .
             "bill.Currency = currency.ID" .
             " and " .
             "bill.PaymentMode = paymentmode.ID" .
             " and " .
             "bill.Category = billcategory.ID" .
             " and " .
             "bill.PID in (select person.ID from person where person.FID=" . $fid . ")" .
             " order by bill.Datetime asc";
        $result = "{" . W3CreateSuccessfulResult(false) . "," . W3MakeString(w3ApiResultData) . ":[";
        EJReadTable($sql, function ($row) use (&$result, $aid) {
            $apiDef = W3GetAPIDef($aid);
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
    });
}

function EJGetDebt(&$debtParams) {
    $aid = "aidDebt";
    return EJExecuteWithAuthenticatedFamily($aid, $debtParams, function ($fid, $aid, &$debtParams) {
        $paramOffset = 1; # The first one is the whole string from reg match
        $startDate = $debtParams[W3GetAPIParamIndex($aid, "from") + $paramOffset];
        $endDate = $debtParams[W3GetAPIParamIndex($aid, "to") + $paramOffset];

        $sql = "select " .
             "debt.Start as start, debt.End as end, " .
             "debt.Amount as amount, debt.Balance as balance, debt.Note as note" .
             " from " .
             "debt" .
             " where FID=" . $fid . " and " .
             "(debt.Start <= '" . $endDate . "' and debt.End >= '" . $startDate . "')" .
             " order by debt.Start asc";
        return EJReadMultiResultFromTable($aid, $sql);
    });
}

function EJGetFinanceEvent(&$eventParams) {
    $aid = "aidFinanceEvent";
    return EJExecuteWithAuthenticatedFamily($aid, $eventParams, function ($fid, $aid, &$eventParams) {
        $paramOffset = 1; # The first one is the whole string from reg match
        $eventName = EJDecodeURLString($eventParams[W3GetAPIParamIndex($aid, "name") + $paramOffset]);

        $sql = "select " .
             "financeevent.ID as id, " .
             "financeevent.Name as name, " .
             "financeevent.Budget as budget, " .
             "financeevent.Note as note " .
             "from financeevent " .
             "where FID=" . $fid . "";
        if ($eventName != "") {
            $sql .= " and financeevent.Name like " . W3MakeString("%" . $eventName . "%", true);
        }
        $sql .= " order by financeevent.Name asc";
        $result = "{" . W3CreateSuccessfulResult(false) . "," . W3MakeString(w3ApiResultData) . ":[";
        EJReadTable($sql, function ($row) use (&$result, $aid) {
            $apiDef = W3GetAPIDef($aid);
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
    });
}

function EJGetIncome(&$incomeParams) {
    $aid = "aidIncome";
    return EJExecuteWithAuthenticatedFamily($aid, $incomeParams, function ($fid, $aid, &$incomeParams) {
        $paramOffset = 1; # The first one is the whole string from reg match
        $startDate = $incomeParams[W3GetAPIParamIndex($aid, "from") + $paramOffset];
        $endDate = $incomeParams[W3GetAPIParamIndex($aid, "to") + $paramOffset];

        $sql = "select " .
             "income.Datetime as datetime, income.Amount as amount, income.Currency as currencyID, income.Note as note," .
             "person.Name as owner," .
             "currency.SID as currency," .
             "incomecategory.SID as category" .
             " from " .
             "income, currency, incomecategory, person" .
             " where " .
             "income.Datetime >= '" . $startDate . "' and income.Datetime <= '" . $endDate . "'" .
             " and " .
             "income.PID = person.ID" .
             " and " .
             "income.Currency = currency.ID" .
             " and " .
             "income.Category = incomecategory.ID" .
             " and " .
             "income.PID in (select person.ID from person where person.FID=" . $fid . ")" .
             " order by income.Datetime asc";
        $result = "{" . W3CreateSuccessfulResult(false) . "," . W3MakeString(w3ApiResultData) . ":[";
        EJReadTable($sql, function ($row) use (&$result, $aid) {
            $apiDef = W3GetAPIDef($aid);
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
    });
}

function EJGetFinanceReport(&$reportParams) {
    $aid = "aidFinanceReport";
    return EJExecuteWithAuthenticatedFamily($aid, $reportParams, function ($fid, $aid, &$reportParams) {
        $paramOffset = 1; # The first one is the whole string from reg match
        $reportMonth = $reportParams[W3GetAPIParamIndex($aid, "month") + $paramOffset];

        $time = explode("-", $reportMonth);
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
    
        EJCalculateFinanceReport($year, $month, $report, $fid);
    
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
    });
}

function EJAddBill(&$parameters) {
    $aid = "aidAddBill";
    return EJExecuteWithAuthentication($aid, $parameters, function ($session, $aid, &$parameters) {
        if (EJInsertBill($parameters)) {
            return W3CreateSuccessfulResult();
        }

        return W3CreateFailedResult();
    });
}

function EJAddDebt(&$parameters) {
    $aid = "aidAddDebt";
    return EJExecuteWithAuthenticatedFamily($aid, $parameters, function ($fid, $aid, &$parameters) {
        if (EJInsertDebt($parameters, $fid)) {
            return W3CreateSuccessfulResult();
        }

        return W3CreateFailedResult();
    });
}

function EJAddFinanceEvent(&$parameters) {
    $aid = "aidAddFinanceEvent";
    return EJExecuteWithAuthenticatedFamily($aid, $parameters, function ($fid, $aid, &$parameters) {
        if (EJInsertFinanceEvent($parameters, $fid)) {
            return W3CreateSuccessfulResult();
        }

        return W3CreateFailedResult();
    });
}

function EJAddIncome(&$parameters) {
    $aid = "aidAddIncome";
    return EJExecuteWithAuthentication($aid, $parameters, function ($session, $aid, &$parameters) {
        if (EJInsertIncome($parameters)) {
            return W3CreateSuccessfulResult();
        }

        return W3CreateFailedResult();
    });
}

 ?>
