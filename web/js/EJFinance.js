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
