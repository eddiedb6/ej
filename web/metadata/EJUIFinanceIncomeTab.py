{
    # Finance Page - income tab
    "uidFinanceTabIncomePanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropSubUI: [
            "uidFinanceTabIncomeQueryPanel",
            "uidFinanceTabIncomeAddPanel"
        ]
    },

    # Finance Page - income tab, query
    "uidFinanceTabIncomeQueryPanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropSubUI: [
            "uidIncomeFilterTable",
            "uidIncomeDisplayTable"
        ],
    },

    # Finance Page - income tab, query, display
    "uidIncomeDisplayTable": {
        W3Const.w3PropType: W3Const.w3TypeTable,
        W3Const.w3PropSubUI: [
            [], # No header
            ["uidIncomeTable"],
            ["uidIncomeTotalPanel"]
        ]
    },
    "uidIncomeTable": {
        W3Const.w3PropType: W3Const.w3TypeTable,
        W3Const.w3PropSubUI: [
            ["uidColumnOwner", "uidTableHeaderDatetime", "uidTableHeaderAmount", "uidColumnCurrency", "uidColumnCategory", "uidColumnNote"]
        ],
        W3Const.w3PropCSS: {
            "border": "1px solid"
        },
        W3Const.w3PropBindingApi: {
            W3Const.w3ApiID: "aidIncome",
            W3Const.w3BindingRow: [
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
                # Column 6 map to API result field "note"
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
                W3Const.w3ApiDataValue: "note"
            }]
        }
    },
    "uidIncomeTotalPanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropSubUI: [
            "uidTotalLabel",
            "uidIncomeTotalAmount"
        ],
        W3Const.w3PropCSS: {
            "text-align": "right"
        }
    },
    "uidIncomeTotalAmount": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropPrototype: "uidTotalAmount"
    },

    # Finance Page - income tab, query, filter    
    "uidIncomeFilterTable": {
        W3Const.w3PropType: W3Const.w3TypeTable,
        W3Const.w3PropSubUI: [
            [], # No header
            ["uidFromLabel", "uidIncomeFilterFromDatePicker", "uidToLabel", "uidIncomeFilterToDatePicker", "uidIncomeFilterGetButton", "uidIncomeFilterAddButton"]
        ]
    },
    "uidIncomeFilterFromDatePicker": {
        W3Const.w3PropType: W3Const.w3TypeDatePicker,
    },
    "uidIncomeFilterToDatePicker": {
        W3Const.w3PropType: W3Const.w3TypeDatePicker,
    },
    "uidIncomeFilterGetButton": {
        W3Const.w3PropType: W3Const.w3TypeButton,
        W3Const.w3PropString: "sidGet",
        W3Const.w3PropTriggerApi: {
            W3Const.w3TriggerEvent: W3Const.w3EventClick,
            W3Const.w3ApiID: "aidIncome",
            W3Const.w3ApiParams: [
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeUID,
                W3Const.w3ApiDataValue: "uidIncomeFilterFromDatePicker"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeUID,
                W3Const.w3ApiDataValue: "uidIncomeFilterToDatePicker"
            }]
        }
    },
    "uidIncomeFilterAddButton": {
        W3Const.w3PropType: W3Const.w3TypeButton,
        W3Const.w3PropString: "sidAdd",
        W3Const.w3PropEvent: {
            W3Const.w3EventClick: [
                "W3HideUI('uidFinanceTabIncomeQueryPanel')",
                "W3DisplayUI('uidFinanceTabIncomeAddPanel')"
            ]
        }
    },

    # Finance Page - income tab, add
    "uidFinanceTabIncomeAddPanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropSubUI: [
            "uidIncomeAddTable",
            "uidIncomeAddOperationPanel"
        ],
        W3Const.w3PropCSS: {
            "display": "none"
        }
    },

    # Finance Page - income tab, add, operation
    "uidIncomeAddOperationPanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropSubUI: [
            "uidIncomeAddOperationTable"
        ]
    },
    "uidIncomeAddOperationTable": {
        W3Const.w3PropType: W3Const.w3TypeTable,
        W3Const.w3PropSubUI: [
            [], # No header
            ["uidIncomeAddSubmitButton", "uidIncomeAddCancelButton"]
        ],
        W3Const.w3PropCSS: {
            "float": "right"
        }
    },
    "uidIncomeAddSubmitButton": {
        W3Const.w3PropType: W3Const.w3TypeButton,
        W3Const.w3PropString: "sidSubmit",
        W3Const.w3PropTriggerApi: {
            W3Const.w3TriggerEvent: W3Const.w3EventClick,
            W3Const.w3ApiID: "aidAddIncome",
            W3Const.w3ApiParams: [
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeUID,
                W3Const.w3ApiDataValue: "uidIncomeAddOwner"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeUID,
                W3Const.w3ApiDataValue: "uidIncomeAddDatetime"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeUID,
                W3Const.w3ApiDataValue: "uidIncomeAddAmount"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeUID,
                W3Const.w3ApiDataValue: "uidIncomeAddCurrency"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeUID,
                W3Const.w3ApiDataValue: "uidIncomeAddCategory"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeUID,
                W3Const.w3ApiDataValue: "uidIncomeAddNote"
            }]
        },
        W3Const.w3PropCSS: {
            "float": "right"
        }
    },
    "uidIncomeAddCancelButton": {
        W3Const.w3PropType: W3Const.w3TypeButton,
        W3Const.w3PropString: "sidCancel",
        W3Const.w3PropEvent: {
            W3Const.w3EventClick: [
                "W3HideUI('uidFinanceTabIncomeAddPanel')",
                "W3DisplayUI('uidFinanceTabIncomeQueryPanel')"
            ]
        },
        W3Const.w3PropCSS: {
            "float": "right"
        }
    },

    # Finance Page - income tab, add, table
    "uidIncomeAddTable": {
        W3Const.w3PropType: W3Const.w3TypeTable,
        W3Const.w3PropSubUI: [
            [], # No header
            ["uidOwnerLabel",    "uidIncomeAddOwner"],
            ["uidDatetimeLabel", "uidIncomeAddDatetime"],
            ["uidAmountLabel",   "uidIncomeAddAmount"],
            ["uidCurrencyLabel", "uidIncomeAddCurrency"],
            ["uidCategoryLabel", "uidIncomeAddCategory"],
            ["uidNoteLabel",     "uidIncomeAddNote"]
        ]
    },
    "uidIncomeAddDatetime": {
        W3Const.w3PropType: W3Const.w3TypeDatePicker
    },
    "uidIncomeAddAmount": {
        W3Const.w3PropType: W3Const.w3TypeText
    },
    "uidIncomeAddCurrency": {
        W3Const.w3PropType: W3Const.w3TypeCombobox,
        W3Const.w3PropFunc: {
            W3Const.w3FuncCreator: "EJCreateCurrencyCombo"
        }
    },
    "uidIncomeAddCategory": {
        W3Const.w3PropType: W3Const.w3TypeCombobox,
        W3Const.w3PropFunc: {
            W3Const.w3FuncCreator: "EJCreateIncomeCategoryCombo"
        }
    },
    "uidIncomeAddNote": {
        W3Const.w3PropType: W3Const.w3TypeText
    },
    "uidIncomeAddOwner": {
        W3Const.w3PropType: W3Const.w3TypeCombobox,
        W3Const.w3PropFunc: {
            W3Const.w3FuncCreator: "EJCreateOwnerCombo"
        }
    }
}
