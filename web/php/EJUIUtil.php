<?php

function EJCreateOptionListFromDB($table, $keyColumn, $valueColumn, $isSID = true) {
    $list = "";
    $sql = "select " . $keyColumn . "," . $valueColumn . " from " . $table;
    EJReadTable($sql, function ($row) use ($keyColumn, $valueColumn, $isSID, &$list) {
        if ($isSID) {
            $list .= "<option value='" .
                  $row[$keyColumn] . "'>" .
                  W3GetStringValue($row[$valueColumn]) .
                  "</option>";
        } else {
            $list .= "<option value='" .
                  $row[$keyColumn] . "'>" .
                  $row[$valueColumn] .
                  "</option>";
        }
    });
    
    return $list;
}

function EJCreateBillCategoryCombo() {
    return EJCreateOptionListFromDB("billcategory", "ID", "SID");
}

function EJCreateIncomeCategoryCombo() {
    return EJCreateOptionListFromDB("incomecategory", "ID", "SID");
}

function EJCreatePaymentModeCombo() {
    return EJCreateOptionListFromDB("paymentmode", "ID", "SID");
}

function EJCreateCurrencyCombo() {
    return EJCreateOptionListFromDB("currency", "ID", "SID");
}

function EJCreateOwnerCombo() {
    return EJCreateOptionListFromDB("person", "ID", "Name", false);
}

 ?>