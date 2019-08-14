
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
var _journeyDisplayFunc = null;
var _selectedJourneyID = null;

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
                    pin = new Microsoft.Maps.Pushpin(r.results[i].location,
                                                     {
                                                         text: i + 1 + '',
                                                         title: r.results[i].name
                                                     });
                    pins.push(pin);
                    locs.push(r.results[i].location);

                    Microsoft.Maps.Events.addHandler(pin, 'click', function (e) {
                        EJOnSearchPlaceSelected(e);
                    });

                    W3LogDebug("Search Reult: " + i);
                    W3LogDebug("Place: " + r.results[i].name);
                    W3LogDebug("Location: " + r.results[i].location);
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

    _journeyDisplayFunc = function (places) {
        mapObj.entities.clear();

        var pins = [];
        var locs = [];

        for (var i = 0; i < places.length; ++i) {
            var location = new Microsoft.Maps.Location(places[i]["latitude"], places[i]["longitude"]);
            var pin = new Microsoft.Maps.Pushpin(location,
                                                 {
                                                     text: i + 1 + '',
                                                     title: places[i]["name"],
                                                     subTitle: places[i]["remark"] + "___" + places[i]["note"]
                                                 });
            pins.push(pin);
            locs.push(location);
        }

        mapObj.entities.push(pins);

        var bounds = Microsoft.Maps.LocationRect.fromLocations(locs);
        mapObj.setView({ bounds: bounds });
    };
}

function EJMapSearch(uidInput)
{
    if (_searchFunc != null) {
        var address = W3GetUIText(uidInput);
        _searchFunc(address);
    }
}

function EJGenerateJourneyCheckboxID(uidTable, rowIndex)
{
    return uidTable + "CheckBox" + rowIndex;
}

function EJGenerateJourneyCellID(uidTable, rowIndex, column)
{
    return uidTable + "" + rowIndex + "" + column;
}

function EJFillSelectedJourney(selectedJourney)
{
    W3SetUIText("uidSelectedJourneyName", selectedJourney[0]);
    W3SetUIText("uidSelectedJourneyDatetime", selectedJourney[1]);
    W3SetUIText("uidSelectedJourneyTraveler", selectedJourney[2]);
    W3SetUIText("uidSelectedJourneyID", selectedJourney[3]);
}

function EJOnJourneySelected(uidTable, rowIndex)
{
    var uidCheckBox = EJGenerateJourneyCheckboxID(uidTable, rowIndex);

    if (!$("#" + uidCheckBox).is(":checked")) {
        W3DisableUI("uidJourneyGotoMapButton");
        W3HideUI("uidSelectedJourneyPanel");
        W3HideUI("uidSelectedPlacePanel");
        _selectedJourneyID = null;
        return;
    }

    var selectedJourney = [];
    selectedJourney.push(W3GetUIText(EJGenerateJourneyCellID(uidTable, rowIndex, 1)));
    selectedJourney.push(W3GetUIText(EJGenerateJourneyCellID(uidTable, rowIndex, 2)));
    selectedJourney.push(W3GetUIText(EJGenerateJourneyCellID(uidTable, rowIndex, 3)));
    selectedJourney.push(W3GetUIText(EJGenerateJourneyCellID(uidTable, rowIndex, 7)));

    $("table#" + uidTable + " [type='checkbox']").each(function (index) {
        if (rowIndex != index) {
            $(this).attr("checked", false);
        } else if (rowIndex == index) {
            W3EnableUI("uidJourneyGotoMapButton");
            EJFillSelectedJourney(selectedJourney);
            W3DisplayUI("uidSelectedJourneyPanel");
            _selectedJourneyID = selectedJourney[3];
        }
    });
}

function EJCreateJourneySelectBox(uidTable, rowIndex)
{
    var uid = EJGenerateJourneyCheckboxID(uidTable, rowIndex);
    return "<input id=\"" + uid + "\" type='checkbox' onclick=\"EJOnJourneySelected('" + uidTable + "'," + rowIndex + ")\">";
}

function EJDisplaySelectedJourneyOnMap()
{
    $("table#uidJourneyTable [type='checkbox']").each(function (index) {
        if (!$(this).is(":checked")) {
            return;
        }

        $("#uidJourneyTabHeader2").click();
        EJFreshJourney(_selectedJourneyID);
    });
}

function EJDisplayCurrentJourneyOnMap()
{
    EJFreshJourney(_selectedJourneyID);
}

function EJFreshJourney(journeyID)
{
    W3HideUI("uidSelectedPlacePanel");

    if (journeyID == null) {
        return;
    }

    var aid = "aidJourneyPlace";
    var session = W3GetSession();
    var request = W3CreateAPI(aid, String(journeyID), session);
    if (request == "") {
	alert("Failed to create get journey place request");
	return;
    }

    W3CallAPIAsync(request, function(data, status) {
	var result = eval("(" + data + ")");
	if (result[w3ApiResultStatus] != w3ApiResultSuccessful) {
	    W3LogWarning("Get journey place failed!");
	    alert("Get journey place failed!");
	    return;
	}

        if (_journeyDisplayFunc != null) {
            _journeyDisplayFunc(result[w3ApiResultData]);
        }
    });
}

function EJOnSearchPlaceSelected(e)
{
    if (_selectedJourneyID == null) {
        return;
    }

    W3DisplayUI("uidSelectedPlacePanel");

    W3SetUIText("uidMapPlaceName", e.target.getTitle());
    W3SetUIText("uidMapPlaceLatitude", e.target.getLocation().latitude);
    W3SetUIText("uidMapPlaceLongitude", e.target.getLocation().longitude);
}
