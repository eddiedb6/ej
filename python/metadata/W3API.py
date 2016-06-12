import sys
sys.path.append("..")
import W3Const

w3API = {
    ###################################
    # User data should be added below #
    ###################################

    "aidPage": {
        W3Const.w3ApiName: "page",
        W3Const.w3ApiParam1: [W3Const.w3ApiValueTypeNum, "id"]
    },
    
    "aidBill": {
        W3Const.w3ApiName: "bill",
        W3Const.w3ApiParam1: [W3Const.w3ApiValueTypeString, "from"],
        W3Const.w3ApiParam2: [W3Const.w3ApiValueTypeString,"to"],
        W3Const.w3ApiResult: {
            W3Const.w3ApiResultStatus: [
                W3Const.w3ApiResultSuccessful,
                W3Const.w3ApiResultFailed
            ],
            W3Const.w3ApiResultData: [
                [W3Const.w3ApiValueTypeString, "owner"],
                [W3Const.w3ApiValueTypeString, "datetime"],
                [W3Const.w3ApiValueTypeNum, "amount"],
                [W3Const.w3ApiValueTypeNum, "currency"],
                [W3Const.w3ApiValueTypeNum, "category"],
                [W3Const.w3ApiValueTypeNum, "scene"],
                [W3Const.w3ApiValueTypeNum, "paymentmode"],
                [W3Const.w3ApiValueTypeString, "note"]
            ]
        }
    },

    "aidDebt": {
        W3Const.w3ApiName: "debt",
        W3Const.w3ApiParam1: [W3Const.w3ApiValueTypeString, "from"],
        W3Const.w3ApiParam2: [W3Const.w3ApiValueTypeString, "to"],
        W3Const.w3ApiResult: {
            W3Const.w3ApiResultStatus: [
                W3Const.w3ApiResultSuccessful,
                W3Const.w3ApiResultFailed
            ],
            W3Const.w3ApiResultData: [
                [W3Const.w3ApiValueTypeString, "start"],
                [W3Const.w3ApiValueTypeString, "end"],
                [W3Const.w3ApiValueTypeNum, "amount"],
                [W3Const.w3ApiValueTypeNum, "balance"],
                [W3Const.w3ApiValueTypeString, "note"]
            ]
        }
    },
    
    "aidIncome": {
        W3Const.w3ApiName: "income",
        W3Const.w3ApiParam1: [W3Const.w3ApiValueTypeString, "from"],
        W3Const.w3ApiParam2: [W3Const.w3ApiValueTypeString, "to"],
        W3Const.w3ApiResult: {
            W3Const.w3ApiResultStatus: [
                W3Const.w3ApiResultSuccessful,
                W3Const.w3ApiResultFailed
            ],
            W3Const.w3ApiResultData: [
                [W3Const.w3ApiValueTypeString, "owner"],
                [W3Const.w3ApiValueTypeString, "datetime"],
                [W3Const.w3ApiValueTypeNum, "amount"],
                [W3Const.w3ApiValueTypeNum, "currency"],
                [W3Const.w3ApiValueTypeNum, "category"],
                [W3Const.w3ApiValueTypeString, "note"]
            ]
        }
    },

    "aidFinanceReport": {
        W3Const.w3ApiName: "financereport",
        W3Const.w3ApiParam1: [W3Const.w3ApiValueTypeString, "month"],
        W3Const.w3ApiResult: {
            W3Const.w3ApiResultStatus: [
                W3Const.w3ApiResultSuccessful,
                W3Const.w3ApiResultFailed
            ],
            W3Const.w3ApiResultData: [
                [W3Const.w3ApiValueTypeNum, "income"],
                [W3Const.w3ApiValueTypeNum, "deposit"],
                [W3Const.w3ApiValueTypeNum, "debt"],
                [W3Const.w3ApiValueTypeNum, "consume"],
                [W3Const.w3ApiValueTypeNum, "balance"],
                [W3Const.w3ApiValueTypeString, "category"],
                [W3Const.w3ApiValueTypeString, "scene"],
                [W3Const.w3ApiValueTypeString, "paymentmode"],
                [W3Const.w3ApiValueTypeNum, "incomeyear"],
                [W3Const.w3ApiValueTypeNum, "deposityear"],
                [W3Const.w3ApiValueTypeNum, "debtyear"],
                [W3Const.w3ApiValueTypeNum, "consumeyear"],
                [W3Const.w3ApiValueTypeNum, "balanceyear"],
                [W3Const.w3ApiValueTypeString, "categoryyear"],
                [W3Const.w3ApiValueTypeString, "sceneyear"],
                [W3Const.w3ApiValueTypeString, "paymentmodeyear"]
            ]
        }
    },

    "aidFinanceEvent": {
        W3Const.w3ApiName: "financeevent",
        W3Const.w3ApiParam1: [W3Const.w3ApiValueTypeString, "name"],
        W3Const.w3ApiResult: {
            W3Const.w3ApiResultStatus: [
                W3Const.w3ApiResultSuccessful,
                W3Const.w3ApiResultFailed
            ],
            W3Const.w3ApiResultData: [
                [W3Const.w3ApiValueTypeString, "name"],
                [W3Const.w3ApiValueTypeNum, "budget"],
                [W3Const.w3ApiValueTypeNum, "balance"],
                [W3Const.w3ApiValueTypeString, "note"] 
            ]
        }
    },

    "aidAddBill": {
        W3Const.w3ApiName: "addbill",
        W3Const.w3ApiParam1: [W3Const.w3ApiValueTypeString, "owner"],
        W3Const.w3ApiParam2: [W3Const.w3ApiValueTypeString, "datetime"],
        W3Const.w3ApiParam3: [W3Const.w3ApiValueTypeNum, "amount"],
        W3Const.w3ApiParam4: [W3Const.w3ApiValueTypeNum, "currency"],
        W3Const.w3ApiParam5: [W3Const.w3ApiValueTypeNum, "category"],
        W3Const.w3ApiParam6: [W3Const.w3ApiValueTypeNum, "scene"],
        W3Const.w3ApiParam7: [W3Const.w3ApiValueTypeNum, "paymentmode"],
        W3Const.w3ApiParam8: [W3Const.w3ApiValueTypeString, "note"],
        W3Const.w3ApiParam9: [W3Const.w3ApiValueTypeString, "event"],
        W3Const.w3ApiResult: {
            W3Const.w3ApiResultStatus: [
                W3Const.w3ApiResultSuccessful,
                W3Const.w3ApiResultFailed
            ]
        }
    },

    "aidAddDebt": {
        W3Const.w3ApiName: "adddebt",
        W3Const.w3ApiParam1: [W3Const.w3ApiValueTypeString, "start"],
        W3Const.w3ApiParam2: [W3Const.w3ApiValueTypeString, "end"],
        W3Const.w3ApiParam3: [W3Const.w3ApiValueTypeNum, "amount"],
        W3Const.w3ApiParam4: [W3Const.w3ApiValueTypeNum, "balance"],
        W3Const.w3ApiParam5: [W3Const.w3ApiValueTypeString, "note"],
        W3Const.w3ApiResult: {
            W3Const.w3ApiResultStatus: [
                W3Const.w3ApiResultSuccessful,
                W3Const.w3ApiResultFailed
            ]
        }
    },

    "aidAddIncome": {
        W3Const.w3ApiName: "addincome",
        W3Const.w3ApiParam1: [W3Const.w3ApiValueTypeString, "owner"],
        W3Const.w3ApiParam2: [W3Const.w3ApiValueTypeString, "datetime"],
        W3Const.w3ApiParam3: [W3Const.w3ApiValueTypeNum, "amount"],
        W3Const.w3ApiParam4: [W3Const.w3ApiValueTypeNum, "currency"],
        W3Const.w3ApiParam5: [W3Const.w3ApiValueTypeNum, "category"],
        W3Const.w3ApiParam6: [W3Const.w3ApiValueTypeString, "note"],
        W3Const.w3ApiResult: {
            W3Const.w3ApiResultStatus: [
                W3Const.w3ApiResultSuccessful,
                W3Const.w3ApiResultFailed
            ]
        }
    },

    "aidAddFinanceEvent": {
        W3Const.w3ApiName: "addfinanceevent",
        W3Const.w3ApiParam1: [W3Const.w3ApiValueTypeString, "name"],
        W3Const.w3ApiParam2: [W3Const.w3ApiValueTypeNum, "budget"],
        W3Const.w3ApiParam3: [W3Const.w3ApiValueTypeString, "note"],
        W3Const.w3ApiResult: {
            W3Const.w3ApiResultStatus: [
                W3Const.w3ApiResultSuccessful,
                W3Const.w3ApiResultFailed
            ]
        }
    }

    ###################################
    # User data should be added above #
    ###################################
}
