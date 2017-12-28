//
// Processor
//

function EJCalcBillTotalAmount(paramArray) {
    return EJCalcCurrencyAmount(paramArray, billTotalAmount);
}

function EJCalcIncomeTotalAmount(paramArray) {
    return EJCalcCurrencyAmount(paramArray, incomeTotalAmount);
}

function EJGenerateCategoryDrawFunc(paramArray) {
    var categoryString = paramArray[0];
    var drawFunc = "EJDrawCategoryReport(w3PlaceHolder_1, " + categoryString + ")";
    return [drawFunc, paramArray[1]];
}

function EJGeneratePaymentmodeDrawFunc(paramArray) {
    var paymentmodeString = paramArray[0];
    var drawFunc = "EJDrawPaymentmodeReport(w3PlaceHolder_1, " + paymentmodeString + ")";
    return [drawFunc, paramArray[1]];
}

// Exchange Rate
function EJGetExchangeRate(date, currency) {
    var aid = "aidExchangeRate";
    var apiDef = W3GetAPIDef(aid);
    if (apiDef == null) {
	return 0;
    }
    
    var api = apiDef[w3ApiName];
    api += "?";
    api += apiDef[w3ApiParams][0][w3ApiDataValue] + "=" + currency;
    api += "&";
    api += apiDef[w3ApiParams][1][w3ApiDataValue] + "=" + date;

    var rate = 0;

    // Need sync but not async
    W3CallAPISync(api, function(data) {
	W3LogDebug("data: " + data);

	var apiResult = eval("(" + data + ")");
	var resultStatus = apiResult[w3ApiResultStatus];
	var resultData = apiResult[w3ApiResultData];

	if (resultStatus != w3ApiResultFailed) {
	    rate = parseFloat(resultData);
	}
    });

    return rate;
}
