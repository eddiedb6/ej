function EJHideNoteID(paramArray) {
    return [paramArray[0], {"display": "none", }, paramArray[2]];
}

function EJCreateNoteLink(paramArray) {
    var rowIndex = paramArray[2][0];
    var columnIndex = paramArray[2][1];
    var uidCell = "uidNoteListTable" + String(rowIndex) + String(columnIndex - 1);
    var uiHTML = "<a onclick=\"EJOnNoteClicked('" + uidCell + "')\" href='javascript:' void(0);=''>" + paramArray[0] + "</a>"
    return [uiHTML, paramArray[1], paramArray[2]];
}

function EJMarkNote(uidCell) {
    $("#uidNoteListTable").find("tr").each(function() {
	var tdAttr = $(this).children();
	var uid = tdAttr.eq(1).attr("id");
	if (uidCell == uid) {
	    tdAttr.eq(0).text("*");
	} else {
	    tdAttr.eq(0).text("");
	}
    });
}

function EJOnNoteClicked(uidCell) {
    var idNote = W3GetUIText(uidCell)
    var session = W3GetSession();
    var noteRequest = W3CreateAPI("aidNote", idNote, session);
    if (noteRequest == "") {
	alert("Failed to create note request");
	return;
    }

    W3CallAPIAsync(noteRequest, function(data, status) {
	var result = eval("(" + data + ")");
	if (result[w3ApiResultStatus] != w3ApiResultSuccessful) {
	    W3LogWarning("Get note failed!");
	    alert("Get note failed!");
	    return;
	}

	var apiDef = W3GetAPIDef("aidNote");
	var title = result[w3ApiResultData][apiDef[w3ApiResult][w3ApiResultData][0][w3ApiDataValue]];
	var tag = result[w3ApiResultData][apiDef[w3ApiResult][w3ApiResultData][1][w3ApiDataValue]];
	var note = result[w3ApiResultData][apiDef[w3ApiResult][w3ApiResultData][2][w3ApiDataValue]];

	W3SetUIText("uidNoteContentTitleLabel", title);
	W3SetUIText("uidNoteContentBodyPanel", note);
    });

    W3EnableUI("uidNoteEditButton");
    EJMarkNote(uidCell);
}

function EJEditNote() {
    var note = W3GetUIText("uidNoteContentBodyPanel");
    var title = W3GetUIText("uidNoteContentTitleLabel");

    W3SetUIText("uidNoteEditor", note);
    W3SetUIText("uidNoteEditTitle", title);
}

function EJSaveNote() {
    // Redirect to note page
}

function EJGotoNotePage() {
    var pageRequest = W3CreateAPI("aidPage", "uidPageNote");
    if (pageRequest == "") {
	alert("Create note page request failed!");
	return;
    }
    W3CallAPI(pageRequest);
}
