function EJUpdateBill(column, value, indexRow, countRow, indexColumn, countColumn, data) {
    var rowData = "";

    if (column == "datetime") {
	rowData += "<td>" + value.split(" ")[0] + "</td>";
    } else if (column == "currency" || column == "category" || column == "scene" || column == "paymentmode") {
	rowData += "<td>" + w3Lan[W3GetLanguage()][value] + "</td>";
    } else if (column == "amount") {
	if (indexRow == 0) {
	    data["total"] = 0.0;
	}
	rowData += "<td style='text-align:right'>" + value + "</td>";
	data["total"] += Number(value); // TODO, convert between different money required
	if (indexRow + 1 >= countRow) {
	    $("#uidBillTotalAmount").text(data["total"].toFixed(2).toString());
	}
    } else {
	rowData += "<td>" + value + "</td>";
    }

    return rowData;
}

function EJUpdateDebt(column, value, indexRow, countRow, indexColumn, countColumn, data) {
    var rowData = "";
    if (column == "start" || column == "end") {
	rowData += "<td>" + value.split(" ")[0] + "</td>";
    } else if (column == "amount" || column == "balance") {
	rowData += "<td style='text-align:right'>" + value + "</td>";
    } else {
	rowData += "<td>" + value + "</td>";
    }

    return rowData;
}

function EJUpdateFinanceEvent(column, value, indexRow, countRow, indexColumn, countColumn, data) {
    var rowData = "";
    if (column == "budget") {
	rowData += "<td style='text-align:right'>" + value + "</td>";
    } else if (column == "balance") {
	var css = "color:green";
	if (value < 0) {
	    css = "color:red";
	}

	// Round to 0.00 format
	var balance = parseFloat(value);
	
	rowData += "<td style='text-align:right;" + css + "'>" + balance.toFixed(2) + "</td>";
    } else {
	rowData += "<td>" + value + "</td>";
    }

    return rowData;
}

function EJUpdateIncome(column, value, indexRow, countRow, indexColumn, countColumn, data) {
    var rowData = "";
    if (column == "datetime") {
	rowData += "<td>" + value.split(" ")[0] + "</td>";
    } else if (column == "currency" || column == "category") {
	rowData += "<td>" + w3Lan[W3GetLanguage()][value] + "</td>";
    } else if (column == "amount") {
	if (indexRow == 0) {
	    data["total"] = 0.0;
	}
	rowData += "<td style='text-align:right'>" + value + "</td>";
	data["total"] += Number(value); // TODO, convert between different money required
	if (indexRow + 1 >= countRow) {
	    $("#uidIncomeTotalAmount").text(data["total"].toFixed(2).toString());
	}
    } else {
	rowData += "<td>" + value + "</td>";
    }
    
    return rowData;
}

function EJGetFinaceReport(uid) {
    var request = W3CreateAPI(uid);
    $.get(request, function(data, status) {
	var report = eval("(" + data + ")")[w3ApiResultData][0];
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

function EJAddBill() {
    $("#uidFinanceTabBillQueryPanel").css("display", "none");
    $("#uidFinanceTabBillAddPanel").css("display", "block");
}

function EJAddDebt() {
    $("#uidFinanceTabDebtQueryPanel").css("display", "none");
    $("#uidFinanceTabDebtAddPanel").css("display", "block");
}

function EJAddIncome() {
    $("#uidFinanceTabIncomeQueryPanel").css("display", "none");
    $("#uidFinanceTabIncomeAddPanel").css("display", "block");
}

function EJAddFinanceEvent() {
    $("#uidFinanceTabEventQueryPanel").css("display", "none");
    $("#uidFinanceTabEventAddPanel").css("display", "block");
}

function EJCancelBillAdd() {
    $("#uidFinanceTabBillQueryPanel").css("display", "block");
    $("#uidFinanceTabBillAddPanel").css("display", "none");
}

function EJCancelDebtAdd() {
    $("#uidFinanceTabDebtQueryPanel").css("display", "block");
    $("#uidFinanceTabDebtAddPanel").css("display", "none");
}

function EJCancelIncomeAdd() {
    $("#uidFinanceTabIncomeQueryPanel").css("display", "block");
    $("#uidFinanceTabIncomeAddPanel").css("display", "none");
}

function EJCancelFinanceEventAdd() {
    $("#uidFinanceTabEventQueryPanel").css("display", "block");
    $("#uidFinanceTabEventAddPanel").css("display", "none");
}
