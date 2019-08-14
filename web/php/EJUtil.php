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

function EJIsAPIAuthenticated($aid, &$params) {
    # The params is from reg check, so the first one is always the whole string be checked
    $session = $params[W3GetAPIParamIndex($aid, w3SessionKey) + 1];
    if (!EJIsLogin($session)) {
        return false;
    }

    return true;
}

function EJExecuteWithAuthentication($aid, &$params, $executor) {
    if (!EJIsAPIParamValid($params, $aid)) {
        return W3CreateFailedResult();
    }

    if (!EJIsAPIAuthenticated($aid, $params)) {
        return W3CreateAuthenticationResult();
    }

    return $executor($params);
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
