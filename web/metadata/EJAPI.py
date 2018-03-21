{
    ### Finance ###
    
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
        },
        {
            W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
            W3Const.w3ApiDataValue: "session"
        }],
        W3Const.w3ApiResult: {
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
        },
        {
            W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
            W3Const.w3ApiDataValue: "session"
        }],            
        W3Const.w3ApiResult: {
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
        },
        {
            W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
            W3Const.w3ApiDataValue: "session"
        }],
        W3Const.w3ApiResult: {
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
        },
        {
            W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
            W3Const.w3ApiDataValue: "session"
        }],            
        W3Const.w3ApiResult: {
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
        },
        {
            W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
            W3Const.w3ApiDataValue: "session"
        }],
        W3Const.w3ApiResult: {
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
        },
        {
            W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
            W3Const.w3ApiDataValue: "session"
        }],
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
        },
        {
            W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
            W3Const.w3ApiDataValue: "session"
        }],
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
        },
        {
            W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
            W3Const.w3ApiDataValue: "session"
        }],
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
        },
        {
            W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
            W3Const.w3ApiDataValue: "session"
        }],            
        W3Const.w3ApiHandler: "EJAddFinanceEvent"
    },

    ### Note ###

    "aidNote": {
        W3Const.w3ElementType: W3Const.w3TypeApi,
        W3Const.w3ApiName: "note",
        W3Const.w3ApiParams: [
        {
            W3Const.w3ApiDataType: W3Const.w3ApiDataTypeNum,
            W3Const.w3ApiDataValue: "id"
        },
        {
            W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
            W3Const.w3ApiDataValue: "session"
        }],
        W3Const.w3ApiResult: {
            W3Const.w3ApiResultData: [
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
                W3Const.w3ApiDataValue: "title"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeNum,
                W3Const.w3ApiDataValue: "tag"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
                W3Const.w3ApiDataValue: "note"
            }]
        },
        W3Const.w3ApiHandler: "EJGetNote"
    },

    "aidNoteTitle": {
        W3Const.w3ElementType: W3Const.w3TypeApi,
        W3Const.w3ApiName: "notetitle",
        W3Const.w3ApiParams: [
        {
            W3Const.w3ApiDataType: W3Const.w3ApiDataTypeNum,
            W3Const.w3ApiDataValue: "tag"
        },
        {
            W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
            W3Const.w3ApiDataValue: "session"
        }],
        W3Const.w3ApiResult: {
            W3Const.w3ApiResultData: [
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeNum,
                W3Const.w3ApiDataValue: "id"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
                W3Const.w3ApiDataValue: "title"
            }]
        },
        W3Const.w3ApiHandler: "EJGetNoteTitle"
    },

    "aidAddNote": {
        W3Const.w3ElementType: W3Const.w3TypeApi,
        W3Const.w3ApiName: "addnote",
        W3Const.w3ApiParams: [
        {
            W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
            W3Const.w3ApiDataValue: "title"
        },
        {
            W3Const.w3ApiDataType: W3Const.w3ApiDataTypeNum,
            W3Const.w3ApiDataValue: "tag"
        },
        {
            W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
            W3Const.w3ApiDataValue: "note"
        },
        {
            W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
            W3Const.w3ApiDataValue: "session"
        }],
        W3Const.w3ApiHandler: "EJAddNote",
        W3Const.w3ApiListener: [
            "EJGotoNotePage(w3PlaceHolder_1, w3PlaceHolder_2)"
        ]
    },

    "aidModifyNote": {
        W3Const.w3ElementType: W3Const.w3TypeApi,
        W3Const.w3ApiName: "modifynote",
        W3Const.w3ApiParams: [
        {
            W3Const.w3ApiDataType: W3Const.w3ApiDataTypeNum,
            W3Const.w3ApiDataValue: "id"
        },
        {
            W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
            W3Const.w3ApiDataValue: "note"
        },
        {
            W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
            W3Const.w3ApiDataValue: "session"
        }],
        W3Const.w3ApiHandler: "EJModifyNote",
        W3Const.w3ApiListener: [
            "EJGotoNotePage(w3PlaceHolder_1, w3PlaceHolder_2)"
        ]
    },

    ### Others ###

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
            W3Const.w3ApiResultData: [
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeNum,
                W3Const.w3ApiDataValue: "session"
            }]
        },
        W3Const.w3ApiHandler: "EJLogin"
    }
}
