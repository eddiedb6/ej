
var _htmlMark = "*";
var _pdfMark = "#";
var _htmlType = 1;
var _pdfType = 2;

function EJCreateNoteLink(processorParam) {
    var title = decodeURI(processorParam[0]);
    var rowIndex = processorParam[2][0];
    var columnIndex = processorParam[2][1];
    var uidCell = "uidNoteListTable" + String(rowIndex) + String(columnIndex - 1);
    var uiHTML = "<a onclick=\"EJOnNoteClicked('" + uidCell + "')\" href='javascript:' void(0);=''>" + title + "</a>"
    return [uiHTML, processorParam[1], processorParam[2]];
}

function EJMarkNote(uidCell, markChar) {
    $("#uidNoteListTable").find("tr").each(function() {
	var tdAttr = $(this).children();
	var uid = tdAttr.eq(1).attr("id");
	if (uidCell == uid) {
	    tdAttr.eq(0).text(markChar);
	} else {
	    tdAttr.eq(0).text("");
	}
    });
}

function EJGetSelectedNoteID() {
    var id = "";
    $("#uidNoteListTable").find("tr").each(function() {
	var tdAttr = $(this).children();
	if ((tdAttr.eq(0).text() == _htmlMark) || (tdAttr.eq(0).text() == _pdfMark)) {
	    id = tdAttr.eq(1).text();
	} 
    });

    return id;
}

function EJGetSelectedNoteType() {
    var type = 0;
    $("#uidNoteListTable").find("tr").each(function() {
	var tdAttr = $(this).children();
	if (tdAttr.eq(0).text() == _htmlMark) {
	    type = _htmlType;
	} else if (tdAttr.eq(0).text() == _pdfMark) {
            type = _pdfType;
        }
    });

    return type;
}

function EJDisplayHTMLNote(note) {
    W3DisplayUI("uidNoteHTMLContent");
    W3HideUI("uidNotePDFContent");
    W3SetUIText("uidNoteHTMLContent", note);
}

function EJDisplayPDFLNote(note, error, id) {
    W3DisplayUI("uidNotePDFContent");
    W3HideUI("uidNoteHTMLContent");
    W3SetUIText("uidNotePDFCanvas", note);
    $("#uidNotePDFCanvas").W3DisplayPDF(id, error);
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
        var apiResultData = apiDef[w3ApiResult][w3ApiResultData];
        var title = result[w3ApiResultData][apiResultData[0][w3ApiDataValue]];
        var tag = result[w3ApiResultData][apiResultData[1][w3ApiDataValue]]
        var type = result[w3ApiResultData][apiResultData[2][w3ApiDataValue]];
        var note = result[w3ApiResultData][apiResultData[3][w3ApiDataValue]];
        var error = result[w3ApiResultData][apiResultData[4][w3ApiDataValue]];

	title = decodeURI(title);
	W3SetUIText("uidNoteContentTitleLabel", title);

        var markChar = "";
        if (type == _htmlType) {
            EJDisplayHTMLNote(note);
            markChar = _htmlMark;
        } else if (type == _pdfType) {
            EJDisplayPDFLNote(note, error, idNote);
            markChar = _pdfMark;
        } else {
            W3LogError("Unknown note type: " + type);
            return;
        }

        W3EnableUI("uidNoteEditButton");
        EJMarkNote(uidCell, markChar);
    });
}

function EJInitHTMLEditor() {
    var note = W3GetUIText("uidNoteHTMLContent");
    W3SetUIText("uidNoteHTMLEditor", note);

    W3DisplayUI("uidNoteHTMLEditorWrapper");
    W3DisplayUI("uidNoteHTMLSaveButton");
    W3HideUI("uidNotePDFEditor");
    W3HideUI("uidNotePDFSaveButton");
}

function EJInitPDFEditor() {
    var note = W3GetUIText("uidNotePDFCanvas");
    W3SetUIText("uidNotePDFEditor", note);

    W3DisplayUI("uidNotePDFEditor");
    W3DisplayUI("uidNotePDFSaveButton");
    W3HideUI("uidNoteHTMLEditorWrapper");
    W3HideUI("uidNoteHTMLSaveButton");
}

function EJEditNote() {
    var id = EJGetSelectedNoteID();
    if (id == "") {
	W3LogError("No note selected yet");
	return;
    }

    W3SetUIText("uidNoteEditID", id);

    var type = EJGetSelectedNoteType();
    if (type == _htmlType) {
        EJInitHTMLEditor();
    } else if (type == _pdfType) {
        EJInitPDFEditor();
    }
}

function EJGotoNotePage(data, status) {
    W3OnAPIDefaultListener(data, status);
    
    var pageRequest = W3CreateAPI("aidPage", "uidPageNote");
    if (pageRequest == "") {
	alert("Create note page request failed!");
	return;
    }
    W3CallAPI(pageRequest);
}

function EJInitHTMLAdd() {
    W3DisplayUI("uidNoteAddHTMLWrapper");
    W3DisplayUI("uidNoteAddSubmitHTML");
    W3HideUI("uidNoteAddPDF");
    W3HideUI("uidNoteAddSubmitPDF");
}

function EJInitPDFAdd() {
    W3DisplayUI("uidNoteAddPDF");
    W3DisplayUI("uidNoteAddSubmitPDF");
    W3HideUI("uidNoteAddHTMLWrapper");
    W3HideUI("uidNoteAddSubmitHTML");
}

function EJOnNoteTypeChange() {
    var type = W3GetUIText("uidNoteAddType");

    if (type == _htmlType) {
        EJInitHTMLAdd();
    } else if (type == _pdfType) {
        EJInitPDFAdd();
    } else {
        W3LogError("Unknown note type selected: " + type);
    }
}
