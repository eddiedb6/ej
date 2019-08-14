<?php

function EJAddNote(&$noteParams) {
    $aid = "aidAddNote";
    return EJExecuteWithAuthentication($aid, $noteParams, function () use ($aid, &$noteParams) {
        $postParams = "";
        if (W3GetAPIPostParams($aid, $postParams)) {
            if (EJInsertNote($noteParams, $postParams)) {
                return W3CreateSuccessfulResult();
            }
        }

        return W3CreateFailedResult();
    });
}

function EJGetNote(&$noteParams) {
    $aid = "aidNote";
    return EJExecuteWithAuthentication($aid, $noteParams, function () use ($aid, &$noteParams) {
        $paramOffset = 1; # The first one is alway whole string from reg match
        $id = $noteParams[W3GetAPIParamIndex($aid, "id") + $paramOffset];

        $sql = "select " .
             "note.Title as title, note.Tag as tag, note.Note as note" .
             " from " .
             "note" .
             " where " .
             "note.ID = " . $id;

        return EJReadResultFromTable($aid, $sql, false);
    });
}

function EJGetNoteTitle(&$noteParams) {
    $aid = "aidNoteTitle";
    return EJExecuteWithAuthentication($aid, $noteParams, function () use ($aid, &$noteParams) {
        $paramOffset = 1; # The first one is alway whole string from reg match
        $idTag = $noteParams[W3GetAPIParamIndex($aid, "tag") + $paramOffset];

        $sql = "select " .
             "note.Title as title, note.ID as id" .
             " from " .
             "note" .
             " where " .
             "note.Tag = " . $idTag .
             " order by note.Modified desc";

        return EJReadResultFromTable($aid, $sql, true);
    });
}

function EJModifyNote(&$noteParams) {
    $aid = "aidModifyNote";

    return EJExecuteWithAuthentication($aid, $noteParams, function () use ($aid, &$noteParams) {
        $postParams = "";
        if (W3GetAPIPostParams($aid, $postParams)) {
            if (EJUpdateNote($noteParams, $postParams)) {
                return W3CreateSuccessfulResult();
            }
        }

        return W3CreateFailedResult();
    });
}

 ?>
