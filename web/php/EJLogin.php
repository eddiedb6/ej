<?php

function EJLogin(&$credential) {
    if (!isset($credential) or sizeof($credential) != 3) {
        W3LogError("Get credential is not correct: " . var_dump($credential));
        return W3CreateFailedResult();
    }

    # [TODO] Edward
    $temp = $credential[1] . ":" . $credential[2];
    $result = "{" . W3CreateSuccessfulResult(false) . ", " . W3MakeString(w3ApiResultData) . ":{";
    $result = $result . W3MakeString("session") . ":" . W3MakeString($temp);
    $result = $result . "}}";

    return $result;
}

 ?>