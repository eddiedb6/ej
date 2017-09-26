//
// Processor
//

function EJCalcBillTotalAmount(paramArray) {
    var amount = paramArray[0];
    var totalAmount = W3GetVariable(billTotalAmount);
    
    totalAmount += parseFloat(amount);
    W3SetVariable(billTotalAmount, totalAmount);
    
    return paramArray;
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
