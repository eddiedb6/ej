<?php

function EJCreateNoteUIFromTag($tag) {
    $uiListDef = array (
        w3PropType => w3TypeTable,
        w3PropSubUI => array (
            array ()
        )
    );
    
    $sql = "select ID, Title, Modified from note where Tag='" . $tag ."' order by Modified desc" ;
    EJReadTable($sql, function ($row) use (&$uiListDef) {
        $uiLink = array (
            w3PropType => w3TypeLink,
            w3PropString => $row["Title"],
            w3PropEvent => array (
                w3EventClick => array (
                    "EJOnNoteClicked('" . $row["ID"] . "')"
                )
            )
        );
        array_push($uiListDef[w3PropSubUI], array ($uiLink));
    });

    $uiPanelDef = array (
        w3PropType => w3TypePanel,
        w3PropID => "uidNoteDisplayPanel" . strval($tag),
        w3PropSubUI => array (
            "uidButtonBack"
        )
    );

    return array($uiListDef, $uiPanelDef);
}

function EJCreateNoteTab() {
    $uid = "uidNoteTab";
    $uiDef = array (
        w3PropType => w3TypeTab,
        w3PropCSS => array (
            "border-style" => "solid",
            "border-width" => "1px",
            "background-color" => "white"
        ),
        w3PropSubUI => array ()
    );
    
    $sql = "select ID, SID from notetag";
    EJReadTable($sql, function ($row) use (&$uiDef, $uid) {
        $uiLabel = array (
            w3PropType => w3TypeLabel,
            w3PropID => $uid . "HeaderLabel" . $row["ID"],
            w3PropClass => "cidLRPadding",
            w3PropString => $row["SID"]
        );

        $uiPanel = array (
            w3PropType => w3TypePanel,
            w3PropID => $uid . "Panel" . $row["ID"],
            w3PropSubUI => EJCreateNoteUIFromTag($row["ID"])
        );

        array_push($uiDef[w3PropSubUI], array ($uiLabel, $uiPanel));
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
