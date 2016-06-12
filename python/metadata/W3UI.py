import sys
sys.path.append("..")
import W3Const

w3UI = {
    ###################################
    # User data should be added below #
    ###################################

    # Common UI
    "uidButtonBack": {
        W3Const.w3PropType: W3Const.w3TypeButton,
        W3Const.w3PropString: "sidButtonBack",
        W3Const.w3PropEvent: {
            W3Const.w3EventClick: "W3GoBack()"
        }
    },
    "uidLine": {
        W3Const.w3PropType: W3Const.w3TypeLine
    },
    "uidLineBreak": {
        W3Const.w3PropType: W3Const.w3TypeLineBreak
    },

    # Common Label
    "uidNullLabel": {
        W3Const.w3PropType: W3Const.w3TypeLabel
    },
    "uidTotalLabel": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropString: "sidTotalLabel",
        W3Const.w3PropClass: "cidLRPadding"
    },
    "uidTotalAmount": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropString: "sidTotalAmount",
        W3Const.w3PropClass: "cidLRPadding"
    },
    "uidFromLabel": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropString: "sidFromLabel"
    },
    "uidToLabel": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropString: "sidToLabel"
    },
    "uidDatetimeLabel": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropClass: "cidRightLable",
        W3Const.w3PropString: "sidDatetimeLabel"
    },
    "uidAmountLabel": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropClass: "cidRightLable",
        W3Const.w3PropString: "sidAmountLabel"
    },
    "uidCurrencyLabel": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropClass: "cidRightLable",
        W3Const.w3PropString: "sidCurrencyLabel"
    },
    "uidCategoryLabel": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropClass: "cidRightLable",
        W3Const.w3PropString: "sidCategoryLabel"
    },
    "uidSceneLabel": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropClass: "cidRightLable",
        W3Const.w3PropString: "sidSceneLabel"
    },
    "uidPaymentLabel": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropClass: "cidRightLable",
        W3Const.w3PropString: "sidPaymentLabel"
    },
    "uidNoteLabel": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropClass: "cidRightLable",
        W3Const.w3PropString: "sidNoteLabel"
    },
    "uidOwnerLabel": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropClass: "cidRightLable",
        W3Const.w3PropString: "sidOwnerLabel"
    },
    "uidIncomeLabel": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropClass: "cidRightLable",
        W3Const.w3PropString: "sidIncomeLabel"
    },
    "uidDepositLabel": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropClass: "cidRightLable",
        W3Const.w3PropString: "sidDepositLabel"
    },
    "uidDebtLabel": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropClass: "cidRightLable",
        W3Const.w3PropString: "sidDebtLabel"
    },
    "uidBalanceLabel": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropClass: "cidRightLable",
        W3Const.w3PropString: "sidBalanceLabel"
    },
    "uidConsumeLabel": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropClass: "cidRightLable",
        W3Const.w3PropString: "sidConsumeLabel"
    },
    "uidStartLabel": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropClass: "cidRightLable",
        W3Const.w3PropString: "sidStartLabel"
    },
    "uidEndLabel": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropClass: "cidRightLable",
        W3Const.w3PropString: "sidEndLabel"
    },
    "uidEventLabel": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropClass: "cidRightLable",
        W3Const.w3PropString: "sidEventLabel"
    },
    "uidBudgetLabel": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropClass: "cidRightLable",
        W3Const.w3PropString: "sidBudgetLabel"
    },
    "uidMonthLabel": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropString: "sidMonthLabel"
    },

    # Common Table Header
    "uidColumnOwner": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropString: "sidColumnOwner",
        W3Const.w3PropClass: "cidLRPadding"
    },
    "uidColumnDatetime": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropString: "sidColumnDatetime",
        W3Const.w3PropClass: "cidLRPadding"
    },
    "uidColumnAmount": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropString: "sidColumnAmount",
        W3Const.w3PropClass: "cidLRPadding"
    },
    "uidColumnCurrency": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropString: "sidColumnCurrency",
        W3Const.w3PropClass: "cidLRPadding"
    },
    "uidColumnCategory": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropString: "sidColumnCategory",
        W3Const.w3PropClass: "cidLRPadding"
    },
    "uidColumnScene": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropString: "sidColumnScene",
        W3Const.w3PropClass: "cidLRPadding"
    },
    "uidColumnPayment": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropString: "sidColumnPayment",
        W3Const.w3PropClass: "cidLRPadding"
    },
    "uidColumnNote": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropString: "sidColumnNote",
        W3Const.w3PropClass: "cidLRPadding"
    },
    "uidColumnStart": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropString: "sidColumnStart",
        W3Const.w3PropClass: "cidLRPadding"
    },
    "uidColumnEnd": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropString: "sidColumnEnd",
        W3Const.w3PropClass: "cidLRPadding"
    },
    "uidColumnBalance": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropString: "sidColumnBalance",
        W3Const.w3PropClass: "cidLRPadding"
    },
    "uidColumnEvent": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropString: "sidColumnEvent",
        W3Const.w3PropClass: "cidLRPadding"
    },
    "uidColumnMonthReport": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropClass: "cidLRPadding",
        W3Const.w3PropString: "sidColumnMonthReport"
    },
    "uidColumnYearReport": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropClass: "cidLRPadding",
        W3Const.w3PropString: "sidColumnYearReport"
    },
    "uidColumnBudget": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropClass: "cidLRPadding",
        W3Const.w3PropString: "sidColumnBudget"
    },

    # Main Page
    "uidBody": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropTypeDef: [
            "uidHeader",
            "uidMain",
            "uidFooter"
        ]
    },
    "uidHeader": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropTypeDef: [
            "uidTitle",
            "uidLine"
        ],
        W3Const.w3PropCSS: {
            "text-align": "center",
        }
    },
    "uidMain": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropTypeDef: [
            "uidNavigation",
            "uidContent"
        ]
    },
    "uidNavigation": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropTypeDef: [
            "uidNaviFinance",
            "uidLineBreak",
            "uidNaviDebug",
            "uidLineBreak"
        ],
        W3Const.w3PropClass: "cidLeftBorder",
        W3Const.w3PropCSS: {
            "padding-right": "15px"
        }
    },
    "uidContent": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropClass: "cidLRPadding",
        W3Const.w3PropFunc: {
            W3Const.w3FuncCreator: "W3SelectPage"
        },
        W3Const.w3PropClass: "cidLeftBorder"
    },
    "uidFooter": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropTypeDef: [
            "uidLine",
            "uidCopyright"
        ],
        W3Const.w3PropCSS: {
            "text-align": "center",
            "clear": "both",
            "padding-top": "5px",
        }
    },
    "uidTitle": {
        W3Const.w3PropType: W3Const.w3TypeHeadline,
        W3Const.w3PropTypeDef: "1",
        W3Const.w3PropString: "sidTitle" 
    },
    "uidCopyright": {
        W3Const.w3PropType: W3Const.w3TypeParagraph,
        W3Const.w3PropString: "sidCopyright"
    },

    # Navigation
    "uidNaviFinance": {
        W3Const.w3PropType: W3Const.w3TypeLink,
        W3Const.w3PropString: "sidNaviFinance",
        W3Const.w3PropApi: {
            W3Const.w3ApiID: "aidPage",
            W3Const.w3ApiParam1: "uidPageFinance"
        }
    },
    "uidNaviDebug": {
        W3Const.w3PropType: W3Const.w3TypeLink,
        W3Const.w3PropString: "sidNaviDebug",
        W3Const.w3PropApi: {
            W3Const.w3ApiID: "aidPage",
            W3Const.w3ApiParam1: "uidPageDebug"
        }
    },

    # Debug Page
    "uidPageDebug": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropTypeDef: [
            "uidDebugContent",
            "uidLineBreak",
            "uidButtonBack"
        ],
        W3Const.w3PropCSS: {
            "text-align": "center",
        }
    },
    "uidDebugContent": {
        W3Const.w3PropType: W3Const.w3TypeParagraph,
        W3Const.w3PropString: "sidDebugContent"
    },

    # Error Page
    "uidPageError": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropTypeDef: [
            "uidErrorContent",
            "uidLineBreak",
            "uidButtonBack"
        ],
        W3Const.w3PropCSS: {
            "text-align": "center",
        }
    },
    "uidErrorContent": {
        W3Const.w3PropType: W3Const.w3TypeParagraph,
        W3Const.w3PropString: "sidErrorContent"
    },

    # Finance Page
    "uidPageFinance": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropTypeDef: [
            "uidFinanceTab"
        ]
    },
    "uidFinanceTab": {
        W3Const.w3PropType: W3Const.w3TypeTab,
        W3Const.w3PropTypeDef: [
            ["uidFinanceTabBillLabel", "uidFinanceTabBillPanel"],
            ["uidFinanceTabIncomeLabel", "uidFinanceTabIncomePanel"],
            ["uidFinanceTabDebtLabel", "uidFinanceTabDebtPanel"],
            ["uidFinanceTabReportLabel", "uidFinanceTabReportPanel"],
            ["uidFinanceTabEventLabel", "uidFinanceTabEventPanel"]
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

    # Finance Page - bill tab
    "uidFinanceTabBillPanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropTypeDef: [
            "uidFinanceTabBillQueryPanel",
            "uidFinanceTabBillAddPanel"
        ]
    },

    # Finance Page - bill tab, add
    "uidFinanceTabBillAddPanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropTypeDef: [
            "uidBillAddTable",
            "uidBillAddOperationPanel"
        ],
        W3Const.w3PropCSS: {
            "display": "none"
        }
    },
    "uidBillAddOperationPanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropTypeDef: [
            "uidBillAddOperationTable"
        ]
    },
    "uidBillAddOperationTable": {
        W3Const.w3PropType: W3Const.w3TypeTable,
        W3Const.w3PropTypeDef: [
            [], # No header
            [
                "uidBillAddSubmitButton",
                "uidBillAddCancelButton"
            ]
        ],
        W3Const.w3PropCSS: {
            "float": "right"
        }
    },
    "uidBillAddTable": {
        W3Const.w3PropType: W3Const.w3TypeTable,
        W3Const.w3PropTypeDef: [
            [], # No header
            [
                "uidOwnerLabel",
                "uidBillAddOwner"
            ],
            [
                "uidDatetimeLabel",
                "uidBillAddDatetime"
            ],
            [
                "uidAmountLabel",
                "uidBillAddAmount"
            ],
            [
                "uidCurrencyLabel",
                "uidBillAddCurrency"
            ],
            [
                "uidCategoryLabel",
                "uidBillAddCategory"
            ],
            [
                "uidSceneLabel",
                "uidBillAddScene"
            ],
            [
                "uidPaymentLabel",
                "uidBillAddPaymentMode"
            ],
            [
                "uidNoteLabel",
                "uidBillAddNote"
            ],
            [
                "uidEventLabel",
                "uidBillAddEvent"
            ]
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
    "uidBillAddScene": {
        W3Const.w3PropType: W3Const.w3TypeCombobox,
        W3Const.w3PropFunc: {
            W3Const.w3FuncCreator: "EJCreateBillSceneCombo"
        }
    },
    "uidBillAddPaymentMode": {
        W3Const.w3PropType: W3Const.w3TypeCombobox,
        W3Const.w3PropFunc: {
            W3Const.w3FuncCreator: "EJCreatePaymentmodeCombo"
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
    "uidBillAddSubmitButton": {
        W3Const.w3PropType: W3Const.w3TypeButton,
        W3Const.w3PropString: "sidSubmit",
        W3Const.w3PropApi: {
            W3Const.w3ApiID: "aidAddBill",
            W3Const.w3ApiParam1: "uidBillAddOwner",
            W3Const.w3ApiParam2: "uidBillAddDatetime",
            W3Const.w3ApiParam3: "uidBillAddAmount",
            W3Const.w3ApiParam4: "uidBillAddCurrency",
            W3Const.w3ApiParam5: "uidBillAddCategory",
            W3Const.w3ApiParam6: "uidBillAddScene",
            W3Const.w3ApiParam7: "uidBillAddPaymentMode",
            W3Const.w3ApiParam8: "uidBillAddNote",
            W3Const.w3ApiParam9: "uidBillAddEvent"
        },
        W3Const.w3PropEvent: {
            W3Const.w3EventClick: "W3Submit('uidBillAddSubmitButton')"
        }
    },
    "uidBillAddCancelButton": {
        W3Const.w3PropType: W3Const.w3TypeButton,
        W3Const.w3PropString: "sidCancel",
        W3Const.w3PropEvent: {
            W3Const.w3EventClick: "EJCancelBillAdd()"
        }
    },

    # Finance Page - bill tab, query
    "uidFinanceTabBillQueryPanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropTypeDef: [
            "uidBillFilterTable",
            "uidBillDisplayTable"
        ]
    },
    "uidBillDisplayTable": {
        W3Const.w3PropType: W3Const.w3TypeTable,
        W3Const.w3PropTypeDef: [
            [],
            [
                "uidBillTable"
            ],
            [
                "uidBillTotalPanel"
            ]
        ]
    },
    "uidBillTotalPanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropTypeDef: [
            "uidTotalLabel",
            "uidBillTotalAmount"
        ],
        W3Const.w3PropCSS: {
            "text-align": "right"
        }
    },
    "uidBillTotalAmount": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropPrototype: "uidTotalAmount"
    },
    "uidBillFilterTable": {
        W3Const.w3PropType: W3Const.w3TypeTable,
        W3Const.w3PropTypeDef: [
            [], # No header
            [
                "uidFromLabel",
                "uidBillFilterFromDatePicker",
                "uidToLabel",
                "uidBillFilterToDatePicker",
                "uidBillFilterGetButton",
                "uidBillFilterAddButton"
            ]
        ]
    },
    "uidBillTable": {
        W3Const.w3PropType: W3Const.w3TypeTable,
        W3Const.w3PropTypeDef: [
            [
                "uidColumnOwner",
                "uidColumnDatetime",
                "uidColumnAmount",
                "uidColumnCurrency",
                "uidColumnCategory",
                "uidColumnScene",
                "uidColumnPayment",
                "uidColumnNote"
            ]
        ],
        W3Const.w3PropApi: [
            "owner",
            "datetime",
            "amount",
            "currency",
            "category",
            "scene",
            "paymentmode",
            "note"
        ],
        W3Const.w3PropCSS: {
            "border": "1px solid"
        }
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
        W3Const.w3PropEvent: {
            W3Const.w3EventClick: "W3UpdateTable('uidBillFilterGetButton', 'uidBillTable', EJUpdateBill)"
        },
        W3Const.w3PropApi: {
            W3Const.w3ApiID: "aidBill",
            W3Const.w3ApiParam1: "uidBillFilterFromDatePicker",
            W3Const.w3ApiParam2: "uidBillFilterToDatePicker"
        }
    },
    "uidBillFilterAddButton": {
        W3Const.w3PropType: W3Const.w3TypeButton,
        W3Const.w3PropString: "sidAdd",
        W3Const.w3PropEvent: {
            W3Const.w3EventClick: "EJAddBill()"
        }
    },

    # Finance Page - income tab
    "uidFinanceTabIncomePanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropTypeDef: [
            "uidFinanceTabIncomeQueryPanel",
            "uidFinanceTabIncomeAddPanel"
        ]
    },

    # Finance Page - income tab, query
    "uidFinanceTabIncomeQueryPanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropTypeDef: [
            "uidIncomeFilterTable",
            "uidIncomeDisplayTable"
        ],
    },
    "uidIncomeDisplayTable": {
        W3Const.w3PropType: W3Const.w3TypeTable,
        W3Const.w3PropTypeDef: [
            [],
            [
                "uidIncomeTable"
            ],
            [
                "uidIncomeTotalPanel"
            ]
        ]
    },
    "uidIncomeTotalPanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropTypeDef: [
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
    "uidIncomeFilterTable": {
        W3Const.w3PropType: W3Const.w3TypeTable,
        W3Const.w3PropTypeDef: [
            [], # No header
            [
                "uidFromLabel",
                "uidIncomeFilterFromDatePicker",
                "uidToLabel",
                "uidIncomeFilterToDatePicker",
                "uidIncomeFilterGetButton",
                "uidIncomeFilterAddButton"
            ]
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
        W3Const.w3PropEvent: {
            W3Const.w3EventClick: "W3UpdateTable('uidIncomeFilterGetButton', 'uidIncomeTable', EJUpdateIncome)"
        },
        W3Const.w3PropApi: {
            W3Const.w3ApiID: "aidIncome",
            W3Const.w3ApiParam1: "uidIncomeFilterFromDatePicker",
            W3Const.w3ApiParam2: "uidIncomeFilterToDatePicker"
        }
    },
    "uidIncomeFilterAddButton": {
        W3Const.w3PropType: W3Const.w3TypeButton,
        W3Const.w3PropString: "sidAdd",
        W3Const.w3PropEvent: {
            W3Const.w3EventClick: "EJAddIncome()"
        }
    },
    "uidIncomeTable": {
        W3Const.w3PropType: W3Const.w3TypeTable,
        W3Const.w3PropTypeDef: [
            [
                "uidColumnOwner",
                "uidColumnDatetime",
                "uidColumnAmount",
                "uidColumnCurrency",
                "uidColumnCategory",
                "uidColumnNote"
            ]
        ],
        W3Const.w3PropApi: [
            "owner",
            "datetime",
            "amount",
            "currency",
            "category",
            "note"
        ],
        W3Const.w3PropCSS: {
            "border": "1px solid"
        }
    },

    # Finance Page - income tab, add
    "uidFinanceTabIncomeAddPanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropTypeDef: [
            "uidIncomeAddTable",
            "uidIncomeAddOperationPanel"
        ],
        W3Const.w3PropCSS: {
            "display": "none"
        }
    },
    "uidIncomeAddOperationPanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropTypeDef: [
            "uidIncomeAddOperationTable"
        ]
    },
    "uidIncomeAddOperationTable": {
        W3Const.w3PropType: W3Const.w3TypeTable,
        W3Const.w3PropTypeDef: [
            [], # No header
            [
                "uidIncomeAddSubmitButton",
                "uidIncomeAddCancelButton"
            ]
        ],
        W3Const.w3PropCSS: {
            "float": "right"
        }
    },
    "uidIncomeAddTable": {
        W3Const.w3PropType: W3Const.w3TypeTable,
        W3Const.w3PropTypeDef: [
            [], # No header
            [
                "uidOwnerLabel",
                "uidIncomeAddOwner"
            ],
            [
                "uidDatetimeLabel",
                "uidIncomeAddDatetime"
            ],
            [
                "uidAmountLabel",
                "uidIncomeAddAmount"
            ],
            [
                "uidCurrencyLabel",
                "uidIncomeAddCurrency"
            ],
            [
                "uidCategoryLabel",
                "uidIncomeAddCategory"
            ],
            [
                "uidNoteLabel",
                "uidIncomeAddNote"
            ]
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
    },
    "uidIncomeAddSubmitButton": {
        W3Const.w3PropType: W3Const.w3TypeButton,
        W3Const.w3PropString: "sidSubmit",
        W3Const.w3PropApi: {
            W3Const.w3ApiID: "aidAddIncome",
            W3Const.w3ApiParam1: "uidIncomeAddOwner",
            W3Const.w3ApiParam2: "uidIncomeAddDatetime",
            W3Const.w3ApiParam3: "uidIncomeAddAmount",
            W3Const.w3ApiParam4: "uidIncomeAddCurrency",
            W3Const.w3ApiParam5: "uidIncomeAddCategory",
            W3Const.w3ApiParam6: "uidIncomeAddNote"
        },
        W3Const.w3PropEvent: {
            W3Const.w3EventClick: "W3Submit('uidIncomeAddSubmitButton')"
        },
        W3Const.w3PropCSS: {
            "float": "right"
        }
    },
    "uidIncomeAddCancelButton": {
        W3Const.w3PropType: W3Const.w3TypeButton,
        W3Const.w3PropString: "sidCancel",
        W3Const.w3PropEvent: {
            W3Const.w3EventClick: "EJCancelIncomeAdd()"
        },
        W3Const.w3PropCSS: {
            "float": "right"
        }
    },

    # Financial Page - debt tab
    "uidFinanceTabDebtPanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropTypeDef: [
            "uidFinanceTabDebtQueryPanel",
            "uidFinanceTabDebtAddPanel"
        ]
    },

    # Finance Page - debt tab, query
    "uidFinanceTabDebtQueryPanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropTypeDef: [
            "uidDebtFilterTable",
            "uidDebtTable"
        ],
    },
    "uidDebtFilterTable": {
        W3Const.w3PropType: W3Const.w3TypeTable,
        W3Const.w3PropTypeDef: [
            [], # No header
            [
                "uidFromLabel",
                "uidDebtFilterFromDatePicker",
                "uidToLabel",
                "uidDebtFilterToDatePicker",
                "uidDebtFilterGetButton",
                "uidDebtFilterAddButton"
            ]
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
            W3Const.w3EventClick: "W3UpdateTable('uidDebtFilterGetButton', 'uidDebtTable', EJUpdateDebt)"
        },
        W3Const.w3PropApi: {
            W3Const.w3ApiID: "aidDebt",
            W3Const.w3ApiParam1: "uidDebtFilterFromDatePicker",
            W3Const.w3ApiParam2: "uidDebtFilterToDatePicker"
        }
    },
    "uidDebtFilterAddButton": {
        W3Const.w3PropType: W3Const.w3TypeButton,
        W3Const.w3PropString: "sidAdd",
        W3Const.w3PropEvent: {
            W3Const.w3EventClick: "EJAddDebt()"
        }
    },
    "uidDebtTable": {
        W3Const.w3PropType: W3Const.w3TypeTable,
        W3Const.w3PropTypeDef: [
            [
                "uidColumnStart",
                "uidColumnEnd",
                "uidColumnAmount",
                "uidColumnBalance",
                "uidColumnNote"
            ]
        ],
        W3Const.w3PropApi: [
            "start",
            "end",
            "amount",
            "balance",
            "note"
        ],
        W3Const.w3PropCSS: {
            "border": "1px solid"
        }
    },

    # Finance Page - debt tab, add
    "uidFinanceTabDebtAddPanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropTypeDef: [
            "uidDebtAddTable",
            "uidDebtAddOperationPanel"
        ],
        W3Const.w3PropCSS: {
            "display": "none"
        }
    },
    "uidDebtAddOperationPanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropTypeDef: [
            "uidDebtAddOperationTable"
        ]
    },
    "uidDebtAddOperationTable": {
        W3Const.w3PropType: W3Const.w3TypeTable,
        W3Const.w3PropTypeDef: [
            [], # No header
            [
                "uidDebtAddSubmitButton",
                "uidDebtAddCancelButton"
            ]
        ],
        W3Const.w3PropCSS: {
            "float": "right"
        }
    },
    "uidDebtAddTable": {
        W3Const.w3PropType: W3Const.w3TypeTable,
        W3Const.w3PropTypeDef: [
            [], # No header
            [
                "uidStartLabel",
                "uidDebtAddStart"
            ],
            [
                "uidEndLabel",
                "uidDebtAddEnd"
            ],
            [
                "uidAmountLabel",
                "uidDebtAddAmount"
            ],
            [
                "uidBalanceLabel",
                "uidDebtAddBalance"
            ],
            [
                "uidNoteLabel",
                "uidDebtAddNote"
            ]
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
    },
    "uidDebtAddSubmitButton": {
        W3Const.w3PropType: W3Const.w3TypeButton,
        W3Const.w3PropString: "sidSubmit",
        W3Const.w3PropApi: {
            W3Const.w3ApiID: "aidAddDebt",
            W3Const.w3ApiParam1: "uidDebtAddStart",
            W3Const.w3ApiParam2: "uidDebtAddEnd",
            W3Const.w3ApiParam3: "uidDebtAddAmount",
            W3Const.w3ApiParam4: "uidDebtAddBalance",
            W3Const.w3ApiParam5: "uidDebtAddNote"
        },
        W3Const.w3PropEvent: {
            W3Const.w3EventClick: "W3Submit('uidDebtAddSubmitButton')"
        },
        W3Const.w3PropCSS: {
            "float": "right"
        }
    },
    "uidDebtAddCancelButton": {
        W3Const.w3PropType: W3Const.w3TypeButton,
        W3Const.w3PropString: "sidCancel",
        W3Const.w3PropEvent: {
            W3Const.w3EventClick: "EJCancelDebtAdd()"
        },
        W3Const.w3PropCSS: {
            "float": "right"
        }
    },

    # Financial Page - report tab
    "uidFinanceTabReportPanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropTypeDef: [
            "uidFinanceReportFilterTable",
            "uidFinanceReportTable"
        ]
    },
    "uidFinanceReportFilterTable": {
        W3Const.w3PropType: W3Const.w3TypeTable,
        W3Const.w3PropTypeDef: [
            [], # No header
            [
                "uidFinanceReportFilterPanel"
            ]
        ]
    },
    "uidFinanceReportFilterPanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropTypeDef: [
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
            W3Const.w3ApiParam1: "uidFinanceReportFilterDatePicker"
        },
        W3Const.w3PropEvent: {
            W3Const.w3EventClick: "EJGetFinaceReport('uidFinanceReportFilterGetButton')"
        }
    },
    "uidFinanceReportTable": {
        W3Const.w3PropType: W3Const.w3TypeTable,
        W3Const.w3PropCSS: {
            "border": "1px solid"
        },
        W3Const.w3PropTypeDef: [
            [
                "uidNullLabel",
                "uidColumnMonthReport",
                "uidColumnYearReport"
            ],
            [
                "uidIncomeLabel",
                "uidFinanceReportIncomeValue",
                "uidFinanceReportIncomeYearValue"
            ],
            [
                "uidDepositLabel",
                "uidFinanceReportDepositValue",
                "uidFinanceReportDepositYearValue"
            ],
            [
                "uidDebtLabel",
                "uidFinanceReportDebtValue",
                "uidFinanceReportDebtYearValue"
            ],
            [
                "uidConsumeLabel",
                "uidFinanceReportConsumeValue",
                "uidFinanceReportConsumeYearValue"
            ],
            [
                "uidBalanceLabel",
                "uidFinanceReportBalanceValue",
                "uidFinanceReportBalanceYearValue"
            ],
            [
                "uidCategoryLabel",
                "uidFinanceCategoryReportPanel",
                "uidFinanceCategoryYearReportPanel"
            ],
            [
                "uidSceneLabel",
                "uidFinanceSceneReportPanel",
                "uidFinanceSceneYearReportPanel"
            ],
            [
                "uidPaymentLabel",
                "uidFinancePaymentmodeReportPanel",
                "uidFinancePaymentmodeYearReportPanel"
            ]
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
        W3Const.w3PropTypeDef: [
            "uidFinanceReportCanvasPlaceHolder"
        ]        
    },
    "uidFinanceCategoryYearReportPanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropTypeDef: [
            "uidFinanceReportCanvasPlaceHolder"
        ]
    },
    "uidFinanceSceneReportPanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropTypeDef: [
            "uidFinanceReportCanvasPlaceHolder"
        ]        
    },
    "uidFinanceSceneYearReportPanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropTypeDef: [
            "uidFinanceReportCanvasPlaceHolder"
        ]
    },
    "uidFinancePaymentmodeReportPanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropTypeDef: [
            "uidFinanceReportCanvasPlaceHolder"
        ]        
    },
    "uidFinancePaymentmodeYearReportPanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropTypeDef: [
            "uidFinanceReportCanvasPlaceHolder"
        ]
    },

    # Financial Page - event tab
    "uidFinanceTabEventPanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropTypeDef: [
            "uidFinanceTabEventQueryPanel",
            "uidFinanceTabEventAddPanel"
        ]
    },

    # Finance Page - event tab, add
    "uidFinanceTabEventAddPanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropTypeDef: [
            "uidFinanceEventAddTable",
            "uidFinanceEventAddOperationPanel"
        ],
        W3Const.w3PropCSS: {
            "display": "none"
        }
    },
    "uidFinanceEventAddOperationPanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropTypeDef: [
            "uidFinanceEventAddOperationTable"
        ]
    },
    "uidFinanceEventAddOperationTable": {
        W3Const.w3PropType: W3Const.w3TypeTable,
        W3Const.w3PropTypeDef: [
            [], # No header
            [
                "uidFinanceEventAddSubmitButton",
                "uidFinanceEventAddCancelButton"
            ]
        ],
        W3Const.w3PropCSS: {
            "float": "right"
        }
    },
    "uidFinanceEventAddTable": {
        W3Const.w3PropType: W3Const.w3TypeTable,
        W3Const.w3PropTypeDef: [
            [], # No header
            [
                "uidEventLabel",
                "uidFinanceEventAddName"
            ],
            [
                "uidBudgetLabel",
                "uidFinanceEventAddBudget"
            ],
            [
                "uidNoteLabel",
                "uidFinanceEventAddNote"
            ]
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
        W3Const.w3PropApi: {
            W3Const.w3ApiID: "aidAddFinanceEvent",
            W3Const.w3ApiParam1: "uidFinanceEventAddName",
            W3Const.w3ApiParam2: "uidFinanceEventAddBudget",
            W3Const.w3ApiParam3: "uidFinanceEventAddNote"
        },
        W3Const.w3PropEvent: {
            W3Const.w3EventClick: "W3Submit('uidFinanceEventAddSubmitButton')"
        }
    },
    "uidFinanceEventAddCancelButton": {
        W3Const.w3PropType: W3Const.w3TypeButton,
        W3Const.w3PropString: "sidCancel",
        W3Const.w3PropEvent: {
            W3Const.w3EventClick: "EJCancelFinanceEventAdd()"
        }
    },

    # Finance Page - event tab, query
    "uidFinanceTabEventQueryPanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropTypeDef: [
            "uidFinanceEventFilterTable",
            "uidFinanceEventTable"
        ]
    },
    "uidFinanceEventTable": {
        W3Const.w3PropType: W3Const.w3TypeTable,
        W3Const.w3PropTypeDef: [
            [
                "uidColumnEvent",
                "uidColumnBudget",
                "uidColumnBalance",
                "uidColumnNote"
            ]
        ],
        W3Const.w3PropApi: [
            "name",
            "budget",
            "balance",
            "note"
        ],
        W3Const.w3PropCSS: {
            "border": "1px solid"
        }
    },
    "uidFinanceEventFilterTable": {
        W3Const.w3PropType: W3Const.w3TypeTable,
        W3Const.w3PropTypeDef: [
            [], # No header
            [
                "uidEventLabel",
                "uidFinanceEventNameText",
                "uidFinanceEventGetButton",
                "uidFinanceEventAddButton"
            ]
        ]
    },
    "uidFinanceEventNameText": {
        W3Const.w3PropType: W3Const.w3TypeText
    },
    "uidFinanceEventGetButton": {
        W3Const.w3PropType: W3Const.w3TypeButton,
        W3Const.w3PropString: "sidGet",
        W3Const.w3PropApi: {
            W3Const.w3ApiID: "aidFinanceEvent",
            W3Const.w3ApiParam1: "uidFinanceEventNameText"
        },
        W3Const.w3PropEvent: {
            W3Const.w3EventClick: "W3UpdateTable('uidFinanceEventGetButton', 'uidFinanceEventTable', EJUpdateFinanceEvent)"
        },
        W3Const.w3PropCSS: {
            "float": "right"
        }
    },
    "uidFinanceEventAddButton": {
        W3Const.w3PropType: W3Const.w3TypeButton,
        W3Const.w3PropString: "sidAdd",
        W3Const.w3PropEvent: {
            W3Const.w3EventClick: "EJAddFinanceEvent()"
        }
    }

    ###################################
    # User data should be added above #
    ###################################
}
