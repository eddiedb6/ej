<?php

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
    $isDateCurrencyRecorded = false;
    EJReadTable($sql, function ($row) use (&$rate) {
        if (sizeof($row) > 0) {
            $rate = $row["rate"];
            $isDateCurrencyRecorded = true;
        }
    });

    if ($rate == NULL) {
        W3LogWarning("Exchange rate not found for (" . $date . ", " . $currency . ")");
        if (!$isDateCurrencyRecorded) {
            # Insert date and currency, and the rate will be updated by other script automatically later
            EJInsertExchangeRate($date, $currency);
        }
    }

    return $rate;
}

function EJGetExchangeRateString($date, $currency) {
    $rate = "100.0";
    # 1 - CNY
    if ($currency != "1") {
        $rate = EJGetExchangeRateImpl($date, $currency);
        if ($rate == NULL) {
            $rate = "0";
        }
    }

    return $rate;
}

function EJSumCurrency($sql) {
    $finalAmount = 0.0;
    EJReadTable($sql, function ($row) use (&$finalAmount) {
        $amount = floatval($row["amount"]);
        $date = explode(" ", $row["datetime"])[0];
        $currencyID = $row["currency"];

        $rate = floatval(EJGetExchangeRateString($date, $currencyID));
        $amount *= $rate / 100;

        $finalAmount += $amount;
    });

    return $finalAmount;
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
    # Separate to 3 everage
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

 ?>
