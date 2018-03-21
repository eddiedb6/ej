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

 ?>
