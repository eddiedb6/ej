<?php

function EJGetJourney(&$journeyParams) {
    $aid = "aidJourney";
    return EJExecuteWithAuthentication($aid, $journeyParams, function () use ($aid, &$journeyParams) {
        // [TODO]
        
        return "";
    });
}

function EJAddJourney(&$parameters) {
    $aid = "aidAddJourney";
    return EJExecuteWithAuthentication($aid, $parameters, function () use ($aid, &$parameters) {
        $paramOffset = 1; # The first one is alway whole string from reg match
        $travelerStr = $parameters[W3GetAPIParamIndex($aid, "traveler") + $paramOffset];

        // [TODO] Handle travelers
        $travelers = explode(",", $travelerStr);
        
        if (EJInsertJourney($parameters)) {
            return W3CreateSuccessfulResult();
        }

        return W3CreateFailedResult();
    });
}

 ?>
