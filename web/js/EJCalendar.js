
//
// Calculate calendar panel width
//

$(window).load(function() {
    var naviID = "#uidNavigation";
    var calendarID = "#uidPageCalendar";
    var screenWidth = $(window).width();
    var naviWidth = $(naviID).width();
    var calendarWidth = screenWidth - naviWidth - 50;
    
    $(calendarID).css("max-width", calendarWidth);
});

