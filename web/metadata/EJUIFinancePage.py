{
    "uidPageFinance": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropSubUI: [
            "uidFinanceTab"
        ]
    },
    "uidFinanceTab": {
        W3Const.w3PropType: W3Const.w3TypeTab,
        W3Const.w3PropSubUI: [
            ["uidFinanceTabBillLabel",   "uidFinanceTabBillPanel"],
            ["uidFinanceTabIncomeLabel", "uidFinanceTabIncomePanel"],
            ["uidFinanceTabDebtLabel",   "uidFinanceTabDebtPanel"],
            ["uidFinanceTabReportLabel", "uidFinanceTabReportPanel"],
            ["uidFinanceTabEventLabel",  "uidFinanceTabEventPanel"]
        ],
        W3Const.w3PropCSS: {
            # CSS for tab only support these format
            "border-width": "1px",
            "border-style": "solid",
            "background-color": "white"
        }
    },
    "uidFinanceTabBillLabel": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropString: "sidFinanceTabBill",
        W3Const.w3PropClass: "cidLRPadding"
    },
    "uidFinanceTabIncomeLabel": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropString: "sidFinanceTabIncome",
        W3Const.w3PropClass: "cidLRPadding"
    },
    "uidFinanceTabDebtLabel": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropString: "sidFinanceTabDebt",
        W3Const.w3PropClass: "cidLRPadding"
    },
    "uidFinanceTabReportLabel": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropString: "sidFinanceTabReport",
        W3Const.w3PropClass: "cidLRPadding"
    },
    "uidFinanceTabEventLabel": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropString: "sidFinanceTabEvent",
        W3Const.w3PropClass: "cidLRPadding"
    },

    "FinanceBillTab": ImportPartial("EJUIFinanceBillTab.py"),
    "FinanceIncomeTab": ImportPartial("EJUIFinanceIncomeTab.py"),
    "FinanceDebtTab": ImportPartial("EJUIFinanceDebtTab.py"),
    "FinanceReportTab": ImportPartial("EJUIFinanceReportTab.py"),
    "FinanceEventTab": ImportPartial("EJUIFinanceEventTab.py")
}
