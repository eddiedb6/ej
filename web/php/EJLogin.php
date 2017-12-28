<?php

function EJLogin(&$credential) {
    if (!isset($credential) or sizeof($credential) != 3) {
        W3LogError("Get credential is not correct: " . var_dump($credential));
        return W3CreateFailedResult();
    }

    # [TODO] generate real session
    $session = $credential[1] . ":" . $credential[2];
    
    $apiDef = W3GetAPIDef("aidLogin");
    $result = "{" . W3CreateSuccessfulResult(false) . "," . W3MakeString(w3ApiResultData) . ":{";
    $result .= W3MakeString($apiDef[w3ApiResult][w3ApiResultData][0][w3ApiDataValue]) . ":";
    $result .= W3MakeString($session) . "}}";

    return $result;
}

 ?>