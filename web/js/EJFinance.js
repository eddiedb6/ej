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

	// TODO
	
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
	    w3Lan[W3GetLanguage()]["sidTableBillcategory1"],
            w3Lan[W3GetLanguage()]["sidTableBillcategory2"],
	    w3Lan[W3GetLanguage()]["sidTableBillcategory3"],
            w3Lan[W3GetLanguage()]["sidTableBillcategory4"],
            w3Lan[W3GetLanguage()]["sidTableBillcategory6"],
            w3Lan[W3GetLanguage()]["sidTableBillcategory7"],
            w3Lan[W3GetLanguage()]["sidTableBillcategory8"],
            w3Lan[W3GetLanguage()]["sidTableBillcategory9"],
            w3Lan[W3GetLanguage()]["sidTableBillcategory10"],
            w3Lan[W3GetLanguage()]["sidTableBillcategory11"],
            w3Lan[W3GetLanguage()]["sidTableBillcategory12"],
            w3Lan[W3GetLanguage()]["sidTableBillcategory13"],
            w3Lan[W3GetLanguage()]["sidTableBillcategory17"],
            w3Lan[W3GetLanguage()]["sidOther"]
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

	var textScene = [
	    w3Lan[W3GetLanguage()]["sidTableBillscene1"],
            w3Lan[W3GetLanguage()]["sidTableBillscene2"],
            w3Lan[W3GetLanguage()]["sidTableBillscene3"],
            w3Lan[W3GetLanguage()]["sidTableBillscene4"],
            w3Lan[W3GetLanguage()]["sidTableBillscene5"],
            w3Lan[W3GetLanguage()]["sidTableBillscene6"],
            w3Lan[W3GetLanguage()]["sidTableBillscene7"],
            w3Lan[W3GetLanguage()]["sidTableBillscene8"],
            w3Lan[W3GetLanguage()]["sidTableBillscene9"],
            w3Lan[W3GetLanguage()]["sidTableBillscene10"],
            w3Lan[W3GetLanguage()]["sidTableBillscene11"],
            w3Lan[W3GetLanguage()]["sidTableBillscene12"],
            w3Lan[W3GetLanguage()]["sidTableBillscene13"],
            w3Lan[W3GetLanguage()]["sidTableBillscene14"],
            w3Lan[W3GetLanguage()]["sidTableBillscene15"],
            w3Lan[W3GetLanguage()]["sidTableBillscene16"],
            w3Lan[W3GetLanguage()]["sidTableBillscene17"],
            w3Lan[W3GetLanguage()]["sidTableBillscene18"],
            w3Lan[W3GetLanguage()]["sidTableBillscene19"],
            w3Lan[W3GetLanguage()]["sidOther"]
	];

	// Draw scene
	var dataScene = [];
	var scenePercentage = report["scene"].split(separater);
	for (var i = 0; i < scenePercentage.length; ++i) {
	    dataScene.push((parseInt(scenePercentage[i]) / 10000).toFixed(4))
	}
    	$("#uidFinanceSceneReportPanel").empty();
	$("#uidFinanceSceneReportPanel").append(W3CreateCanvas("uidFinanceSceneReportCanvas"));
	W3DrawPercentageReport("uidFinanceSceneReportCanvas", dataScene, textScene, 5);

	// Draw scene year
	dataScene = [];
	scenePercentage = report["sceneyear"].split(separater);
	for (var i = 0; i < scenePercentage.length; ++i) {
	    dataScene.push((parseInt(scenePercentage[i]) / 10000).toFixed(4))
	}
    	$("#uidFinanceSceneYearReportPanel").empty();
	$("#uidFinanceSceneYearReportPanel").append(W3CreateCanvas("uidFinanceSceneYearReportCanvas"));
	W3DrawPercentageReport("uidFinanceSceneYearReportCanvas", dataScene, textScene, 5);

	var textPayment = [
	    w3Lan[W3GetLanguage()]["sidTablePaymentmode1"],
            w3Lan[W3GetLanguage()]["sidTablePaymentmode2"],
	    w3Lan[W3GetLanguage()]["sidTablePaymentmode3"],
            w3Lan[W3GetLanguage()]["sidTablePaymentmode4"],
            w3Lan[W3GetLanguage()]["sidOther"]
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

