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
            ["uidNoteTagLabel", "uidNoteTag", "uidNoteGetButton", "uidNoteAddButton"]
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
                "EJDisplayHTMLNote('')",
                "W3SetUIText('uidNoteContentTitleLabel', '')"
            ]
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
            ["uidNoteListTableHeaderSelectMark", "uidTableHeaderInvisibleData", "uidNoteListTableHeaderTitle"]
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
            "uidNullLabel"
        ]
    },
    "uidNoteListTableHeaderTitle": {
        W3Const.w3PropType: W3Const.w3TypeTableHeader,
        W3Const.w3PropSubUI: [
            "uidNullLabel"
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
            "padding-left": "15px",
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
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropSubUI: [
            "uidNoteHTMLContent",
            "uidNotePDFContent"
        ]
    },
    "uidNoteHTMLContent": {
        W3Const.w3PropType: W3Const.w3TypeDisplayPanel,
        W3Const.w3PropCSS: {
            "display": "none"
        }
    },
    "uidNotePDFContent": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropSubUI: [
            "uidNotePDFCanvas"
        ],
        W3Const.w3PropCSS: {
            "display": "none"
        }
    },
    "uidNotePDFCanvas": {
        W3Const.w3PropType: W3Const.w3TypePDFCanvas
    },

    # Note - Operation
    
    "uidNoteOperationPanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropSubUI: [
            "uidNoteEditButton"
        ],
        W3Const.w3PropCSS: {
            "clear": "both",
            "padding-top": "5px",
            "float": "right"
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
            "uidNoteEditorPanel",
            "uidNoteEditOperationPanel"
        ]
    },
    "uidNoteEditID": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropCSS: {
            "display": "none"
        }
    },
    "uidNoteEditorPanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropSubUI: [
            "uidNoteHTMLEditorWrapper",
            "uidNotePDFEditor"
        ]
    },
    "uidNoteHTMLEditorWrapper": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropSubUI: [
            # The wrapper is needed because the actual control will be hide deep in plugin
            "uidNoteHTMLEditor"
        ],
        W3Const.w3PropCSS: {
            "display": "none"
        }
    },
    "uidNoteHTMLEditor": {
        W3Const.w3PropType: W3Const.w3TypeTextEditor,
        W3Const.w3PropAttr: {
            "rows": "32",
            "cols": "80"
        }
    },
    "uidNotePDFEditor": {
        W3Const.w3PropType: W3Const.w3TypePlainTextEditor,
        W3Const.w3PropAttr: {
            "rows": "32",
            "cols": "80"
        },
        W3Const.w3PropCSS: {
            "display": "none"
        }
    },
    "uidNoteEditOperationPanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropSubUI: [
            "uidNoteEditOperationTable"
        ],
        W3Const.w3PropCSS: {
            "clear": "both",
            "padding-top": "5px",
            "float": "right"
        }
    },
    "uidNoteEditOperationTable": {
        W3Const.w3PropType: W3Const.w3TypeTable,
        W3Const.w3PropSubUI: [
            [],
            ["uidNoteHTMLSaveButton", "uidNotePDFSaveButton", "uidNoteEditCancelButton"]
        ]
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
    "uidNoteHTMLSaveButton": {
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
                W3Const.w3ApiDataValue: "uidNoteHTMLEditor"
            }]
        }],
        W3Const.w3PropEvent: {
            W3Const.w3EventClick: [
                W3Const.w3PlaceHolder_1
            ]
        },
        W3Const.w3PropCSS: {
            "display": "none"
        }
    },
    "uidNotePDFSaveButton": {
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
                W3Const.w3ApiDataValue: "uidNotePDFEditor"
            }]
        }],
        W3Const.w3PropEvent: {
            W3Const.w3EventClick: [
                W3Const.w3PlaceHolder_1
            ]
        },
        W3Const.w3PropCSS: {
            "display": "none"
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
            ["uidNoteAddSubmitHTML", "uidNoteAddSubmitPDF", "uidNoteAddCancelButton"]
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
    "uidNoteAddSubmitHTML": {
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
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeUID,
                W3Const.w3ApiDataValue: "uidNoteAddType"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeVar,
                W3Const.w3ApiDataValue: W3Const.w3Session
            }],
            W3Const.w3ApiPost: [
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeUID,
                W3Const.w3ApiDataValue: "uidNoteAddHTML"
            }]
        }],
        W3Const.w3PropEvent: {
            W3Const.w3EventClick: [
                W3Const.w3PlaceHolder_1
            ]
        },
        W3Const.w3PropCSS: {
            "display": "block"
        }
    },
    "uidNoteAddSubmitPDF": {
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
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeUID,
                W3Const.w3ApiDataValue: "uidNoteAddType"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeVar,
                W3Const.w3ApiDataValue: W3Const.w3Session
            }],
            W3Const.w3ApiPost: [
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeUID,
                W3Const.w3ApiDataValue: "uidNoteAddPDF"
            }]
        }],
        W3Const.w3PropEvent: {
            W3Const.w3EventClick: [
                W3Const.w3PlaceHolder_1
            ]
        },
        W3Const.w3PropCSS: {
            "display": "none"
        }
    },
    "uidNoteAddTable": {
        W3Const.w3PropType: W3Const.w3TypeTable,
        W3Const.w3PropSubUI: [
            [], # No header
            ["uidNoteTitleLabel", "uidNoteAddTitle"],
            ["uidNoteTagLabel",   "uidNoteAddTag"],
            ["uidNoteTypeLabel",  "uidNoteAddType"],
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
    "uidNoteAddType": {
        W3Const.w3PropType: W3Const.w3TypeCombobox,
        W3Const.w3PropFunc: {
            W3Const.w3FuncCreator: "EJCreateNoteTypeCombo"
        },
        W3Const.w3PropEvent: {
            W3Const.w3EventChange: [
                "EJOnNoteTypeChange()"
            ]
        }
    },
    "uidNoteAddNote": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropSubUI: [
            "uidNoteAddHTMLWrapper",
            "uidNoteAddPDF"
        ]
    },
    "uidNoteAddHTMLWrapper": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropSubUI: [
            # The wrapper is needed because the actual control will be hide deep in plugin
            "uidNoteAddHTML"
        ],
        W3Const.w3PropCSS: {
            "display": "block"
        }
    },
    "uidNoteAddHTML": {
        W3Const.w3PropType: W3Const.w3TypeTextEditor,
        W3Const.w3PropAttr: {
            "rows": "32",
            "cols": "80"
        }
    },
    "uidNoteAddPDF": {
        W3Const.w3PropType: W3Const.w3TypePlainTextEditor,
        W3Const.w3PropCSS: {
            "display": "none"
        },
        W3Const.w3PropAttr: {
            "rows": "32",
            "cols": "80"
        }
    },
    "uidNoteTitleLabel": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropClass: "cidRightLabel",
        W3Const.w3PropString: "sidNoteTitleLabel"
    },
    "uidNoteTypeLabel": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropClass: "cidRightLabel",
        W3Const.w3PropString: "sidNoteTypeLabel"
    }
}
