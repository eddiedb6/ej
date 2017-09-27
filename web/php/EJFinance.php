<?php

function EJGetBill(&$filter) {
    if (!isset($filter) or sizeof($filter) != 3) {
        W3LogError("Get bill filter is not correct: " . var_dump($filter));
        return W3CreateFailedResult();
    }

    $sql = "select " .
         "bill.Datetime as datetime, bill.Amount as amount, bill.Note as note," .
         "person.Name as owner," .
         "currency.SID as currency," .
         "currency.ID as currencyID," .
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
            if ($value[w3ApiDataValue] == "amount") {
                $resultForColumn .= "|" . $row["currencyID"] . "|" . $row["datetime"];
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

function EJSumCurrency($sql) {
    $finalAmount = 0.0;
    EJReadTable($sql, function ($row) use (&$finalAmount) {
        $amount = floatval($row["amount"]);
        $date = explode(" ", $row["datetime"])[0];
        $currencyID = $row["currency"];

        if ($currencyID != "1") {
            $rate = EJGetExchangeRateImpl($date, $currencyID);
            if ($rate != NULL) {
                $amount = floatval($rate) * $amount;
            } else {
                // Do not calc this item if could not get exchange rate
                $amount = 0.0;
            }
        }

        $finalAmount += $amount;
    });

    return $finalAmount;
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
         "income.Datetime as datetime, income.Amount as amount, income.Note as note," .
         "person.Name as owner," .
         "currency.SID as currency," .
         "currency.ID as currencyID," .
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
                $resultForColumn .= "|" . $row["currencyID"] . "|" . $row["datetime"];
            }
            $result .= W3MakeString($value[w3ApiDataValue]) . ":" . W3MakeString($resultForColumn) . ",";
        }
        $result = rtrim($result, ",") . "},";
    });
    $result = rtrim($result, ",") . "]}";
    
    return $result;
}

function EJCalculatePercentageReport($table, $column, $year, $month, &$reports) {
    $nextYear = $year;
    $nextMonth = $month + 1;
    if ($nextMonth == 13) {
        $nextMonth = 1;
        $nextYear = $year + 1;
    }

    $sqlID = "select ID from " . $table . " order by ID asc";
    $sqlBill = "select bill.Amount as amount, bill.Datetime as datetime, bill.Currency as currency from bill where " .
             "bill.Datetime < " . W3MakeDateString($nextYear, $nextMonth, 1, true) .
             " and " .
             "bill.Datetime >= " . W3MakeDateString($year, $month, 1, true);
    $sqlBillYear = "select bill.Amount as amount, bill.Datetime as datetime, bill.Currency as currency from bill where " .
             "bill.Datetime < " . W3MakeDateString($nextYear, $nextMonth, 1, true) .
             " and " .
             "bill.Datetime >= " . W3MakeDateString($year, 1, 1, true);
    $amount = array();
    $amountYear = array();
    EJReadTable($sqlID, function ($row) use ($column, $sqlBill, $sqlBillYear, &$amount, &$amountYear) {
        $amountBill = EJSumCurrency($sqlBill . " and bill." . $column . " = " . $row["ID"]);
        array_push($amount, $amountBill);

        $amountBillYear = EJSumCurrency($sqlBillYear . " and bill." . $column . " = " . $row["ID"]);
        array_push($amountYear, $amountBillYear);
    });
    $totalAmount = array_sum($amount);
    $percentageStr = "";
    foreach ($amount as $value) {
        if ($totalAmount <= 0) {
            $percentageStr .= "0_";
        } else {
            $percentageStr .= strval(intval(($value / $totalAmount) * 10000)) . "_";
        }
    }
    $percentageStr = trim($percentageStr, "_");
    $totalAmountYear = array_sum($amountYear);
    $percentageStrYear = "";
    foreach ($amountYear as $value) {
        if ($totalAmountYear <= 0) {
            $percentageStrYear .= "0_";
        } else {
            $percentageStrYear .= strval(intval(($value / $totalAmountYear) * 10000)) . "_";
        }
    }
    $percentageStrYear = trim($percentageStrYear, "_");
    $reports["percentage"] = $percentageStr;
    $reports["percentageyear"] = $percentageStrYear;
}

function EJCalculateDebtReport($year, $month, &$reports, $isLastMonth = true) {
    $preYear = $year;
    $preMonth = $month - 1;
    if ($preMonth == 0) {
        $preMonth = 12;
        $preYear = $year - 1;
    }

    $nextYear = $year;
    $nextMonth = $month + 1;
    if ($nextMonth == 13) {
        $nextMonth = 1;
        $nextYear = $year + 1;
    }

    # debt of month
    $sql = "select sum(debt.Amount) from debt where " .
         "debt.Start < " . W3MakeDateString($nextYear, $nextMonth, 1, true) .
         " and " .
         "debt.End >= " . W3MakeDateString($year, $month, 1, true);
    $totalMonthDebt = 0.0;
    EJReadTable($sql, function ($row) use (&$totalMonthDebt) {
        $totalMonthDebt = floatval($row["sum(debt.Amount)"]); # [ED] PENDING: Need to consider balance of debt
    });

    if ($isLastMonth) {
        $reports["debt"] = $totalMonthDebt;
        $reports["debtyear"] = 0.0;
    }
    $reports["debtyear"] += $totalMonthDebt;
    
    if ($preMonth != 12) {
        EJCalculateDebtReport($preYear, $preMonth, $reports, false);
    }
}
    
function EJCalculateFinanceReport($year, $month, &$reports) {
    $preYear = $year;
    $preMonth = $month - 1;
    if ($preMonth == 0) {
        $preMonth = 12;
        $preYear = $year - 1;
    }

    $nextYear = $year;
    $nextMonth = $month + 1;
    if ($nextMonth == 13) {
        $nextMonth = 1;
        $nextYear = $year + 1;
    }

    # income of month
    $sql = "select income.Amount as amount, income.Datetime as datetime, income.Currency as currency from income where " .
         "income.Datetime >= " . W3MakeDateString($preYear, $preMonth, 1, true) .
         " and " .
         "income.Datetime < " . W3MakeDateString($year, $month, 1, true) .
         " and " .
         "income.PID in (select person.ID from person where person.FID=1)"; # [ED] PENDING: Handle FID
    $totalMonthIncome = EJSumCurrency($sql);

    # income of year
    $sql = "select income.Amount as amount, income.Datetime as datetime, income.Currency as currency from income where " .
         "income.Datetime >= " . W3MakeDateString($year - 1, 12, 1, true) .
         " and " .
         "income.Datetime < " . W3MakeDateString($year, $month, 1, true) .
         " and " .
         "income.PID in (select person.ID from person where person.FID=1)"; # [ED] PENDING: Handle FID
    $totalYearIncome = EJSumCurrency($sql);

    # consume of month
    $sql = "select bill.Amount as amount, bill.Datetime as datetime, bill.Currency as currency from bill where " .
         "bill.Datetime < " . W3MakeDateString($nextYear, $nextMonth, 1, true) .
         " and " .
         "bill.Datetime >= " . W3MakeDateString($year, $month, 1, true);
    $totalMonthConsume = EJSumCurrency($sql);

    # consume of year
    $sql = "select bill.Amount as amount, bill.Datetime as datetime, bill.Currency as currency from bill where " .
         "bill.Datetime < " . W3MakeDateString($nextYear, $nextMonth, 1, true) .
         " and " .
         "bill.Datetime >= " . W3MakeDateString($year, 1, 1, true);
    $totalYearConsume = EJSumCurrency($sql);

    # debt
    EJCalculateDebtReport($year, $month, $reports);
    $totalMonthDebt = $reports["debt"];
    $totalYearDebt = $reports["debtyear"];
    
    # deposit
    $totalMonthDeposit = $totalMonthIncome / 3;
    $totalYearDeposit = $totalYearIncome / 3;
    
    # balance
    $totalMonthBalance = $totalMonthIncome - $totalMonthDeposit - $totalMonthDebt - $totalMonthConsume;
    $totalYearBalance = $totalYearIncome - $totalYearDeposit - $totalYearDebt - $totalYearConsume;

    $reports["income"] = $totalMonthIncome;
    $reports["incomeyear"] = $totalYearIncome;
    $reports["deposit"] = $totalMonthDeposit;
    $reports["deposityear"] = $totalYearDeposit;
    $reports["consume"] = $totalMonthConsume;
    $reports["consumeyear"] = $totalYearConsume;
    $reports["balance"] = $totalMonthBalance;
    $reports["balanceyear"] = $totalYearBalance;

    # category
    EJCalculatePercentageReport("billcategory", "Category", $year, $month, $reports);
    $reports["category"] = $reports["percentage"];
    $reports["categoryyear"] = $reports["percentageyear"];

    # paymentmode
    EJCalculatePercentageReport("paymentmode", "PaymentMode", $year, $month, $reports);
    $reports["paymentmode"] = $reports["percentage"];
    $reports["paymentmodeyear"] = $reports["percentageyear"];
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

function EJUpdateExchangeRate($date, $currency) {
    //$url = "http://download.finance.yahoo.com/d/quotes.csv?e=.csv&f=sl1d1t1&s=EURCNY=x";
    $ctx = stream_context_create(array(
        "http" => array(
            "timeout" => 5,
            "proxy" => "q379741:mju7mko0@160.48.211.81:8080",
            //"proxy" => "160.48.235.10:8080",
            "result_fulluri" => True)
    ));
    //$result = file_get_contents($url, False, $ctx);
    $result = NULL;
    return $result;
}

function EJGetExchangeRateImpl($date, $currency) {
    $sql = "select " .
         "exchangerate.Rate as rate" .
         " from " .
         "exchangerate" .
         " where " .
         "exchangerate.Datetime = '" . $date . "'" .
         " and " .
         "exchangerate.Currency = " . $currency;
    
    $rate = NULL;
    EJReadTable($sql, function ($row) use (&$rate) {
        if (sizeof($row) > 0) {
            $rate = $row["rate"];
        }
    });

    if ($rate == NULL) {
        // Exchange rate is not in db, need to get from internet now
        $rate = EJUpdateExchangeRate($date, $currency);
    }

    return $rate;
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