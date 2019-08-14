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

function EJReadResultFromTable($aid, $sql, $isResultArray) {
    $result = "{" . W3CreateSuccessfulResult(false) . "," . W3MakeString(w3ApiResultData) . ($isResultArray ? ":[" : ":{");
    EJReadTable($sql, function ($row) use (&$result, $aid) {
        $apiDef = W3GetAPIDef($aid);
        $columns = $apiDef[w3ApiResult][w3ApiResultData];
        if ($isResultArray) {
            $result .= "{";
        }
        foreach ($columns as $value) {
            $resultForColumn = $row[$value[w3ApiDataValue]];
            $result .= W3MakeString($value[w3ApiDataValue]) . ":" . W3MakeString($resultForColumn) . ",";
        }
        if ($isResultArray) {
            $result = rtrim($result, ",") . "},";
        }
    });
    $result = rtrim($result, ",") . ($isResultArray ? "]}" : "}}");

    return $result;
}

 ?>
