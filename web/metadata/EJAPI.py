{
    "aidBill": {
        W3Const.w3ElementType: W3Const.w3TypeApi,
        W3Const.w3ApiName: "bill",
        W3Const.w3ApiParams: [
        {
            W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
            W3Const.w3ApiDataValue: "from"
        },
        {
            W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
            W3Const.w3ApiDataValue: "to"
        }],
        W3Const.w3ApiResult: {
            W3Const.w3ApiResultStatus: [
                W3Const.w3ApiResultSuccessful,
                W3Const.w3ApiResultFailed
            ],
            W3Const.w3ApiResultData: [
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
                W3Const.w3ApiDataValue: "owner"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
                W3Const.w3ApiDataValue: "datetime"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeNum,
                W3Const.w3ApiDataValue: "amount"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeNum,
                W3Const.w3ApiDataValue: "currency"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeNum,
                W3Const.w3ApiDataValue: "category"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeNum,
                W3Const.w3ApiDataValue: "paymentmode"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
                W3Const.w3ApiDataValue: "note"
            }]
        },
        W3Const.w3ApiHandler: "EJGetBill"
    },

    "aidDebt": {
        W3Const.w3ElementType: W3Const.w3TypeApi,
        W3Const.w3ApiName: "debt",
        W3Const.w3ApiParams: [
        {
            W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
            W3Const.w3ApiDataValue: "from"
        },
        {
            W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
            W3Const.w3ApiDataValue: "to"
        }],
        W3Const.w3ApiResult: {
            W3Const.w3ApiResultStatus: [
                W3Const.w3ApiResultSuccessful,
                W3Const.w3ApiResultFailed
            ],
            W3Const.w3ApiResultData: [
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
                W3Const.w3ApiDataValue: "start"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
                W3Const.w3ApiDataValue: "end"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeNum,
                W3Const.w3ApiDataValue: "amount"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeNum,
                W3Const.w3ApiDataValue: "balance"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
                W3Const.w3ApiDataValue: "note"
            }]
        },
        W3Const.w3ApiHandler: "EJGetDebt"
    },
    
    "aidIncome": {
        W3Const.w3ElementType: W3Const.w3TypeApi,
        W3Const.w3ApiName: "income",
        W3Const.w3ApiParams: [
        {
            W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
            W3Const.w3ApiDataValue: "from"
        },
        {
            W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
            W3Const.w3ApiDataValue: "to"
        }],
        W3Const.w3ApiResult: {
            W3Const.w3ApiResultStatus: [
                W3Const.w3ApiResultSuccessful,
                W3Const.w3ApiResultFailed
            ],
            W3Const.w3ApiResultData: [
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
                W3Const.w3ApiDataValue: "owner"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
                W3Const.w3ApiDataValue: "datetime"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeNum,
                W3Const.w3ApiDataValue: "amount"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeNum,
                W3Const.w3ApiDataValue: "currency"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeNum,
                W3Const.w3ApiDataValue: "category"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
                W3Const.w3ApiDataValue: "note"
            }]
        },
        W3Const.w3ApiHandler: "EJGetIncome"
    },

    "aidFinanceReport": {
        W3Const.w3ElementType: W3Const.w3TypeApi,
        W3Const.w3ApiName: "financereport",
        W3Const.w3ApiParams: [
        {
            W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
            W3Const.w3ApiDataValue: "month"
        }],
        W3Const.w3ApiResult: {
            W3Const.w3ApiResultStatus: [
                W3Const.w3ApiResultSuccessful,
                W3Const.w3ApiResultFailed
            ],
            W3Const.w3ApiResultData: [
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeNum,
                W3Const.w3ApiDataValue: "income"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeNum,
                W3Const.w3ApiDataValue: "deposit"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeNum,
                W3Const.w3ApiDataValue: "debt"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeNum,
                W3Const.w3ApiDataValue: "consume"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeNum,
                W3Const.w3ApiDataValue: "balance"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
                W3Const.w3ApiDataValue: "category"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
                W3Const.w3ApiDataValue: "paymentmode"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeNum,
                W3Const.w3ApiDataValue: "incomeyear"
            },                
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeNum,
                W3Const.w3ApiDataValue: "deposityear"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeNum,
                W3Const.w3ApiDataValue: "debtyear"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeNum,
                W3Const.w3ApiDataValue: "consumeyear"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeNum,
                W3Const.w3ApiDataValue: "balanceyear"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
                W3Const.w3ApiDataValue: "categoryyear"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
                W3Const.w3ApiDataValue: "paymentmodeyear"
            }]
        },
        W3Const.w3ApiHandler: "EJGetFinanceReport"
    },

    "aidFinanceEvent": {
        W3Const.w3ElementType: W3Const.w3TypeApi,
        W3Const.w3ApiName: "financeevent",
        W3Const.w3ApiParams: [
        {
            W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
            W3Const.w3ApiDataValue: "name"
        }],
        W3Const.w3ApiResult: {
            W3Const.w3ApiResultStatus: [
                W3Const.w3ApiResultSuccessful,
                W3Const.w3ApiResultFailed
            ],
            W3Const.w3ApiResultData: [
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
                W3Const.w3ApiDataValue: "name"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeNum,
                W3Const.w3ApiDataValue: "budget"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeNum,
                W3Const.w3ApiDataValue: "balance"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
                W3Const.w3ApiDataValue: "note"
            }]
        },
        W3Const.w3ApiHandler: "EJGetFinanceEvent"
    },

    "aidAddBill": {
        W3Const.w3ElementType: W3Const.w3TypeApi,
        W3Const.w3ApiName: "addbill",
        W3Const.w3ApiParams: [
        {
            W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
            W3Const.w3ApiDataValue: "owner"
        },
        {
            W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
            W3Const.w3ApiDataValue: "datetime"
        },
        {
            W3Const.w3ApiDataType: W3Const.w3ApiDataTypeNum,
            W3Const.w3ApiDataValue: "amount"
        },
        {
            W3Const.w3ApiDataType: W3Const.w3ApiDataTypeNum,
            W3Const.w3ApiDataValue: "currency"
        },
        {
            W3Const.w3ApiDataType: W3Const.w3ApiDataTypeNum,
            W3Const.w3ApiDataValue: "category"
        },
        {
            W3Const.w3ApiDataType: W3Const.w3ApiDataTypeNum,
            W3Const.w3ApiDataValue: "paymentmode"
        },
        {
            W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
            W3Const.w3ApiDataValue: "note"
        },
        {
            W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
            W3Const.w3ApiDataValue: "event"
        }],
        W3Const.w3ApiResult: {
            W3Const.w3ApiResultStatus: [
                W3Const.w3ApiResultSuccessful,
                W3Const.w3ApiResultFailed
            ]
        },
        W3Const.w3ApiHandler: "EJAddBill"
    },

    "aidAddDebt": {
        W3Const.w3ElementType: W3Const.w3TypeApi,
        W3Const.w3ApiName: "adddebt",
        W3Const.w3ApiParams: [
        {
            W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
            W3Const.w3ApiDataValue: "start"
        },
        {
            W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
            W3Const.w3ApiDataValue: "end"
        },
        {
            W3Const.w3ApiDataType: W3Const.w3ApiDataTypeNum,
            W3Const.w3ApiDataValue: "amount"
        },
        {
            W3Const.w3ApiDataType: W3Const.w3ApiDataTypeNum,
            W3Const.w3ApiDataValue: "balance"
        },
        {
            W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
            W3Const.w3ApiDataValue: "note"
        }],
        W3Const.w3ApiResult: {
            W3Const.w3ApiResultStatus: [
                W3Const.w3ApiResultSuccessful,
                W3Const.w3ApiResultFailed
            ]
        },
        W3Const.w3ApiHandler: "EJAddDebt"
    },

    "aidAddIncome": {
        W3Const.w3ElementType: W3Const.w3TypeApi,
        W3Const.w3ApiName: "addincome",
        W3Const.w3ApiParams: [
        {
            W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
            W3Const.w3ApiDataValue: "owner"
        },
        {
            W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
            W3Const.w3ApiDataValue: "datetime"
        },
        {
            W3Const.w3ApiDataType: W3Const.w3ApiDataTypeNum,
            W3Const.w3ApiDataValue: "amount"
        },
        {
            W3Const.w3ApiDataType: W3Const.w3ApiDataTypeNum,
            W3Const.w3ApiDataValue: "currency"
        },
        {
            W3Const.w3ApiDataType: W3Const.w3ApiDataTypeNum,
            W3Const.w3ApiDataValue: "category"
        },
        {
            W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
            W3Const.w3ApiDataValue: "note"
        }],
        W3Const.w3ApiResult: {
            W3Const.w3ApiResultStatus: [
                W3Const.w3ApiResultSuccessful,
                W3Const.w3ApiResultFailed
            ]
        },
        W3Const.w3ApiHandler: "EJAddIncome"
    },

    "aidAddFinanceEvent": {
        W3Const.w3ElementType: W3Const.w3TypeApi,
        W3Const.w3ApiName: "addfinanceevent",
        W3Const.w3ApiParams: [
        {
            W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
            W3Const.w3ApiDataValue: "name"
        },
        {
            W3Const.w3ApiDataType: W3Const.w3ApiDataTypeNum,
            W3Const.w3ApiDataValue: "budget"
        },
        {
            W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
            W3Const.w3ApiDataValue: "note"
        }],
        W3Const.w3ApiResult: {
            W3Const.w3ApiResultStatus: [
                W3Const.w3ApiResultSuccessful,
                W3Const.w3ApiResultFailed
            ]
        },
        W3Const.w3ApiHandler: "EJAddFinanceEvent"
    },

    "aidExchangeRate": {
        W3Const.w3ElementType: W3Const.w3TypeApi,
        W3Const.w3ApiName: "exchangerate",
        W3Const.w3ApiParams: [
        {
            W3Const.w3ApiDataType: W3Const.w3ApiDataTypeNum,
            W3Const.w3ApiDataValue: "currencyid"
        },
        {
            W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
            W3Const.w3ApiDataValue: "date"
        }],
        W3Const.w3ApiResult: {
            W3Const.w3ApiResultStatus: [
                W3Const.w3ApiResultSuccessful,
                W3Const.w3ApiResultFailed
            ],
            W3Const.w3ApiResultData: [
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeNum,
                W3Const.w3ApiDataValue: "rate"
            }]
        },
        W3Const.w3ApiHandler: "EJGetExchangeRate"
    },

    "aidLogin": {
        W3Const.w3ElementType: W3Const.w3TypeApi,
        W3Const.w3ApiName: "login",
        W3Const.w3ApiParams: [
        {
            W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
            W3Const.w3ApiDataValue: "username"
        },
        {
            W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
            W3Const.w3ApiDataValue: "password"
        }],
        W3Const.w3ApiResult: {
            W3Const.w3ApiResultStatus: [
                W3Const.w3ApiResultSuccessful,
                W3Const.w3ApiResultFailed
            ],
            W3Const.w3ApiResultData: [
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeNum,
                W3Const.w3ApiDataValue: "session"
            }]
        },
        W3Const.w3ApiHandler: "EJLogin"
    }
}
