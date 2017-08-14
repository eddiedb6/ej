{
    # Financial Page - debt tab
    "uidFinanceTabDebtPanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropSubUI: [
            "uidFinanceTabDebtQueryPanel",
            "uidFinanceTabDebtAddPanel"
        ]
    },

    # Finance Page - debt tab, query
    "uidFinanceTabDebtQueryPanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropSubUI: [
            "uidDebtFilterTable",
            "uidDebtTable"
        ],
    },

    # Finance Page - debt tab, query, filter
    "uidDebtFilterTable": {
        W3Const.w3PropType: W3Const.w3TypeTable,
        W3Const.w3PropSubUI: [
            [], # No header
            ["uidFromLabel", "uidDebtFilterFromDatePicker", "uidToLabel", "uidDebtFilterToDatePicker", "uidDebtFilterGetButton", "uidDebtFilterAddButton"]
        ]
    },
    "uidDebtFilterFromDatePicker": {
        W3Const.w3PropType: W3Const.w3TypeDatePicker,
    },
    "uidDebtFilterToDatePicker": {
        W3Const.w3PropType: W3Const.w3TypeDatePicker,
    },
    "uidDebtFilterGetButton": {
        W3Const.w3PropType: W3Const.w3TypeButton,
        W3Const.w3PropString: "sidGet",
        W3Const.w3PropEvent: {
            W3Const.w3EventClick: [
                "W3UpdateTableByAPI('uidDebtFilterGetButton', 'uidDebtTable')"
            ]
        },
        W3Const.w3PropApi: {
            W3Const.w3ApiID: "aidDebt",
            W3Const.w3ApiParams: [
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeUID,
                W3Const.w3ApiDataValue: "uidDebtFilterFromDatePicker"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeUID,
                W3Const.w3ApiDataValue: "uidDebtFilterToDatePicker"
            }]
        }
    },
    "uidDebtFilterAddButton": {
        W3Const.w3PropType: W3Const.w3TypeButton,
        W3Const.w3PropString: "sidAdd",
        W3Const.w3PropEvent: {
            W3Const.w3EventClick: [
                "W3HideUI('uidFinanceTabDebtQueryPanel')",
                "W3DisplayUI('uidFinanceTabDebtAddPanel')"
            ]
        }
    },

    # Finance Page - debt tab, query, table
    "uidDebtTable": {
        W3Const.w3PropType: W3Const.w3TypeTable,
        W3Const.w3PropSubUI: [
            ["uidTableHeaderStart", "uidTableHeaderEnd", "uidTableHeaderAmount", "uidTableHeaderBalance", "uidTableHeaderNote"]
        ],
        W3Const.w3PropCSS: {
            "border": "1px solid"
        },
        W3Const.w3PropApi: {
            W3Const.w3ApiID: "aidDebt",
            W3Const.w3ApiResult: {
                W3Const.w3ApiResultData: [
                {
                    # Column 1 map to API result field "start"
                    W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
                    W3Const.w3ApiDataValue: "start"
                },
                {
                    # Column 2 map to API result field "end"
                    W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
                    W3Const.w3ApiDataValue: "end"
                },
                {
                    # Column 3 map to API result field "amount"
                    W3Const.w3ApiDataType: W3Const.w3ApiDataTypeNum,
                    W3Const.w3ApiDataValue: "amount"
                },
                {
                    # Column 4 map to API result field "balance"
                    W3Const.w3ApiDataType: W3Const.w3ApiDataTypeNum,
                    W3Const.w3ApiDataValue: "balance"
                },
                {
                    # Column 5 map to API result field "note"
                    W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
                    W3Const.w3ApiDataValue: "note"
                }]
            }
        }
    },

    # Finance Page - debt tab, add
    "uidFinanceTabDebtAddPanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropSubUI: [
            "uidDebtAddTable",
            "uidDebtAddOperationPanel"
        ],
        W3Const.w3PropCSS: {
            "display": "none"
        }
    },

    # Finance Page - debt tab, add, operation
    "uidDebtAddOperationPanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropSubUI: [
            "uidDebtAddOperationTable"
        ]
    },
    "uidDebtAddOperationTable": {
        W3Const.w3PropType: W3Const.w3TypeTable,
        W3Const.w3PropSubUI: [
            [], # No header
            ["uidDebtAddSubmitButton", "uidDebtAddCancelButton"]
        ],
        W3Const.w3PropCSS: {
            "float": "right"
        }
    },
    "uidDebtAddSubmitButton": {
        W3Const.w3PropType: W3Const.w3TypeButton,
        W3Const.w3PropString: "sidSubmit",
        W3Const.w3PropApi: {
            W3Const.w3ApiID: "aidAddDebt",
            W3Const.w3ApiParams: [
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeUID,
                W3Const.w3ApiDataValue: "uidDebtAddStart"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeUID,
                W3Const.w3ApiDataValue: "uidDebtAddEnd"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeUID,
                W3Const.w3ApiDataValue: "uidDebtAddAmount"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeUID,
                W3Const.w3ApiDataValue: "uidDebtAddBalance"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeUID,
                W3Const.w3ApiDataValue: "uidDebtAddNote"
            }]
        },
        W3Const.w3PropEvent: {
            W3Const.w3EventClick: [
                "W3Submit('uidDebtAddSubmitButton')"
            ]
        },
        W3Const.w3PropCSS: {
            "float": "right"
        }
    },
    "uidDebtAddCancelButton": {
        W3Const.w3PropType: W3Const.w3TypeButton,
        W3Const.w3PropString: "sidCancel",
        W3Const.w3PropEvent: {
            W3Const.w3EventClick: [
                "W3HideUI('uidFinanceTabDebtAddPanel')",
                "W3DisplayUI('uidFinanceTabDebtQueryPanel')"
            ]
        },
        W3Const.w3PropCSS: {
            "float": "right"
        }
    },

     # Finance Page - debt tab, add, table
    "uidDebtAddTable": {
        W3Const.w3PropType: W3Const.w3TypeTable,
        W3Const.w3PropSubUI: [
            [], # No header
            ["uidStartLabel",   "uidDebtAddStart"],
            ["uidEndLabel",     "uidDebtAddEnd"],
            ["uidAmountLabel",  "uidDebtAddAmount"],
            ["uidBalanceLabel", "uidDebtAddBalance"],
            ["uidNoteLabel",    "uidDebtAddNote"]
        ]
    },
    "uidDebtAddStart": {
        W3Const.w3PropType: W3Const.w3TypeDatePicker
    },
    "uidDebtAddEnd": {
        W3Const.w3PropType: W3Const.w3TypeDatePicker
    },
    "uidDebtAddAmount": {
        W3Const.w3PropType: W3Const.w3TypeText
    },
    "uidDebtAddBalance": {
        W3Const.w3PropType: W3Const.w3TypeText
    },
    "uidDebtAddNote": {
        W3Const.w3PropType: W3Const.w3TypeText
    }
}
