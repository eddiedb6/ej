
//
// Calculate calendar panel width
//

$(window).load(function() {
    if (document.getElementById("uidMSMap") == null) {
        // Make map is loaded first
        return;
    }
    
    var mapElement = $("#uidMSMap");
    if (mapElement == undefined) {
        return;
    }

    var naviElement = $("#uidNavigation");
    if (naviElement != undefined) {          
        var screenWidth = $(window).width();
        var naviWidth = naviElement.width();
        var mapWidth = screenWidth - naviWidth - 160;
        if (mapWidth > 800) {
            mapElement.css("width", mapWidth);
            mapElement.css("height", mapWidth / 16 * 9);
        }
    }
});

function EJMapHandler(map)
{
    var bj = new Microsoft.Maps.Location(39.918794, 116.398568);
    var pinBJ = new Microsoft.Maps.Pushpin(bj, {
        title: 'China',
        subTitle: 'Beijing',
        text: '1'
    });

    var sh = new Microsoft.Maps.Location(30.918794, 121.398568);
    var pinSH = new Microsoft.Maps.Pushpin(sh, {
        title: 'China',
        subTitle: 'Shanghai',
        text: '2'
    });

    map.entities.push(pinBJ);
    map.entities.push(pinSH);
}
