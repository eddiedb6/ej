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
        W3Const.w3PropApi: {
            W3Const.w3ApiID: "aidFinanceReport",
            W3Const.w3ApiParams: [
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeUID,
                W3Const.w3ApiDataValue: "uidFinanceReportFilterDatePicker"
            }]
        },
        W3Const.w3PropEvent: {
            W3Const.w3EventClick: [
                "EJGetFinanceReport('uidFinanceReportFilterGetButton')"
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
            ["uidTableHeaderNull", "uidTableHeaderMonthReport",        "uidTableHeaderYearReport"],
            ["uidIncomeLabel",     "uidFinanceReportIncomeValue",      "uidFinanceReportIncomeYearValue"],
            ["uidDepositLabel",    "uidFinanceReportDepositValue",     "uidFinanceReportDepositYearValue"],
            ["uidDebtLabel",       "uidFinanceReportDebtValue",        "uidFinanceReportDebtYearValue"],
            ["uidConsumeLabel",    "uidFinanceReportConsumeValue",     "uidFinanceReportConsumeYearValue"],
            ["uidBalanceLabel",    "uidFinanceReportBalanceValue",     "uidFinanceReportBalanceYearValue"],
            ["uidCategoryLabel",   "uidFinanceCategoryReportPanel",    "uidFinanceCategoryYearReportPanel"],
            ["uidPaymentLabel",    "uidFinancePaymentmodeReportPanel", "uidFinancePaymentmodeYearReportPanel"]
        ]
    },
    "uidFinanceReportCanvasPlaceHolder": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropString: "sidNull",
        W3Const.w3PropClass: "cidRightLable"
    },
    "uidFinanceReportIncomeValue": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropString: "sidNull",
        W3Const.w3PropClass: "cidRightLable"
    },
    "uidFinanceReportDepositValue": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropString: "sidNull",
        W3Const.w3PropClass: "cidRightLable"
    },
    "uidFinanceReportDebtValue": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropString: "sidNull",
        W3Const.w3PropClass: "cidRightLable"
    },
    "uidFinanceReportConsumeValue": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropString: "sidNull",
        W3Const.w3PropClass: "cidRightLable"
    },
    "uidFinanceReportBalanceValue": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropString: "sidNull",
        W3Const.w3PropClass: "cidRightLable"
    },
    "uidFinanceReportIncomeYearValue": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropString: "sidNull",
        W3Const.w3PropClass: "cidRightLable"
    },
    "uidFinanceReportDepositYearValue": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropString: "sidNull",
        W3Const.w3PropClass: "cidRightLable"
    },
    "uidFinanceReportDebtYearValue": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropString: "sidNull",
        W3Const.w3PropClass: "cidRightLable"
    },
    "uidFinanceReportConsumeYearValue": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropString: "sidNull",
        W3Const.w3PropClass: "cidRightLable"
    },
    "uidFinanceReportBalanceYearValue": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropString: "sidNull",
        W3Const.w3PropClass: "cidRightLable"
    },
    "uidFinanceCategoryReportPanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropSubUI: [
            "uidFinanceReportCanvasPlaceHolder"
        ]        
    },
    "uidFinanceCategoryYearReportPanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropSubUI: [
            "uidFinanceReportCanvasPlaceHolder"
        ]
    },
    "uidFinancePaymentmodeReportPanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropSubUI: [
            "uidFinanceReportCanvasPlaceHolder"
        ]        
    },
    "uidFinancePaymentmodeYearReportPanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropSubUI: [
            "uidFinanceReportCanvasPlaceHolder"
        ]
    }
}
