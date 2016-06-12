<?php

function EJCreateOptionListFromDB($table, $keyColumn, $valueColumn, $isSID = true) {
    global $w3UI;
    global $w3Lan;

    $list = "";
    $sql = "select " . $keyColumn . "," . $valueColumn . " from " . $table;
    EJReadTable($sql, function ($row) use ($keyColumn, $valueColumn, $isSID, &$w3Lan, &$list) {
        if ($isSID) {
            $list .= "<option value='" .
                  $row[$keyColumn] . "'>" .
                  $w3Lan[W3GetLanguage()][$row[$valueColumn]] .
                  "</option>";
        } else {
            $list .= "<option value='" . $row[$keyColumn] . "'>" . $row[$valueColumn] . "</option>";
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

function EJCreateBillSceneCombo() {
    return EJCreateOptionListFromDB("billscene", "ID", "SID");
}

function EJCreatePaymentmodeCombo() {
    return EJCreateOptionListFromDB("paymentmode", "ID", "SID");
}

function EJCreateCurrencyCombo() {
    return EJCreateOptionListFromDB("currency", "ID", "SID");
}

function EJCreateOwnerCombo() {
    return EJCreateOptionListFromDB("person", "ID", "Name", false);
}

 ?>