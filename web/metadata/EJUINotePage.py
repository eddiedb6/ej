{
    "uidPageNote": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropSubUI: [
            "uidNotePanel",
            "uidNoteAddPanel",
            "uidNoteEditPanel"
        ]
    },

    # Note
    
    "uidNotePanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropSubUI: [
            "uidNoteTagPanel",
            "uidNoteDisplayPanel",
            "uidNoteOperationPanel"
        ]
    },

    # Note - Tag
    
    "uidNoteTagPanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropSubUI: [
            "uidNoteTagTable",
            "uidLine"
        ]
    },
    "uidNoteTagTable": {
        W3Const.w3PropType: W3Const.w3TypeTable,
        W3Const.w3PropSubUI: [
            [],
            ["uidNoteTagLabel", "uidNoteTag", "uidNoteGetButton"]
        ]
    },
    "uidNoteTagLabel": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropClass: "cidRightLabel",
        W3Const.w3PropString: "sidNoteTagLabel"
    },
    "uidNoteTag": {
        W3Const.w3PropType: W3Const.w3TypeCombobox,
        W3Const.w3PropFunc: {
            W3Const.w3FuncCreator: "EJCreateNoteTagCombo"
        }
    },
    "uidNoteGetButton": {
        W3Const.w3PropType: W3Const.w3TypeButton,
        W3Const.w3PropString: "sidGet",
        W3Const.w3PropTriggerApi: [
        {
            W3Const.w3ApiID: "aidNoteTitle",
            W3Const.w3ApiParams: [
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeUID,
                W3Const.w3ApiDataValue: "uidNoteTag"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeVar,
                W3Const.w3ApiDataValue: W3Const.w3Session
            }]                                
        }],
        W3Const.w3PropEvent: {
            W3Const.w3EventClick: [
                W3Const.w3PlaceHolder_1,
                "W3DisableUI('uidNoteEditButton')",
                "W3SetUIText('uidNoteContentBodyPanel', '')",
                "W3SetUIText('uidNoteContentTitleLabel', '')"
            ]
        }
    },

    # Note - Display
    
    "uidNoteDisplayPanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropSubUI: [
            "uidNoteListPanel",
            "uidNoteContentPanel"
        ]
    },
    "uidNoteListPanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropCSS: {
            "float": "left",
            "border-right": "1px solid"
        },
        W3Const.w3PropSubUI: [
            "uidNoteListLayout"
        ]
    },
    "uidNoteListLayout": {
        W3Const.w3PropType: W3Const.w3TypeTable,
        W3Const.w3PropSubUI: [
            [],
            ["uidNoteListLabel"],
            ["uidNoteListTable"]
        ]
    },
    "uidNoteListLabel": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropString: "sidNoteLabel",
        W3Const.w3PropCSS: {
            "padding-right": "5px",
            "float": "left"
        }
    },
    "uidNoteListTable": {
        W3Const.w3PropType: W3Const.w3TypeTable,
        W3Const.w3PropSubUI: [
            ["uidNoteListTableHeaderSelectMark", "uidNoteListTableHeaderID", "uidNoteListTableHeaderTitle"]
        ],
        W3Const.w3PropSinkApi: {
            W3Const.w3ApiID: "aidNoteTitle",
            W3Const.w3SinkRow: [
            {
                # Column 2 map to API result field "id"
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeNone,
                W3Const.w3ApiDataValue: ""
            },
            {
                # Column 2 map to API result field "id"
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeNum,
                W3Const.w3ApiDataValue: "id"
            },
            {
                # Column 3 map to API result field "title"
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
                W3Const.w3ApiDataValue: "title"
            }]
        }
    },
    "uidNoteListTableHeaderSelectMark": {
        W3Const.w3PropType: W3Const.w3TypeTableHeader,
        W3Const.w3PropSubUI: [
        ]
    },
    "uidNoteListTableHeaderID": {
        W3Const.w3PropType: W3Const.w3TypeTableHeader,
        W3Const.w3PropSubUI: [
        ],
        W3Const.w3PropFunc: {
            W3Const.w3FuncProcessor: [
                "EJHideNoteID(w3PlaceHolder_1)"
            ]
        }
    },
    "uidNoteListTableHeaderTitle": {
        W3Const.w3PropType: W3Const.w3TypeTableHeader,
        W3Const.w3PropSubUI: [
        ],
        W3Const.w3PropFunc: {
            W3Const.w3FuncProcessor: [
                "EJCreateNoteLink(w3PlaceHolder_1)"
            ]
        }
    },
    "uidNoteContentPanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropCSS: {
            "padding-left": "5px",
            "float": "left",
        },
        W3Const.w3PropSubUI: [
            "uidNoteContentTitlePanel",
            "uidNoteContentBodyPanel"
        ]
    },
    "uidNoteContentTitlePanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropCSS: {
            "text-align": "center"
        },
        W3Const.w3PropSubUI: [
            "uidNoteContentTitleLabel"
        ]
    },
    "uidNoteContentTitleLabel": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropCSS: {
            "font-weight": "bold"
        }
    },
    "uidNoteContentBodyPanel": {
        W3Const.w3PropType: W3Const.w3TypeDisplayPanel
    },
    
    # Note - Operation
    
    "uidNoteOperationPanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropSubUI: [
            "uidNoteAddButton",
            "uidNoteEditButton"
        ],
        W3Const.w3PropCSS: {
            "clear": "both",
            "padding-top": "5px",
            "float": "right"
        }
    },
    "uidNoteAddButton": {
        W3Const.w3PropType: W3Const.w3TypeButton,
        W3Const.w3PropString: "sidAdd",
        W3Const.w3PropEvent: {
            W3Const.w3EventClick: [
                "W3HideUI('uidNotePanel')",
                "W3DisplayUI('uidNoteAddPanel')"
            ]
        }
    },
    "uidNoteEditButton": {
        W3Const.w3PropType: W3Const.w3TypeButton,
        W3Const.w3PropString: "sidEdit",
        W3Const.w3PropAttr: {
            W3Const.w3AttrDisabled: "true"
        },
        W3Const.w3PropEvent: {
            W3Const.w3EventClick: [
                "EJEditNote()",
                "W3HideUI('uidNotePanel')",
                "W3DisplayUI('uidNoteEditPanel')"
            ]
        }
    },

    # Edit

    "uidNoteEditPanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropCSS: {
            "display": "none"
        },
        W3Const.w3PropSubUI: [
            "uidNoteEditID",
            "uidNoteEditor",
            "uidNoteEditOperationPanel"
        ]
    },
    "uidNoteEditID": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropCSS: {
            "display": "none"
        }
    },
    "uidNoteEditor": {
        W3Const.w3PropType: W3Const.w3TypeTextEditor,
        W3Const.w3PropAttr: {
            "rows": "64",
            "cols": "80"
        }
    },
    "uidNoteEditOperationPanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropSubUI: [
            "uidNoteEditSaveButton",
            "uidNoteEditCancelButton"
        ],
        W3Const.w3PropCSS: {
            "clear": "both",
            "padding-top": "5px",
            "float": "right"
        }
    },
    "uidNoteEditCancelButton": {
        W3Const.w3PropType: W3Const.w3TypeButton,
        W3Const.w3PropString: "sidCancel",
        W3Const.w3PropEvent: {
            W3Const.w3EventClick: [
                "W3HideUI('uidNoteEditPanel')",
                "W3DisplayUI('uidNotePanel')"
            ]
        }
    },
    "uidNoteEditSaveButton": {
        W3Const.w3PropType: W3Const.w3TypeButton,
        W3Const.w3PropString: "sidSave",
        W3Const.w3PropTriggerApi: [
        {
            W3Const.w3ApiID: "aidModifyNote",
            W3Const.w3ApiParams: [
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeUID,
                W3Const.w3ApiDataValue: "uidNoteEditID"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeVar,
                W3Const.w3ApiDataValue: W3Const.w3Session
            }],
            W3Const.w3ApiPost: [
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeUID,
                W3Const.w3ApiDataValue: "uidNoteEditor"
            }]
        }],
        W3Const.w3PropEvent: {
            W3Const.w3EventClick: [
                W3Const.w3PlaceHolder_1
            ]
        }
    },

    # Add
    
    "uidNoteAddPanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropSubUI: [
            "uidNoteAddTable",
            "uidNoteAddOperationPanel"
        ],
        W3Const.w3PropCSS: {
            "display": "none"
        }
    },
    "uidNoteAddOperationPanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropSubUI: [
            "uidNoteAddOperationTable"
        ]
    },
    "uidNoteAddOperationTable": {
        W3Const.w3PropType: W3Const.w3TypeTable,
        W3Const.w3PropSubUI: [
            [], # No header
            ["uidNoteAddSubmitButton", "uidNoteAddCancelButton"]
        ],
        W3Const.w3PropCSS: {
            "float": "right"
        }
    },
    "uidNoteAddCancelButton": {
        W3Const.w3PropType: W3Const.w3TypeButton,
        W3Const.w3PropString: "sidCancel",
        W3Const.w3PropEvent: {
            W3Const.w3EventClick: [
                "W3HideUI('uidNoteAddPanel')",
                "W3DisplayUI('uidNotePanel')"
            ]
        }
    },
    "uidNoteAddSubmitButton": {
        W3Const.w3PropType: W3Const.w3TypeButton,
        W3Const.w3PropString: "sidSubmit",
        W3Const.w3PropTriggerApi: [
        {
            W3Const.w3ApiID: "aidAddNote",
            W3Const.w3ApiParams: [
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeUID,
                W3Const.w3ApiDataValue: "uidNoteAddTitle"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeUID,
                W3Const.w3ApiDataValue: "uidNoteAddTag"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeVar,
                W3Const.w3ApiDataValue: W3Const.w3Session
            }],
            W3Const.w3ApiPost: [
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeUID,
                W3Const.w3ApiDataValue: "uidNoteAddNote"
            }]
        }],
        W3Const.w3PropEvent: {
            W3Const.w3EventClick: [
                W3Const.w3PlaceHolder_1
            ]
        }
    },
    "uidNoteAddTable": {
        W3Const.w3PropType: W3Const.w3TypeTable,
        W3Const.w3PropSubUI: [
            [], # No header
            ["uidNoteTitleLabel", "uidNoteAddTitle"],
            ["uidNoteTagLabel",   "uidNoteAddTag"],
            ["uidNoteLabel",      "uidNoteAddNote"]
        ]
    },
    "uidNoteAddTitle": {
        W3Const.w3PropType: W3Const.w3TypeText
    },
    "uidNoteAddTag": {
        W3Const.w3PropType: W3Const.w3TypeCombobox,
        W3Const.w3PropFunc: {
            W3Const.w3FuncCreator: "EJCreateNoteTagCombo"
        }
    },
    "uidNoteAddNote": {
        W3Const.w3PropType: W3Const.w3TypeTextEditor,
        W3Const.w3PropAttr: {
            "rows": "32",
            "cols": "80"
        }
    },
    "uidNoteTitleLabel": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropClass: "cidRightLabel",
        W3Const.w3PropString: "sidNoteTitleLabel"
    }
}
