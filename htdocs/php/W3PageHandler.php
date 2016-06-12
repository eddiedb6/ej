<?php

function W3CreatePage() {
    #############################################
    # User function logic should be added below #
    #############################################

    echo W3CreateUI("uidBody");

    #############################################
    # User function logic should be added above #
    #############################################
}

function W3SelectPage() {
    #############################################
    # User function logic should be added below #
    #############################################

    global $w3UI;

    if (W3IsEmptyRequest()) {
        return W3CreateUI("uidPageFinance");
    } else {
        if (preg_match(W3CreateAPIReg("aidPage"), $_SERVER["REQUEST_URI"], $matches) and 
            array_key_exists($matches[1], $w3UI)) {
            return W3CreateUI($matches[1]);
        }
    }

    return W3CreateUI("uidPageError");

    #############################################
    # User function logic should be added above #
    #############################################
}

 ?>