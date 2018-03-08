<?php

function EJAddNote() {
}

function EJGetNote(&$filter) {
    if (!EJIsAPIParamValid($filter, "aidNote")) {
        return W3CreateFailedResult();
    }

    $session = $filter[W3GetAPIParamIndex("aidNote", "session") + 1];
    $id = $filter[W3GetAPIParamIndex("aidNote", "id") + 1];

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

function EJGetNoteTitle(&$filter) {
    if (!EJIsAPIParamValid($filter, "aidNoteTitle")) {
        return W3CreateFailedResult();
    }

    $session = $filter[W3GetAPIParamIndex("aidNoteTitle", "session") + 1];
    $idTag = $filter[W3GetAPIParamIndex("aidNoteTitle", "tag") + 1];

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

function EJUpdateNote() {
}

 ?>
