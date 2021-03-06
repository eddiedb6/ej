{
    # Finance Page - bill tab
    "uidFinanceTabBillPanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropSubUI: [
            "uidFinanceTabBillQueryPanel",
            "uidFinanceTabBillAddPanel"
        ]
    },

    # Finance Page - bill tab, add
    "uidFinanceTabBillAddPanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropSubUI: [
            "uidBillAddTable",
            "uidBillAddOperationPanel"
        ],
        W3Const.w3PropCSS: {
            "display": "none"
        }
    },

    # Finance Page - bill tab, add, operation
    "uidBillAddOperationPanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropSubUI: [
            "uidBillAddOperationTable"
        ]
    },
    "uidBillAddOperationTable": {
        W3Const.w3PropType: W3Const.w3TypeTable,
        W3Const.w3PropSubUI: [
            [], # No header
            ["uidBillAddSubmitButton", "uidBillAddCancelButton"]
        ],
        W3Const.w3PropCSS: {
            "float": "right"
        }
    },
    "uidBillAddSubmitButton": {
        W3Const.w3PropType: W3Const.w3TypeButton,
        W3Const.w3PropString: "sidSubmit",
        W3Const.w3PropTriggerApi: [
        {
            W3Const.w3ApiID: "aidAddBill",
            W3Const.w3ApiParams: [
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeUID,
                W3Const.w3ApiDataValue: "uidBillAddOwner"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeUID,
                W3Const.w3ApiDataValue: "uidBillAddDatetime"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeUID,
                W3Const.w3ApiDataValue: "uidBillAddAmount"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeUID,
                W3Const.w3ApiDataValue: "uidBillAddCurrency"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeUID,
                W3Const.w3ApiDataValue: "uidBillAddCategory"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeUID,
                W3Const.w3ApiDataValue: "uidBillAddPaymentMode"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeUID,
                W3Const.w3ApiDataValue: "uidBillAddNote"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeUID,
                W3Const.w3ApiDataValue: "uidBillAddEvent"
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
    "uidBillAddCancelButton": {
        W3Const.w3PropType: W3Const.w3TypeButton,
        W3Const.w3PropString: "sidCancel",
        W3Const.w3PropEvent: {
            W3Const.w3EventClick: [
                "W3HideUI('uidFinanceTabBillAddPanel')",
                "W3DisplayUI('uidFinanceTabBillQueryPanel')"
            ]
        }
    },

    # Finance Page - bill tab, add, table
    "uidBillAddTable": {
        W3Const.w3PropType: W3Const.w3TypeTable,
        W3Const.w3PropSubUI: [
            [], # No header
            ["uidOwnerLabel",    "uidBillAddOwner"],
            ["uidDatetimeLabel", "uidBillAddDatetime"],
            ["uidAmountLabel",   "uidBillAddAmount"],
            ["uidCurrencyLabel", "uidBillAddCurrency"],
            ["uidCategoryLabel", "uidBillAddCategory"],
            ["uidPaymentLabel",  "uidBillAddPaymentMode"],
            ["uidNoteLabel",     "uidBillAddNote"],
            ["uidEventLabel",    "uidBillAddEvent"]
        ]
    },
    "uidBillAddDatetime": {
        W3Const.w3PropType: W3Const.w3TypeDatePicker
    },
    "uidBillAddAmount": {
        W3Const.w3PropType: W3Const.w3TypeText
    },
    "uidBillAddCurrency": {
        W3Const.w3PropType: W3Const.w3TypeCombobox,
        W3Const.w3PropFunc: {
            W3Const.w3FuncCreator: "EJCreateCurrencyCombo"
        }
    },
    "uidBillAddCategory": {
        W3Const.w3PropType: W3Const.w3TypeCombobox,
        W3Const.w3PropFunc: {
            W3Const.w3FuncCreator: "EJCreateBillCategoryCombo"
        }
    },
    "uidBillAddPaymentMode": {
        W3Const.w3PropType: W3Const.w3TypeCombobox,
        W3Const.w3PropFunc: {
            W3Const.w3FuncCreator: "EJCreatePaymentModeCombo"
        }
    },
    "uidBillAddNote": {
        W3Const.w3PropType: W3Const.w3TypeText
    },
    "uidBillAddEvent": {
        W3Const.w3PropType: W3Const.w3TypeText
    },
    "uidBillAddOwner": {
        W3Const.w3PropType: W3Const.w3TypeCombobox,
        W3Const.w3PropFunc: {
            W3Const.w3FuncCreator: "EJCreateOwnerCombo"
        }
    },

    # Finance Page - bill tab, query
    "uidFinanceTabBillQueryPanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropSubUI: [
            "uidBillFilterTable",
            "uidBillDisplayTable"
        ]
    },

    # Finance Page - bill tab, query, display
    "uidBillDisplayTable": {
        W3Const.w3PropType: W3Const.w3TypeTable,
        W3Const.w3PropSubUI: [
            [],
            ["uidBillTable"],
            ["uidBillTotalPanel"]
        ]
    },
    "uidBillTotalPanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropSubUI: [
            "uidTotalLabel",
            "uidBillTotalAmount"
        ],
        W3Const.w3PropCSS: {
            "text-align": "right"
        }
    },
    "uidBillTotalAmount": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropPrototype: "uidTotalAmountLabel",
        W3Const.w3PropBindingVar: {
            W3Const.w3BindingVarName: "billTotalAmount",
            W3Const.w3BindingType: W3Const.w3BindingUIDisplay,
            W3Const.w3BindingFormat: "F2"
        }
    },
    "uidBillTableHeaderAmount": {
        W3Const.w3PropType: W3Const.w3TypeTableHeader,
        W3Const.w3PropPrototype: "uidTableHeaderAmount",
        W3Const.w3PropFunc: {
            W3Const.w3FuncProcessor: [
                "EJCalcBillTotalAmount(w3PlaceHolder_1)"
            ]
        }
    },
    "uidBillTable": {
        W3Const.w3PropType: W3Const.w3TypeTable,
        W3Const.w3PropSubUI: [
            ["uidColumnOwner", "uidTableHeaderDatetime", "uidBillTableHeaderAmount", "uidColumnCurrency", "uidColumnCategory", "uidColumnPayment", "uidColumnNote"]
        ],
        W3Const.w3PropCSS: {
            "border": "1px solid"
        },
        W3Const.w3PropSinkApi: {
            W3Const.w3ApiID: "aidBill",
            W3Const.w3SinkRow: [
            {
                # Column 1 map to API result field "owner"
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
                W3Const.w3ApiDataValue: "owner"
            },
            {
                # Column 2 map to API result field "datetime"
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
                W3Const.w3ApiDataValue: "datetime"
            },
            {
                # Column 3 map to API result field "amount"
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeNum,
                W3Const.w3ApiDataValue: "amount"
            },
            {
                # Column 4 map to API result field "currency"
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeSID,
                W3Const.w3ApiDataValue: "currency"
            },
            {
                # Column 5 map to API result field "category"
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeSID,
                W3Const.w3ApiDataValue: "category"
            },
            {
                # Column 6 map to API result field "paymentmode"
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeSID,
                W3Const.w3ApiDataValue: "paymentmode"
            },
            {
                # Column 7 map to API result field "note"
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
                W3Const.w3ApiDataValue: "note"
            }]
        }
    },

    # Finance Page - bill tab, query, filter
    "uidBillFilterTable": {
        W3Const.w3PropType: W3Const.w3TypeTable,
        W3Const.w3PropSubUI: [
            [], # No header
            ["uidFromLabel", "uidBillFilterFromDatePicker", "uidToLabel", "uidBillFilterToDatePicker", "uidBillFilterGetButton", "uidBillFilterAddButton"]
        ]
    },
    "uidBillFilterFromDatePicker": {
        W3Const.w3PropType: W3Const.w3TypeDatePicker,
    },
    "uidBillFilterToDatePicker": {
        W3Const.w3PropType: W3Const.w3TypeDatePicker,
    },
    "uidBillFilterGetButton": {
        W3Const.w3PropType: W3Const.w3TypeButton,
        W3Const.w3PropString: "sidGet",
        W3Const.w3PropTriggerApi: [
        {
            W3Const.w3ApiID: "aidBill",
            W3Const.w3ApiParams: [
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeUID,
                W3Const.w3ApiDataValue: "uidBillFilterFromDatePicker"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeUID,
                W3Const.w3ApiDataValue: "uidBillFilterToDatePicker"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeVar,
                W3Const.w3ApiDataValue: W3Const.w3Session
            }]
        }],
        W3Const.w3PropEvent: {
            W3Const.w3EventClick: [
                "W3SetVariable(billTotalAmount, 0)",
                W3Const.w3PlaceHolder_1 # Reserve for the first API in w3PropTrigger
            ]
        }
    },
    "uidBillFilterAddButton": {
        W3Const.w3PropType: W3Const.w3TypeButton,
        W3Const.w3PropString: "sidAdd",
        W3Const.w3PropEvent: {
            W3Const.w3EventClick: [
                "W3HideUI('uidFinanceTabBillQueryPanel')",
                "W3DisplayUI('uidFinanceTabBillAddPanel')"
            ]
        }
    }
}
