<?php

function EJAddNote(&$noteParams) {
    $aid = "aidAddNote";
    if (EJIsAPIParamValid($noteParams, $aid)) {
        $paramOffset = 1; # The first one is alway whole string from reg match
        $session = $noteParams[W3GetAPIParamIndex($aid, "session") + $paramOffset];
        if (!EJIsLogin($session)) {
            return W3CreateAuthenticationResult();
        }

        $postParams = "";
        if (W3GetAPIPostParams($aid, $postParams)) {
            if (EJInsertNote($noteParams, $postParams)) {
                return W3CreateSuccessfulResult();
            }
        }
    }

    return W3CreateFailedResult();    
}

function EJGetNote(&$noteParams) {
    if (!EJIsAPIParamValid($noteParams, "aidNote")) {
        return W3CreateFailedResult();
    }

    $paramOffset = 1; # The first one is alway whole string from reg match
    $session = $noteParams[W3GetAPIParamIndex("aidNote", "session") + $paramOffset];
    $id = $noteParams[W3GetAPIParamIndex("aidNote", "id") + $paramOffset];

    if (!EJIsLogin($session)) {
        return W3CreateAuthenticationResult();
    }

    $sql = "select " .
         "note.Title as title, note.Tag as tag, note.Note as note" .
         " from " .
         "note" .
         " where " .
         "note.ID = " . $id;
    $result = "{" . W3CreateSuccessfulResult(false) . "," . W3MakeString(w3ApiResultData) . ":{";
    EJReadTable($sql, function ($row) use (&$result) {
        $apiDef = W3GetAPIDef("aidNote");
        $columns = $apiDef[w3ApiResult][w3ApiResultData];
        foreach ($columns as $value) {
            $resultForColumn = $row[$value[w3ApiDataValue]];
            $result .= W3MakeString($value[w3ApiDataValue]) . ":" . W3MakeString($resultForColumn) . ",";
        }
    });
    $result = rtrim($result, ",") . "}}";

    return $result;
}

function EJGetNoteTitle(&$noteParams) {
    if (!EJIsAPIParamValid($noteParams, "aidNoteTitle")) {
        return W3CreateFailedResult();
    }
    
    $paramOffset = 1; # The first one is alway whole string from reg match
    $session = $noteParams[W3GetAPIParamIndex("aidNoteTitle", "session") + $paramOffset];
    $idTag = $noteParams[W3GetAPIParamIndex("aidNoteTitle", "tag") + $paramOffset];

    if (!EJIsLogin($session)) {
        return W3CreateAuthenticationResult();
    }

    $sql = "select " .
         "note.Title as title, note.ID as id" .
         " from " .
         "note" .
         " where " .
         "note.Tag = " . $idTag .
         " order by note.Modified desc";
    $result = "{" . W3CreateSuccessfulResult(false) . "," . W3MakeString(w3ApiResultData) . ":[";
    EJReadTable($sql, function ($row) use (&$result) {
        $apiDef = W3GetAPIDef("aidNoteTitle");
        $columns = $apiDef[w3ApiResult][w3ApiResultData];
        $result .= "{";
        foreach ($columns as $value) {
            $resultForColumn = $row[$value[w3ApiDataValue]];
            $result .=  W3MakeString($value[w3ApiDataValue]) . ":" . W3MakeString($resultForColumn) . ",";
        }
        $result = rtrim($result, ",") . "},";
    });
    $result = rtrim($result, ",") . "]}";

    return $result;
}

function EJModifyNote(&$noteParams) {
    $aid = "aidModifyNote";
    
    if (EJIsAPIParamValid($noteParams, $aid)) {
        $paramOffset = 1; # The first one is alway whole string from reg match
        $session = $noteParams[W3GetAPIParamIndex($aid, "session") + $paramOffset];
        if (!EJIsLogin($session)) {
            return W3CreateAuthenticationResult();
        }

        $postParams = "";
        if (W3GetAPIPostParams($aid, $postParams)) {
            if (EJUpdateNote($noteParams, $postParams)) {
                return W3CreateSuccessfulResult();
            }
        }
    }

    return W3CreateFailedResult();    
}

 ?>
