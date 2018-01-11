{
    # Financial Page - report tab
    "uidFinanceTabReportPanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropSubUI: [
            "uidFinanceReportFilterTable",
            "uidFinanceReportTable"
        ]
    },

    # Financial Page - report tab, filter
    "uidFinanceReportFilterTable": {
        W3Const.w3PropType: W3Const.w3TypeTable,
        W3Const.w3PropSubUI: [
            [], # No header
            ["uidFinanceReportFilterPanel"]
        ]
    },
    "uidFinanceReportFilterPanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropSubUI: [
            "uidMonthLabel",
            "uidFinanceReportFilterDatePicker",
            "uidFinanceReportFilterGetButton"
        ]
    },
    "uidFinanceReportFilterDatePicker": {
        W3Const.w3PropType: W3Const.w3TypeMonthPicker,
    },
    "uidFinanceReportFilterGetButton": {
        W3Const.w3PropType: W3Const.w3TypeButton,
        W3Const.w3PropString: "sidGet",
        W3Const.w3PropTriggerApi: [
        {
            W3Const.w3ApiID: "aidFinanceReport",
            W3Const.w3ApiParams: [
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeUID,
                W3Const.w3ApiDataValue: "uidFinanceReportFilterDatePicker"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeVar,
                W3Const.w3ApiDataValue: "session"
            }]
        }],
        W3Const.w3PropEvent: {
            W3Const.w3EventClick: [
                W3Const.w3PlaceHolder_1
            ]
        }
    },

    # Financial Page - report tab, table
    "uidFinanceReportTable": {
        W3Const.w3PropType: W3Const.w3TypeTable,
        W3Const.w3PropCSS: {
            "border": "1px solid"
        },
        W3Const.w3PropSubUI: [
            ["uidNullLabel",       "uidColumnMonthReport",             "uidColumnYearReport"],
            ["uidIncomeLabel",     "uidFinanceReportIncomeValue",      "uidFinanceReportIncomeYearValue"],
            ["uidDepositLabel",    "uidFinanceReportDepositValue",     "uidFinanceReportDepositYearValue"],
            ["uidDebtLabel",       "uidFinanceReportDebtValue",        "uidFinanceReportDebtYearValue"],
            ["uidConsumeLabel",    "uidFinanceReportConsumeValue",     "uidFinanceReportConsumeYearValue"],
            ["uidBalanceLabel",    "uidFinanceReportBalanceValue",     "uidFinanceReportBalanceYearValue"],
            ["uidCategoryLabel",   "uidFinanceCategoryReportPanel",    "uidFinanceCategoryYearReportPanel"],
            ["uidPaymentLabel",    "uidFinancePaymentmodeReportPanel", "uidFinancePaymentmodeYearReportPanel"]
        ],
        W3Const.w3PropSinkApi: {
            W3Const.w3ApiID: "aidFinanceReport",
            W3Const.w3SinkMatrix: [
                ## Row 1, income
                [{
                    ## Column 1
                    W3Const.w3ApiDataType: W3Const.w3ApiDataTypeNone,
                    W3Const.w3ApiDataValue: ""
                },
                {
                    ## Column 2
                    W3Const.w3ApiDataType: W3Const.w3ApiDataTypeNum,
                    W3Const.w3ApiDataValue: "income"
                },
                {
                    ## Column 3
                    W3Const.w3ApiDataType: W3Const.w3ApiDataTypeNum,
                    W3Const.w3ApiDataValue: "incomeyear"
                }],
                ## Row 2, deposit
                [{
                    ## Column 1
                    W3Const.w3ApiDataType: W3Const.w3ApiDataTypeNone,
                    W3Const.w3ApiDataValue: ""
                },
                {
                    ## Column 2
                    W3Const.w3ApiDataType: W3Const.w3ApiDataTypeNum,
                    W3Const.w3ApiDataValue: "deposit"
                },
                {
                    ## Column 3
                    W3Const.w3ApiDataType: W3Const.w3ApiDataTypeNum,
                    W3Const.w3ApiDataValue: "deposityear"
                }],
                ## Row 3, debt
                [{
                    ## Column 1
                    W3Const.w3ApiDataType: W3Const.w3ApiDataTypeNone,
                    W3Const.w3ApiDataValue: ""
                },
                {
                    ## Column 2
                    W3Const.w3ApiDataType: W3Const.w3ApiDataTypeNum,
                    W3Const.w3ApiDataValue: "debt"
                },
                {
                    ## Column 3
                    W3Const.w3ApiDataType: W3Const.w3ApiDataTypeNum,
                    W3Const.w3ApiDataValue: "debtyear"
                }],
                ## Row 4, consume
                [{
                    ## Column 1
                    W3Const.w3ApiDataType: W3Const.w3ApiDataTypeNone,
                    W3Const.w3ApiDataValue: ""
                },
                {
                    ## Column 2
                    W3Const.w3ApiDataType: W3Const.w3ApiDataTypeNum,
                    W3Const.w3ApiDataValue: "consume"
                },
                {
                    ## Column 3
                    W3Const.w3ApiDataType: W3Const.w3ApiDataTypeNum,
                    W3Const.w3ApiDataValue: "consumeyear"
                }],
                ## Row 5, balance
                [{
                    ## Column 1
                    W3Const.w3ApiDataType: W3Const.w3ApiDataTypeNone,
                    W3Const.w3ApiDataValue: ""
                },
                {
                    ## Column 2
                    W3Const.w3ApiDataType: W3Const.w3ApiDataTypeNum,
                    W3Const.w3ApiDataValue: "balance"
                },
                {
                    ## Column 3
                    W3Const.w3ApiDataType: W3Const.w3ApiDataTypeNum,
                    W3Const.w3ApiDataValue: "balanceyear"
                }],
                ## Row 6, category
                [{
                    ## Column 1
                    W3Const.w3ApiDataType: W3Const.w3ApiDataTypeNone,
                    W3Const.w3ApiDataValue: ""
                },
                {
                    ## Column 2
                    W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
                    W3Const.w3ApiDataValue: "category"
                },
                {
                    ## Column 3
                    W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
                    W3Const.w3ApiDataValue: "categoryyear"
                }],
                ## Row 7, payment mode
                [{
                    ## Column 1
                    W3Const.w3ApiDataType: W3Const.w3ApiDataTypeNone,
                    W3Const.w3ApiDataValue: ""
                },
                {
                    ## Column 2
                    W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
                    W3Const.w3ApiDataValue: "paymentmode"
                },
                {
                    ## Column 3
                    W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
                    W3Const.w3ApiDataValue: "paymentmodeyear"
                }]
            ]
        }
    },
    "uidFinanceReportCanvasPlaceHolder": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropString: "sidNull",
        W3Const.w3PropClass: "cidRightLable"
    },
    "uidFinanceReportIncomeValue": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropString: "sidNull",
        W3Const.w3PropClass: "cidRightLable",
        W3Const.w3PropFunc: {
            W3Const.w3FuncProcessor: [
                "W3FormatCurrency(w3PlaceHolder_1)"
            ]
        }                        
    },
    "uidFinanceReportDepositValue": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropPrototype: "uidFinanceReportIncomeValue"
    },
    "uidFinanceReportDebtValue": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropPrototype: "uidFinanceReportIncomeValue"
    },
    "uidFinanceReportConsumeValue": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropPrototype: "uidFinanceReportIncomeValue"
    },
    "uidFinanceReportBalanceValue": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropPrototype: "uidFinanceReportIncomeValue",
        W3Const.w3PropFunc: {
            W3Const.w3FuncProcessor: [
                "W3FormatCurrency(w3PlaceHolder_1)",
                "W3FormatCurrencyColor(w3PlaceHolder_1)"
            ]
        }                        
    },
    "uidFinanceReportIncomeYearValue": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropPrototype: "uidFinanceReportIncomeValue"
    },
    "uidFinanceReportDepositYearValue": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropPrototype: "uidFinanceReportIncomeValue"
    },
    "uidFinanceReportDebtYearValue": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropPrototype: "uidFinanceReportIncomeValue"
    },
    "uidFinanceReportConsumeYearValue": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropPrototype: "uidFinanceReportIncomeValue"
    },
    "uidFinanceReportBalanceYearValue": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropPrototype: "uidFinanceReportBalanceValue"
    },
    "uidFinanceCategoryReportPanel": {
        W3Const.w3PropType: W3Const.w3TypeCanvasPanel,
        W3Const.w3PropSubUI: [
            "uidFinanceReportCanvasPlaceHolder"
        ],
        W3Const.w3PropFunc: {
            W3Const.w3FuncProcessor: [
                "EJGenerateCategoryDrawFunc(w3PlaceHolder_1)"
            ]
        }                        
    },
    "uidFinanceCategoryYearReportPanel": {
        W3Const.w3PropType: W3Const.w3TypeCanvasPanel,
        W3Const.w3PropSubUI: [
            "uidFinanceReportCanvasPlaceHolder"
        ],
        W3Const.w3PropFunc: {
            W3Const.w3FuncProcessor: [
                "EJGenerateCategoryDrawFunc(w3PlaceHolder_1)"
            ]
        }                        
    },
    "uidFinancePaymentmodeReportPanel": {
        W3Const.w3PropType: W3Const.w3TypeCanvasPanel,
        W3Const.w3PropSubUI: [
            "uidFinanceReportCanvasPlaceHolder"
        ],
        W3Const.w3PropFunc: {
            W3Const.w3FuncProcessor: [
                "EJGeneratePaymentmodeDrawFunc(w3PlaceHolder_1)"
            ]
        }                        
    },
    "uidFinancePaymentmodeYearReportPanel": {
        W3Const.w3PropType: W3Const.w3TypeCanvasPanel,
        W3Const.w3PropSubUI: [
            "uidFinanceReportCanvasPlaceHolder"
        ],
        W3Const.w3PropFunc: {
            W3Const.w3FuncProcessor: [
                "EJGeneratePaymentmodeDrawFunc(w3PlaceHolder_1)"
            ]
        }                        
    }
}
