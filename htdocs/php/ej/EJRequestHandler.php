<?php

function EJHandleRequest() {
    $request = $_SERVER["REQUEST_URI"];
    $parameters = "";
    if (W3IsRequest_page($request)) {
        require "W3Main.html";
        return true;
    } else if (W3IsRequest_bill($request, $parameters)) {
        echo EJGetBill($parameters);
        return true;
    } else if (W3IsRequest_addbill($request, $parameters)) {
        echo EJAddBill($parameters);
        return true;
    } else if (W3IsRequest_debt($request, $parameters)) {
        echo EJGetDebt($parameters);
        return true;
    } else if (W3IsRequest_adddebt($request, $parameters)) {
        echo EJAddDebt($parameters);
        return true;
    } else if (W3IsRequest_income($request, $parameters)) {
        echo EJGetIncome($parameters);
        return true;
    } else if (W3IsRequest_addincome($request, $parameters)) {
        echo EJAddIncome($parameters);
        return true;
    } else if (W3IsRequest_financereport($request, $parameters)) {
        echo EJGetFinanceReport($parameters);
        return true;
    } else if (W3IsRequest_financeevent($request, $parameters)) {
        echo EJGetFinanceEvent($parameters);
        return true;
    } else if (W3IsRequest_addfinanceevent($request, $parameters)) {
        echo EJAddFinanceEvent($parameters);
        return true;
    } else {
        W3LogError("Request could not be handled: " . $request);
    }

    return false;
}
    
 ?>
