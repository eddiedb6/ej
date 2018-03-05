<?php

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
    
    $sql = "select SID from notetag";
    EJReadTable($sql, function ($row) use (&$uiDef, $uid) {
        $uiLabel = array(
            w3PropType => w3TypeLabel,
            w3PropClass => "cidLRPadding",
            w3PropString => $row["SID"]
        );

        $uiPanel = array (
            w3PropType => w3TypePanel,
            w3PropSubUI => array("uidDebugContent")
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
