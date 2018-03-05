<?php

function EJCreateNoteUIFromTag($tag) {
    $sql = "select Title, Note from note where Tag='" . $tag ."'";
    EJReadTable($sql, function ($row) use (&$uiDef, $uid) {
    });

    return array();
}

function EJCreateNoteTab() {
    $uid = "uidNoteTab";
    $uiDef = array(
        w3PropType => w3TypeTab,
        w3PropCSS => array (
            "border-style" => "solid",
            "border-width" => "1px",
            "background-color" => "white"
        ),
        w3PropSubUI => array()
    );
    
    $sql = "select ID, SID from notetag";
    EJReadTable($sql, function ($row) use (&$uiDef, $uid) {
        $uiLabel = array(
            w3PropType => w3TypeLabel,
            w3PropClass => "cidLRPadding",
            w3PropString => $row["SID"]
        );

        $uiPanel = array (
            w3PropType => w3TypePanel,
            w3PropSubUI => EJCreateNoteUIFromTag($row["ID"])
        );

        array_push($uiDef[w3PropSubUI], array($uiLabel, $uiPanel));
    });

    return W3CreateDynamicUI($uid, $uiDef);
}

function EJSetNote() {
}

function EJGetNote() {
}

function EJGetNoteTitle() {
}

 ?>
