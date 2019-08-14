
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

var _searchFunc = null;

function EJMapHandler(map)
{
    if (map == null) {
        return;
    }

    var mapObj = map;
    var searchManager = null;

    function doSearch(address) {
        var searchRequest = {
            where: address,
            callback: function (r) {
                if (r == null || r.results == null || r.results.length <= 0) {
                    return;
                }

                var pin;
                var pins = [];
                var locs = [];

                for (var i = 0; i < r.results.length; ++i) {
                    pin = new Microsoft.Maps.Pushpin(r.results[i].location, { text: i + '' });
                    pins.push(pin);
                    locs.push(r.results[i].location);
                }

                mapObj.entities.push(pins);

                var bounds;
                if (r.results.length == 1) {
                    bounds = r.results[0].bestView;
                } else {
                    bounds = Microsoft.Maps.LocationRect.fromLocations(locs);
                }

                mapObj.setView({ bounds: bounds });
            },
            errorCallback: function (e) {
                alert("No map search results found.");
            }
        };

        searchManager.geocode(searchRequest);
    }

    _searchFunc = function (address) {
        if (searchManager == null) {
            Microsoft.Maps.loadModule("Microsoft.Maps.Search", function() {
                searchManager = new Microsoft.Maps.Search.SearchManager(mapObj);
                doSearch(address);
            });
        } else {
            mapObj.entities.clear();
            doSearch(address);
        }
    };
}

function EJMapSearch(uidInput)
{
    if (_searchFunc != null) {
        var address = W3GetUIText(uidInput);
        _searchFunc(address);
    }
}
