function EJOnNoteClicked(idTag, idNote) {
    var title = "Title" + idTag + idNote;
    var note = "Body" + idTag + idNote + "Body";

    $("#uidNoteContentTitle" + idTag).html("<b>" + title + "</b>");
    $("#uidNoteContentBody" + idTag).html("<b>" + note + "</b>");
}
