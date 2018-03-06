<?php

function EJCreateNoteUIFromTag($idTag) {
    $uiNoteListPanelDef = array (
        w3PropType => w3TypePanel,
        w3PropID => "uidNoteListPanel" . $idTag,
        w3PropSubUI => array ()
    );
    
    $sql = "select ID, Title, Modified from note where Tag='" . $idTag ."' order by Modified desc";
    EJReadTable($sql, function ($row) use ($idTag, &$uiNoteListPanelDef) {
        $uiLink = array (
            w3PropType => w3TypeLink,
            w3PropString => $row["Title"],
            w3PropEvent => array (
                w3EventClick => array (
                    "EJOnNoteClicked('" . $idTag . "','" . $row["ID"] . "')"
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

    $uiTableDef = array (
        w3PropType => w3TypeTable,
        w3PropID => "uidNoteContentTable" . $idTag,
        w3PropSubUI => array (
            array (),
            array ($uiNoteListPanelDef, $uiNoteContentPanelDef)
        )
    );

    return array ($uiTableDef);
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
