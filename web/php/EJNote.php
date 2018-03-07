<?php

function EJCreateNoteUIFromTag($idTag) {
    $uiNoteListPanelDef = array (
        w3PropType => w3TypePanel,
        w3PropID => "uidNoteListPanel" . $idTag,
        w3PropCSS => array (
            "padding-right" => "5px",
            "float" => "left",
            "border-right" => "1px solid"
        ),
        w3PropSubUI => array ()
    );
    
    $sql = "select ID, Title, Modified from note where Tag='" . $idTag ."' order by Modified desc";
    EJReadTable($sql, function ($row) use ($idTag, &$uiNoteListPanelDef) {
        $uiLink = array (
            w3PropType => w3TypeLink,
            w3PropString => $row["Title"],
            w3PropEvent => array (
                w3EventClick => array (
                    "EJOnNoteClicked(" . $idTag . "," . $row["ID"] . ")"
                )
            )
        );
        $uiLinkPanel = array (
            w3PropType => w3TypePanel,
            w3PropSubUI => array ($uiLink)
        );

        array_push($uiNoteListPanelDef[w3PropSubUI], $uiLinkPanel);
    });

    $uiNoteContentPanelDef = array (
        w3PropType => w3TypePanel,
        w3PropID => "uidNoteContentPanel" . $idTag,
        w3PropCSS => array (
            "padding-left" => "5px",
            "float" => "left"
        ),
        w3PropSubUI => array (
            array (
                w3PropType => w3TypePanel,
                w3PropID => "uidNoteContentTitle" . $idTag,
                w3PropCSS => array (
                    "text-align" => "center"
                ),
                w3PropSubUI => array (
                )
            ),
            array (
                w3PropType => w3TypePanel,
                w3PropID => "uidNoteContentBody" . $idTag,
                w3PropSubUI => array (
                )
            )
        )
    );

    return array ($uiNoteListPanelDef, $uiNoteContentPanelDef);
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
            w3PropID => $uid . "ContentPanel" . $row["ID"],
            w3PropCSS => array (
                "padding-top" => "5px",
            ),
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
