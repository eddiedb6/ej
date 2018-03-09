{
    "uidPageNote": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropSubUI: [
            "uidNoteTagPanel",
            "uidNotePanel",
            "uidNoteOperationPanel"
        ]
    },

    # Tag
    
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
                W3Const.w3PlaceHolder_1
            ]
        }
    },

    # Note 
    
    "uidNotePanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropSubUI: [
            "uidNoteDisplayPanel",
            "uidNoteAddPanel"
        ]
    },

    # Note - display and edit
    
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
            ["uidNoteListTableHeaderID", "uidNoteListTableHeaderTitle"]
        ],
        W3Const.w3PropSinkApi: {
            W3Const.w3ApiID: "aidNoteTitle",
            W3Const.w3SinkRow: [
            {
                # Column 1 map to API result field "id"
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeNum,
                W3Const.w3ApiDataValue: "id"
            },
            {
                # Column 2 map to API result field "title"
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
                W3Const.w3ApiDataValue: "title"
            }]
        }
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
            "uidNoteContentBodyPanel",
            "uidNoteContentEditPanel"
        ]
    },

    "uidNoteContentTitlePanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropCSS: {
            "text-align": "center"
        }
    },
    
    "uidNoteContentBodyPanel": {
        W3Const.w3PropType: W3Const.w3TypePanel
    },
    
    "uidNoteContentEditPanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropCSS: {
            "display": "none"
        },
        W3Const.w3PropSubUI: [
            "uidNoteContentEditor"
        ]
    },

    "uidNoteContentEditor": {
        W3Const.w3PropType: W3Const.w3TypeTextEditor
    },

    # Note - add
    
    "uidNoteAddPanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropSubUI: [
        ],
        W3Const.w3PropCSS: {
            "display": "none"
        }
    },

    # Operation
    
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
                #"W3HideUI('uidFinanceTabBillQueryPanel')",
                #"W3DisplayUI('uidFinanceTabBillAddPanel')"
            ]
        }
    },

    "uidNoteEditButton": {
        W3Const.w3PropType: W3Const.w3TypeButton,
        W3Const.w3PropString: "sidEdit",
        W3Const.w3PropEvent: {
            W3Const.w3EventClick: [
                "EJEditCurrentNote()"
            ]
        }
    }
}
