//
// Processor
//

function EJCalcBillTotalAmount(processorParam) {
    return EJCalcCurrencyAmount(processorParam, billTotalAmount);
}

function EJCalcIncomeTotalAmount(processorParam) {
    return EJCalcCurrencyAmount(processorParam, incomeTotalAmount);
}

function EJGenerateCategoryDrawFunc(processorParam) {
    var categoryString = processorParam[0];
    var drawFunc = "EJDrawCategoryReport(w3PlaceHolder_1, " + categoryString + ")";
    return [drawFunc, processorParam[1]];
}

function EJGeneratePaymentmodeDrawFunc(processorParam) {
    var paymentmodeString = processorParam[0];
    var drawFunc = "EJDrawPaymentmodeReport(w3PlaceHolder_1, " + paymentmodeString + ")";
    return [drawFunc, processorParam[1]];
}
