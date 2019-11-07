<?php

function EJIsAPIParamValid(&$params, $aid) {
    $paramCount = W3GetAPIParamCount($aid);
    
    # The params is from reg check, so the first one is always the whole string be checked
    if (!isset($params) or sizeof($params) != $paramCount + 1) {
        W3LogError("API " . $aid . " parameters are not valid: " . var_dump($params));
        return false;
    }

    return true;
}

function EJIsAPIAuthenticated($aid, &$params, &$authResult) {
    # The params is from reg check, so the first one is always the whole string be checked
    $session = $params[W3GetAPIParamIndex($aid, w3SessionKey) + 1];
    if (!EJIsLogin($session)) {
        return false;
    }

    $authResult = $session;
    return true;
}

function EJIsAPIFamilyValid($session, &$familyID) {
    $familyID = EJGetLoginFamily($session);
    if ($familyID == null) {
        W3LogError("Failed to get family ID");
        return false;
    }

    return true;
}

function EJExecuteAPI($aid, &$params, $executor, $checkSession, $checkFamily) {

    if (!EJIsAPIParamValid($params, $aid)) {
        return W3CreateFailedResult();
    }

    if (!$checkSession) {
        return $executor($aid, $params);
    }

    $session = null;
    if (!EJIsAPIAuthenticated($aid, $params, $session)) {
        return W3CreateAuthenticationResult();
    }

    if (!$checkFamily) {
        return $executor($session, $aid, $params);
    }

    $familyID = null;
    if (!EJIsAPIFamilyValid($session, $familyID)) {
        return W3CreateFailedResult();
    }

    return $executor($familyID, $aid, $params);
}

function EJExecuteWithAuthentication($aid, &$params, $executor) {
    return EJExecuteAPI($aid, $params, $executor, true, false);
}

function EJExecuteWithAuthenticatedFamily($aid, &$params, $executor) {
    return EJExecuteAPI($aid, $params, $executor, true, true);
}

function EJDecodeURLString($str) {
    # Replace White Space
    return str_replace("%20", " ", $str);
}

 ?>
