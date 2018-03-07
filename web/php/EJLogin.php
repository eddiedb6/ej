<?php

function EJLogin(&$credential) {
    if (!EJIsAPIParamValid($credential, "aidLogin")) {
        return W3CreateFailedResult();
    }

    $username = $credential[W3GetAPIParamIndex("aidLogin", "username") + 1];
    $password = $credential[W3GetAPIParamIndex("aidLogin", "password") + 1];

    $isLogin = false;
    $sql = "select " .
         "authentication.Authentication as authentication" .
         " from " .
         "authentication, person" .
         " where " .
         "authentication.PID=person.ID" .
         " and " .
         "person.Name=" . W3MakeString($username, true) . ";";
    EJReadTable($sql, function($row) use (&$isLogin, $password) {
        if ($row["authentication"] == $password) {
            $isLogin = true;
        }
    });

    if (!$isLogin) {
        return W3CreateFailedResult();
    }

    unset($_SESSION[w3Session]);
    $session = EJGenerateSession();
    $_SESSION[w3Session] = $session;
    
    $apiDef = W3GetAPIDef("aidLogin");
    $result = "{" . W3CreateSuccessfulResult(false) . "," . W3MakeString(w3ApiResultData) . ":{";
    $result .= W3MakeString($apiDef[w3ApiResult][w3ApiResultData][0][w3ApiDataValue]) . ":";
    $result .= W3MakeString($session) . "}}";

    return $result;
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