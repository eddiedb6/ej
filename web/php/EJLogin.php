<?php

define('familyKey', 'family');

function EJLogin(&$credential) {
    if (!EJIsAPIParamValid($credential, "aidLogin")) {
        return W3CreateFailedResult();
    }

    $paramOffset = 1; # The first one is the whole match string from reg
    $username = $credential[W3GetAPIParamIndex("aidLogin", "username") + $paramOffset];
    $password = $credential[W3GetAPIParamIndex("aidLogin", "password") + $paramOffset];

    $isLogin = false;
    $familyID = -1;
    $sql = "select " .
         "authentication.Authentication as authentication, person.FID as " . familyKey .
         " from " .
         "authentication, person" .
         " where " .
         "authentication.PID=person.ID" .
         " and " .
         "person.Name=" . W3MakeString($username, true) . ";";
    EJReadTable($sql, function($row) use (&$isLogin, &$familyID, $password) {
        if ($row["authentication"] == $password) {
            $familyID = $row[familyKey];
            $isLogin = true;
        }
    });

    if (!$isLogin) {
        return W3CreateFailedResult();
    }

    unset($_SESSION[w3Session]);
    unset($_SESSION[familyKey]);
    $session = EJGenerateSession();
    $_SESSION[w3Session] = $session;
    $_SESSION[familyKey] = $familyID;

    $apiDef = W3GetAPIDef("aidLogin");
    $result = "{" . W3CreateSuccessfulResult(false) . "," . W3MakeString(w3ApiResultData) . ":{";
    $result .= W3MakeString($apiDef[w3ApiResult][w3ApiResultData][0][w3ApiDataValue]) . ":";
    $result .= W3MakeString($session) . "}}";

    return $result;
}

function EJGetLoginFamily($session) {
    if (EJIsLogin($session)) {
        return $_SESSION[familyKey];
    }

    return null;
}

function EJIsLogin($session) {
    if (array_key_exists(w3Session, $_SESSION) and $session == $_SESSION[w3Session]) {
        return true;
    }
    
    return false;
}

function EJGenerateSession() {
    $charArry = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
    $len = 32;

    $session = "";
    for ($i = $len; $i > 0; $i--) {
        $session .= $charArry[mt_rand(0, strlen($charArry) - 1)];
    }

    return $session;
}

 ?>
