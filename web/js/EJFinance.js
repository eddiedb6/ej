function EJGetFinanceReport(uid) {
    var request = W3CreateAPI(uid);
    if (request == "") {
	W3LogError("Failed to create finance report request");
	return;
    }

    W3LogDebug("Get finance report: " + request);
    
    $.get(request, function(data, status) {
	W3LogDebug(data);
	var report = eval("(" + data + ")")[w3ApiResultData];
	$("#uidFinanceReportIncomeValue").text(report["income"].toFixed(2).toString());
	$("#uidFinanceReportDepositValue").text(report["deposit"].toFixed(2).toString());
	$("#uidFinanceReportDebtValue").text(report["debt"].toFixed(2).toString());
	$("#uidFinanceReportConsumeValue").text(report["consume"].toFixed(2).toString());
	$("#uidFinanceReportBalanceValue").text(report["balance"].toFixed(2).toString());
	$("#uidFinanceReportIncomeYearValue").text(report["incomeyear"].toFixed(2).toString());
	$("#uidFinanceReportDepositYearValue").text(report["deposityear"].toFixed(2).toString());
	$("#uidFinanceReportDebtYearValue").text(report["debtyear"].toFixed(2).toString());
	$("#uidFinanceReportConsumeYearValue").text(report["consumeyear"].toFixed(2).toString());
	$("#uidFinanceReportBalanceYearValue").text(report["balanceyear"].toFixed(2).toString());

	if (report["balanceyear"] >= 0) {
	    $("#uidFinanceReportBalanceYearValue").css("color", "green");
	} else {
	    $("#uidFinanceReportBalanceYearValue").css("color", "red");
	}
	
	if (report["balance"] >= 0) {
	    $("#uidFinanceReportBalanceValue").css("color", "green");
	} else {
	    $("#uidFinanceReportBalanceValue").css("color", "red");
	}

	var separater = "_";
	
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

	// Draw category
	var dataCategory = [];
	var categoryPercentage = report["category"].split(separater);
	for (var i = 0; i < categoryPercentage.length; ++i) {
	    dataCategory.push((parseInt(categoryPercentage[i]) / 10000).toFixed(4))
	}
	$("#uidFinanceCategoryReportPanel").empty();
	$("#uidFinanceCategoryReportPanel").append(W3CreateCanvas("uidFinanceCategoryReportCanvas"));
	W3DrawPercentageReport("uidFinanceCategoryReportCanvas", dataCategory, textCategory, 5);

	// Draw category year
	dataCategory = [];
	categoryPercentage = report["categoryyear"].split(separater);
	for (var i = 0; i < categoryPercentage.length; ++i) {
	    dataCategory.push((parseInt(categoryPercentage[i]) / 10000).toFixed(4))
	}
    	$("#uidFinanceCategoryYearReportPanel").empty();
	$("#uidFinanceCategoryYearReportPanel").append(W3CreateCanvas("uidFinanceCategoryYearReportCanvas"));
	W3DrawPercentageReport("uidFinanceCategoryYearReportCanvas", dataCategory, textCategory, 5);

	var textPayment = [
	    W3GetStringValue("sidTablePaymentMode1"),
            W3GetStringValue("sidTablePaymentMode2"),
	    W3GetStringValue("sidTablePaymentMode3"),
            W3GetStringValue("sidTablePaymentMode4"),
            W3GetStringValue("sidOther")
	];

	// Draw paymentmode 
	var dataPayment = [];
	var paymentPercentage = report["paymentmode"].split(separater);
	for (var i = 0; i < paymentPercentage.length; ++i) {
	    dataPayment.push((parseInt(paymentPercentage[i]) / 10000).toFixed(4))
	}
    	$("#uidFinancePaymentmodeReportPanel").empty();
	$("#uidFinancePaymentmodeReportPanel").append(W3CreateCanvas("uidFinancePaymentmodeReportCanvas"));
	W3DrawPercentageReport("uidFinancePaymentmodeReportCanvas", dataPayment, textPayment, 5);

	// Draw paymentmode year
	dataPayment = [];
	paymentPercentage = report["paymentmodeyear"].split(separater);
	for (var i = 0; i < paymentPercentage.length; ++i) {
	    dataPayment.push((parseInt(paymentPercentage[i]) / 10000).toFixed(4))
	}
    	$("#uidFinancePaymentmodeYearReportPanel").empty();
	$("#uidFinancePaymentmodeYearReportPanel").append(W3CreateCanvas("uidFinancePaymentmodeYearReportCanvas"));
	W3DrawPercentageReport("uidFinancePaymentmodeYearReportCanvas", dataPayment, textPayment, 5);
    });
}

