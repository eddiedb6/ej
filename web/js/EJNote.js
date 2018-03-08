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

	$("#uidNoteContentTitlePanel").html("<b>" + title + "</b>");
	$("#uidNoteContentBodyPanel").html("<p>" + note + "</p>");
    });
}

function EJEditCurrentNote() {
    W3HideUI("uidNoteContentBodyPanel");
    W3DisplayUI("uidNoteContentEditPanel");
}
