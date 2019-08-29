
//
// Calculate calendar panel width
//

$(window).load(function() {
    if (document.getElementById("uidCalendar") == null) {
        // Make sure calendar is loaded first
        return;
    }
    
    var calendarElement = $("#uidCalendar");
    var naviElement = $("#uidNavigation");
    if ((calendarElement == undefined) || (naviElement == undefined)) {
        return;
    }
    
    var screenWidth = $(window).width();
    var naviWidth = naviElement.width();
    var calendarWidth = screenWidth - naviWidth - 50;

    calendarElement.css("max-width", calendarWidth);
    calendarElement.W3CalendarEvent(EJUpdateMonthEvent);
});

function EJUpdateMonthEvent(year, month, calendarUpdater)
{
    var aid = "aidCalendarEvent";
    var session = W3GetSession();
    var calendarEventRequest = W3CreateAPI(aid, String(year) + "-" + String(month), session);
    if (calendarEventRequest == "") {
	alert("Failed to create calendar event request");
	return;
    }

    W3CallAPIAsync(calendarEventRequest, function(data, status) {
	var result = eval("(" + data + ")");
	if (result[w3ApiResultStatus] != w3ApiResultSuccessful) {
	    W3LogWarning("Get calendar event failed!");
	    alert("Get calendar event failed!");
	    return;
	}

        if (calendarUpdater != undefined) {
            calendarUpdater(result[w3ApiResultData]);
        }
    });
}

function EJGotoCalendarPage(data, status)
{
    W3OnAPIDefaultListener(data, status);

    var pageRequest = W3CreateAPI("aidPage", "uidPageCalendar");
    if (pageRequest == "") {
	alert("Create calendar page request failed!");
	return;
    }
    W3CallAPI(pageRequest);
}
