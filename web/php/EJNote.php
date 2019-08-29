<?php

function EJAddNote(&$noteParams) {
    $aid = "aidAddNote";
    return EJExecuteWithAuthenticatedFamily($aid, $noteParams, function ($fid, $aid, &$noteParams) {
        $postParams = "";
        if (W3GetAPIPostParams($aid, $postParams)) {
            if (EJInsertNote($noteParams, $postParams, $fid)) {
                return W3CreateSuccessfulResult();
            }
        }

        return W3CreateFailedResult();
    });
}

function EJGeneratePDF(&$noteRawData) {
    shell_exec("./tmp/clean.sh");

    $note = $noteRawData["note"];
    $noteDecode = W3Decode($note);
    $noteID = $noteRawData["id"];
    $noteTxtName = "tmp/" . $noteID . ".tex";
    $noteTxt = fopen($noteTxtName, "w");
    if ($noteTxt == FALSE) {
        W3LogError("Open tex file failed");
        return;
    }

    fwrite($noteTxt, $noteDecode);
    fclose($noteTxt);

    $result = shell_exec("./tmp/pdfgen.sh " . $noteTxtName);
}

function EJGetNote(&$noteParams) {
    $aid = "aidNote";
    return EJExecuteWithAuthenticatedFamily($aid, $noteParams, function ($fid, $aid, &$noteParams) {
        $paramOffset = 1; # The first one is alway whole string from reg match
        $id = $noteParams[W3GetAPIParamIndex($aid, "id") + $paramOffset];

        $sql = "select " .
             "note.ID as id, note.Title as title, note.Tag as tag, note.Note as note, note.Type as type" .
             " from " .
             "note" .
             " where " .
             "note.ID = " . $id .
             " and " .
             "note.FID = " . $fid;

        $result = "{" . W3CreateSuccessfulResult(false) . "," . W3MakeString(w3ApiResultData) . ":{";
        EJReadTable($sql, function ($row) use (&$result, $aid) {
            $pdfType = "2";
            if ($row["type"] == $pdfType) {
                EJGeneratePDF($row);
            }

            $apiDef = W3GetAPIDef($aid);
            $columns = $apiDef[w3ApiResult][w3ApiResultData];

            foreach ($columns as $value) {
                $resultForColumn = $row[$value[w3ApiDataValue]];
                $result .= W3MakeString($value[w3ApiDataValue]) . ":" . W3MakeString($resultForColumn) . ",";
            }
        });
        $result = rtrim($result, ",") . "}}";

        return $result;
    });
}

function EJGetNoteTitle(&$noteParams) {
    $aid = "aidNoteTitle";
    return EJExecuteWithAuthenticatedFamily($aid, $noteParams, function ($fid, $aid, &$noteParams) {
        $paramOffset = 1; # The first one is alway whole string from reg match
        $idTag = $noteParams[W3GetAPIParamIndex($aid, "tag") + $paramOffset];

        $sql = "select " .
             "note.Title as title, note.ID as id" .
             " from " .
             "note" .
             " where " .
             "note.FID = " . $fid .
             " and " .
             "note.Tag = " . $idTag .
             " order by note.Modified desc";

        return EJReadMultiResultFromTable($aid, $sql);
    });
}

function EJModifyNote(&$noteParams) {
    $aid = "aidModifyNote";

    return EJExecuteWithAuthenticatedFamily($aid, $noteParams, function ($fid, $aid, &$noteParams) {
        $postParams = "";
        if (W3GetAPIPostParams($aid, $postParams)) {
            if (EJUpdateNote($noteParams, $postParams, $fid)) {
                return W3CreateSuccessfulResult();
            }
        }

        return W3CreateFailedResult();
    });
}

 ?>
