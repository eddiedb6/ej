//
// Processor
//

function EJCalcCurrencyAmount(paramArray, varAmount) {
    var amountWithCurrency = paramArray[0].split("|");
    var amount = amountWithCurrency[0];
    var currencyID = amountWithCurrency[1];
    var datetime = amountWithCurrency[2];

    // Remove currency and keep only amount
    paramArray[0] = amount;

    // Change to CNY if necessary
    var amountCNY = amount;
    var isToCalc = true;
    if (currencyID != "1") {
	var date = datetime.split(" ")[0];
	var rate = EJGetExchangeRate(date, currencyID);
	if (rate != 0) {
	    amountCNY = amount * rate;
	} else {
	    // Mark that the exchange failed
	    var css = paramArray[1];
	    css["color"] = "gray";
	    isToCalc = false;
	}
    }

    if (isToCalc) {
	var totalAmount = W3GetVariable(varAmount);
	totalAmount += parseFloat(amountCNY);
	W3SetVariable(varAmount, totalAmount);
    }

    return paramArray;
}

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

//
// Report Drawing
//

function EJDrawCategoryReport(uidCanvas, categoryString) {
    var textCategory = [
	W3GetStringValue("sidTableBillCategory1"),
        W3GetStringValue("sidTableBillCategory2"),
	W3GetStringValue("sidTableBillCategory3"),
        W3GetStringValue("sidTableBillCategory4"),
        W3GetStringValue("sidTableBillCategory6"),
        W3GetStringValue("sidTableBillCategory7"),
        W3GetStringValue("sidTableBillCategory8"),
        W3GetStringValue("sidTableBillCategory9"),
        W3GetStringValue("sidTableBillCategory10"),
        W3GetStringValue("sidTableBillCategory11"),
        W3GetStringValue("sidTableBillCategory12"),
        W3GetStringValue("sidTableBillCategory13"),
        W3GetStringValue("sidTableBillCategory17"),
        W3GetStringValue("sidOther")
    ];

    EJDrawFinanceReport(uidCanvas, categoryString, textCategory);    
}

function EJDrawPaymentmodeReport(uidCanvas, paymentmodeString) {
    var textPaymentmode = [
	W3GetStringValue("sidTablePaymentMode1"),
        W3GetStringValue("sidTablePaymentMode2"),
	W3GetStringValue("sidTablePaymentMode3"),
        W3GetStringValue("sidTablePaymentMode4"),
        W3GetStringValue("sidOther")
    ];

    EJDrawFinanceReport(uidCanvas, paymentmodeString, textPaymentmode);    
}

function EJDrawFinanceReport(uidCanvas, dataString, textArray) {
    var dataArray = dataString.split("_");
    if (dataArray.length != textArray.length) {
	W3LogError("Report data and text array do not match: " + uidCanvas);
	return;
    }
    if (dataArray.length <= 0) {
	W3LogWarning("Report has no data: " + uidCanvas);
	return;
    }
    
    for (var i = 0; i < dataArray.length; ++i) {
	dataArray[i] = (parseInt(dataArray[i]) / 10000).toFixed(4);
    }

    W3DrawPercentageReport(uidCanvas, dataArray, textArray, 5);
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
    W3LogDebug("Trigger API: " + api);
    $.ajax({
	type: "get",
	url: api,
	data: "",
	async: false,
	success: function(data) {
	    W3LogDebug("data: " + data);

	    var apiResult = eval("(" + data + ")");
	    var resultStatus = apiResult[w3ApiResultStatus];
	    var resultData = apiResult[w3ApiResultData];

	    if (resultStatus != w3ApiResultFailed) {
		W3LogDebug("TODL: " + resultData);
		//rate = parseFloat(resultData);
	    }
	}
    });

    return rate;
}
