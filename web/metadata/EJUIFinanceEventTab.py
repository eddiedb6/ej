{    
    # Financial Page - event tab
    "uidFinanceTabEventPanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropSubUI: [
            "uidFinanceTabEventQueryPanel",
            "uidFinanceTabEventAddPanel"
        ]
    },

    # Finance Page - event tab, add
    "uidFinanceTabEventAddPanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropSubUI: [
            "uidFinanceEventAddTable",
            "uidFinanceEventAddOperationPanel"
        ],
        W3Const.w3PropCSS: {
            "display": "none"
        }
    },
    "uidFinanceEventAddOperationPanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropSubUI: [
            "uidFinanceEventAddOperationTable"
        ]
    },
    "uidFinanceEventAddOperationTable": {
        W3Const.w3PropType: W3Const.w3TypeTable,
        W3Const.w3PropSubUI: [
            [], # No header
            ["uidFinanceEventAddSubmitButton", "uidFinanceEventAddCancelButton"]
        ],
        W3Const.w3PropCSS: {
            "float": "right"
        }
    },
    "uidFinanceEventAddTable": {
        W3Const.w3PropType: W3Const.w3TypeTable,
        W3Const.w3PropSubUI: [
            [], # No header
            ["uidEventLabel",  "uidFinanceEventAddName"],
            ["uidBudgetLabel", "uidFinanceEventAddBudget"],
            ["uidNoteLabel",   "uidFinanceEventAddNote"]
        ]
    },
    "uidFinanceEventAddName": {
        W3Const.w3PropType: W3Const.w3TypeText
    },
    "uidFinanceEventAddBudget": {
        W3Const.w3PropType: W3Const.w3TypeText
    },
    "uidFinanceEventAddNote": {
        W3Const.w3PropType: W3Const.w3TypeText
    },
    "uidFinanceEventAddSubmitButton": {
        W3Const.w3PropType: W3Const.w3TypeButton,
        W3Const.w3PropString: "sidSubmit",
        W3Const.w3PropTriggerApi: [
        {
            W3Const.w3ApiID: "aidAddFinanceEvent",
            W3Const.w3ApiParams: [
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeUID,
                W3Const.w3ApiDataValue: "uidFinanceEventAddName"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeUID,
                W3Const.w3ApiDataValue: "uidFinanceEventAddBudget"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeUID,
                W3Const.w3ApiDataValue: "uidFinanceEventAddNote"
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
    "uidFinanceEventAddCancelButton": {
        W3Const.w3PropType: W3Const.w3TypeButton,
        W3Const.w3PropString: "sidCancel",
        W3Const.w3PropEvent: {
            W3Const.w3EventClick: [
                "W3HideUI('uidFinanceTabEventAddPanel')",
                "W3DisplayUI('uidFinanceTabEventQueryPanel')"
            ]
        }
    },

    # Finance Page - event tab, query
    "uidFinanceTabEventQueryPanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropSubUI: [
            "uidFinanceEventFilterTable",
            "uidFinanceEventTable"
        ]
    },
    "uidFinanceEventTable": {
        W3Const.w3PropType: W3Const.w3TypeTable,
        W3Const.w3PropSubUI: [
            ["uidColumnEvent", "uidTableHeaderBudget", "uidTableHeaderBalance", "uidColumnNote"]
        ],
        W3Const.w3PropCSS: {
            "border": "1px solid"
        },
        W3Const.w3PropSinkApi: {
            W3Const.w3ApiID: "aidFinanceEvent",
            W3Const.w3SinkRow: [
            {
                # Column 1 map to API result field "name"
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
                W3Const.w3ApiDataValue: "name"
            },
            {
                # Column 2 map to API result field "budget"
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeNum,
                W3Const.w3ApiDataValue: "budget"
            },
            {
                # Column 3 map to API result field "balance"
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeNum,
                W3Const.w3ApiDataValue: "balance"
            },
            {
                # Column 4 map to API result field "note"
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
                W3Const.w3ApiDataValue: "note"
            }]
        }
    },
    "uidFinanceEventFilterTable": {
        W3Const.w3PropType: W3Const.w3TypeTable,
        W3Const.w3PropSubUI: [
            [], # No header
            ["uidEventLabel", "uidFinanceEventNameText", "uidFinanceEventGetButton", "uidFinanceEventAddButton"]
        ]
    },
    "uidFinanceEventNameText": {
        W3Const.w3PropType: W3Const.w3TypeText
    },
    "uidFinanceEventGetButton": {
        W3Const.w3PropType: W3Const.w3TypeButton,
        W3Const.w3PropString: "sidGet",
        W3Const.w3PropTriggerApi: [
        {
            W3Const.w3ApiID: "aidFinanceEvent",
            W3Const.w3ApiParams: [
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeUID,
                W3Const.w3ApiDataValue: "uidFinanceEventNameText"
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
        },
        W3Const.w3PropCSS: {
            "float": "right"
        }
    },
    "uidFinanceEventAddButton": {
        W3Const.w3PropType: W3Const.w3TypeButton,
        W3Const.w3PropString: "sidAdd",
        W3Const.w3PropEvent: {
            W3Const.w3EventClick: [
                "W3HideUI('uidFinanceTabEventQueryPanel')",
                "W3DisplayUI('uidFinanceTabEventAddPanel')"
            ]
        }
    }
}
