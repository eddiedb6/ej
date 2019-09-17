
//
// Calculate calendar panel width
//

// Map Operation

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
var _allPlacesDisplayFunc = null;
var _allPOIsDisplayFunc = null;
var _mapCleanFunc = null;
var _mapResetFunc = null;

var _selectedJourneyID = null;

function EJMapHandler(map)
{
    if (map == null) {
        return;
    }

    var mapObj = map;
    var searchManager = null;

    var currentManualPlaceChar = 0;

    Microsoft.Maps.Events.addHandler(map, 'rightclick', onRightClick);

    function onRightClick(e)
    {
        var pin = new Microsoft.Maps.Pushpin(e.location,
                                             {
                                                 color: 'black',
                                                 text: String.fromCharCode(currentManualPlaceChar + 'A'.charCodeAt(0))
                                             });
        Microsoft.Maps.Events.addHandler(pin, 'click', function (e) {
            EJOnManualPlaceClicked(e);
        });

        mapObj.entities.push(pin);

        ++currentManualPlaceChar;
    }

    function displayAll(places, pinColor, withLine, lineColor, subtitleGenerator, clickHandler)
    {
        doDisplay(places, pinColor, withLine, lineColor, subtitleGenerator, clickHandler, true);
    }

    function displayInView(places, pinColor, withLine, lineColor, subtitleGenerator, clickHandler)
    {
        doDisplay(places, pinColor, withLine, lineColor, subtitleGenerator, clickHandler, false);
    }

    function isLocationInBounds(location, bounds)
    {
        if ((location.latitude < bounds.getNorth()) && location.latitude > bounds.getSouth()) {
            if ((location.longitude < bounds.getEast()) && (location.longitude > bounds.getWest())) {
                return true;
            }
        }

        return false;
    }

    function doDisplay(places, pinColor, withLine, lineColor, subtitleGenerator, clickHandler, resetView)
    {
        var pins = [];
        var locs = [];
        var lines = [];
        var previousCoord = null;

        var viewBounds = mapObj.getBounds();
        for (var i = 0; i < places.length; ++i) {
            var location = new Microsoft.Maps.Location(places[i]["latitude"], places[i]["longitude"]);
            var pin = new Microsoft.Maps.Pushpin(location,
                                                 {
                                                     color: pinColor,
                                                     text: i + 1 + '',
                                                     title: W3Decode(places[i]["name"]),
                                                     subTitle: subtitleGenerator(places[i])
                                                 });
            pin["AttrPlace"] = places[i];
            Microsoft.Maps.Events.addHandler(pin, 'click', clickHandler);

            locs.push(location);
            if (resetView || isLocationInBounds(location, viewBounds)) {
                pins.push(pin);
            }

            if (!withLine) {
                continue;
            }

            if (previousCoord == null) {
                previousCoord = location;
                continue;
            }

            var coords = [previousCoord, location];
            var line = new Microsoft.Maps.Polyline(coords,
                                                   {
                                                       strokeColor: lineColor,
                                                       strokeThickness: 3,
                                                       strokeDashArray: [4, 4]
                                                   });
            lines.push(line);
            previousCoord = location;
        }

        mapObj.entities.push(pins);
        if (withLine) {
            mapObj.entities.push(lines);
        }

        if (resetView)
        {
            var bounds = Microsoft.Maps.LocationRect.fromLocations(locs);
            mapObj.setView({ bounds: bounds });
        }
    };

    function doSearch(address)
    {
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
                        EJOnSearchPlaceClicked(e);
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
            doSearch(address);
        }
    };

    _journeyDisplayFunc = function (places) {
        displayAll(places, 'blue', true, 'red', EJGenerateRemarkString, EJOnJourneyPlaceClicked);
    };

    _allPlacesDisplayFunc = function (places) {
        displayInView(places, 'red', false, null, EJGenerateRemarkString, EJOnJourneyPlaceClicked);
    };

    _allPOIsDisplayFunc = function (pois) {
        displayAll(pois, 'green', false, null, function (p) { return ""; }, EJOnPOIClicked);
    };

    _mapCleanFunc = function () {
        mapObj.entities.clear();
        currentManualPlaceChar = 0;
    };

    _mapResetFunc = function() {
        if (_mapCleanFunc != null) {
            _mapCleanFunc();
        }

        var coordinate = ["31.230369567871094", "121.47370147705078"];
        var mapProp = W3TryGetUIProperty("uidMSMap", w3PropMap);
        if (mapProp != null && mapProp.hasOwnProperty(w3AttrMapLocation)) {
            coordinate = mapProp[w3AttrMapLocation];
        }

        var location = new Microsoft.Maps.Location(coordinate[0], coordinate[1]);
        mapObj.setView({ center: location, zoom: 15 });
    };
}

// Utility

function EJGenerateJourneyCheckboxID(uidTable, rowIndex)
{
    return uidTable + "CheckBox" + rowIndex;
}

function EJGenerateJourneyCellID(uidTable, rowIndex, column)
{
    return uidTable + "" + rowIndex + "" + column;
}

function EJGenerateRemarkString(place)
{
    var remark = place["remark"];
    if (remark < 1) {
        remark = 1;
    } else if (remark > 5) {
        remark = 5;
    }

    var result = "";
    for (var i = 0; i < remark; ++i) {
        result += "*";
    }

    return result;
}

// UI Utility

function EJFillSelectedJourney(selectedJourney)
{
    W3SetUIText("uidSelectedJourneyName", selectedJourney[0]);
    W3SetUIText("uidSelectedJourneyDatetime", selectedJourney[1]);
    W3SetUIText("uidSelectedJourneyTraveler", selectedJourney[2]);
    W3SetUIText("uidSelectedJourneyID", selectedJourney[3]);
}

function EJCleanPlaceDetail()
{
    W3SetUIText("uidMapPlaceDatetime", "");
    W3SetUIText("uidMapPlaceRemark", "");
    W3SetUIText("uidMapPlaceNote", "");
}

function EJFillManualPlaceDetail(manualEvent)
{
    W3SetUIText("uidMapPlaceName", "TBD");
    W3SetUIText("uidMapPlaceLatitude", manualEvent.location.latitude);
    W3SetUIText("uidMapPlaceLongitude", manualEvent.location.longitude);
}

function EJFillPlaceDetail(placePin)
{
    W3SetUIText("uidMapPlaceName", placePin.getTitle());
    W3SetUIText("uidMapPlaceLatitude", placePin.getLocation().latitude);
    W3SetUIText("uidMapPlaceLongitude", placePin.getLocation().longitude);

    if (!placePin.hasOwnProperty("AttrPlace")) {
        return;
    }

    if (placePin["AttrPlace"].hasOwnProperty("datetime")) {
        var date = placePin["AttrPlace"]["datetime"].split(" ", 1);
        W3SetUIText("uidMapPlaceDatetime", date);
    }
    if (placePin["AttrPlace"].hasOwnProperty("remark")) {
        W3SetUIText("uidMapPlaceRemark", EJGenerateRemarkString(placePin["AttrPlace"]));
    }
    if (placePin["AttrPlace"].hasOwnProperty("note")) {
        W3SetUIText("uidMapPlaceNote", placePin["AttrPlace"]["note"]);
    }
    if (placePin["AttrPlace"].hasOwnProperty("poiid")) {
        W3SetUIText("uidSelectedPOIID", placePin["AttrPlace"]["poiid"]);
    }
}

function EJCreateJourneySelectBox(uidTable, rowIndex)
{
    var uid = EJGenerateJourneyCheckboxID(uidTable, rowIndex);
    return "<input id=\"" + uid + "\" type='checkbox' onclick=\"EJOnJourneySelected('" + uidTable + "'," + rowIndex + ")\">";
}

// UI Operation

function EJUpdatePlace(request, updateFunc)
{
    W3CallAPIAsync(request, function(data, status) {
	var result = eval("(" + data + ")");
	if (result[w3ApiResultStatus] != w3ApiResultSuccessful) {
	    W3LogWarning("Get place failed!");
	    alert("Get place failed!");
	    return;
	}

        var places = result[w3ApiResultData];
        if (updateFunc != null && places.length > 0) {
            updateFunc(places);
        }
    });
}

function EJFreshJourney(journeyID)
{
    EJClearMap();

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

    EJUpdatePlace(request, _journeyDisplayFunc);
}

// UI Callback

function EJDisplaySelectedJourneyOnMap()
{
    $("table#uidJourneyTable [type='checkbox']").each(function (index) {
        if (!$(this).is(":checked")) {
            return;
        }

        $("#uidJourneyTabHeader2").click();
        EJSetViewDisplayJourney();
        EJFreshJourney(_selectedJourneyID);
    });
}

function EJDisplayCurrentJourneyOnMap()
{
    EJSetViewDisplayJourney();
    EJFreshJourney(_selectedJourneyID);
}

function EJOnSearchPlaceClicked(e)
{
    EJFillPlaceDetail(e.target);
    EJSetViewSearchPlaceSelected();
}

function EJOnJourneyPlaceClicked(e)
{
    EJFillPlaceDetail(e.target);
    EJSetViewJourneyPlaceSelected();
}

function EJOnPOIClicked(e)
{
    EJFillPlaceDetail(e.target);
    EJSetViewPOISelected();
}

function EJOnManualPlaceClicked(e)
{
    EJFillManualPlaceDetail(e);
    EJSetViewSearchPlaceSelected();
}

function EJOnJourneySelected(uidTable, rowIndex)
{
    var uidCheckBox = EJGenerateJourneyCheckboxID(uidTable, rowIndex);

    // Unselected
    if (!$("#" + uidCheckBox).is(":checked")) {
        _selectedJourneyID = null;
        EJSetViewJourneyUnselected();

        return;
    }

    // Selected
    var selectedJourney = [];
    selectedJourney.push(W3GetUIText(EJGenerateJourneyCellID(uidTable, rowIndex, 1)));
    selectedJourney.push(W3GetUIText(EJGenerateJourneyCellID(uidTable, rowIndex, 2)));
    selectedJourney.push(W3GetUIText(EJGenerateJourneyCellID(uidTable, rowIndex, 3)));
    selectedJourney.push(W3GetUIText(EJGenerateJourneyCellID(uidTable, rowIndex, 7)));

    $("table#" + uidTable + " [type='checkbox']").each(function (index) {
        if (rowIndex != index) {
            $(this).attr("checked", false);
        } else if (rowIndex == index) {
            _selectedJourneyID = selectedJourney[3];
            EJFillSelectedJourney(selectedJourney);
            EJSetViewJourneySelected();
        }
    });
}

function EJClearMap()
{
    EJSetViewNoPlaceDisplay();
    EJCleanPlaceDetail();

    if (_mapCleanFunc != null) {
        _mapCleanFunc();
    }
}

function EJResetMap()
{
    EJClearMap();

    if (_mapResetFunc != null) {
        _mapResetFunc();
    }
}

function EJShowAllPlaces()
{
    EJClearMap();

    var aid = "aidAllPlace";
    var session = W3GetSession();
    var request = W3CreateAPI(aid, session);
    if (request == "") {
	alert("Failed to create get all place request");
	return;
    }

    EJUpdatePlace(request, _allPlacesDisplayFunc);
}

function EJShowAllPOIs()
{
    EJClearMap();

    var aid = "aidAllPOI";
    var session = W3GetSession();
    var request = W3CreateAPI(aid, session);
    if (request == "") {
	alert("Failed to create get all POI request");
	return;
    }

    EJUpdatePlace(request, _allPOIsDisplayFunc);
}

function EJMapSearch(uidInput)
{
    EJClearMap();

    if (_searchFunc != null) {
        var address = W3GetUIText(uidInput);
        _searchFunc(address);
    }
}

function EJDisplayPOIOnPlacePanel()
{
    EJSetViewPlaceDetailDisplay();
    EJSetViewPlaceDetailEnable();

    W3HideUI("uidMapAddPlaceButton");
    W3HideUI("uidMapSwitchToPlacePanelButton");
    W3DisplayUI("uidMapConfirmAddPlaceButton");
    W3EnableUI("uidMapConfirmAddPlaceButton");
}

// Set View

function EJSetViewJourneyUnselected()
{
    W3DisableUI("uidJourneyGotoMapButton");
    W3HideUI("uidSelectedJourneyPanel");

    EJSetViewNoPlaceDisplay();
}

function EJSetViewJourneySelected()
{
    W3EnableUI("uidJourneyGotoMapButton");
    W3DisplayUI("uidSelectedJourneyPanel");

    EJSetViewNoPlaceDisplay();
}

function EJSetViewDisplayJourney()
{
    W3DisplayUI("uidSelectedJourneyPanel");

    EJSetViewNoPlaceDisplay();
}

function EJSetViewNoPlaceDisplay()
{
    W3HideUI("uidSelectedPlacePanel");
}

function EJSetViewSearchPlaceSelected()
{
    W3DisplayUI("uidSelectedPlacePanel");

    W3DisplayUI("uidMapAddPlaceButton");
    W3HideUI("uidMapSwitchToPlacePanelButton");
    W3HideUI("uidMapConfirmAddPlaceButton");

    W3EnableUI("uidMapAddPOIButton");

    EJSetViewPlaceDetailEnable();

    if (_selectedJourneyID == null) {
        W3DisableUI("uidMapAddPlaceButton");
        EJSetViewPlaceDetailHide();
    } else {
        W3EnableUI("uidMapAddPlaceButton");
        EJSetViewPlaceDetailDisplay();
    }

    W3EnableUI("uidMapPlaceName");
}

function EJSetViewJourneyPlaceSelected()
{
    W3DisplayUI("uidSelectedPlacePanel");

    W3DisplayUI("uidMapAddPlaceButton");
    W3HideUI("uidMapSwitchToPlacePanelButton");
    W3HideUI("uidMapConfirmAddPlaceButton");

    W3DisableUI("uidMapAddPOIButton");
    W3DisableUI("uidMapAddPlaceButton");

    EJSetViewPlaceDetailDisplay();
    EJSetViewPlaceDetailDisable();

    W3DisableUI("uidMapPlaceName");
}

function EJSetViewPOISelected()
{
    W3DisplayUI("uidSelectedPlacePanel");

    W3HideUI("uidMapAddPlaceButton");
    W3DisplayUI("uidMapSwitchToPlacePanelButton");
    W3HideUI("uidMapConfirmAddPlaceButton");

    W3DisableUI("uidMapAddPOIButton");

    EJSetViewPlaceDetailHide();
    EJSetViewPlaceDetailDisable();

    if (_selectedJourneyID == null) {
        W3DisableUI("uidMapSwitchToPlacePanelButton");
        W3DisableUI("uidMapPlaceName");
    } else {
        W3EnableUI("uidMapSwitchToPlacePanelButton");
        W3EnableUI("uidMapPlaceName");
    }
}

function EJSetViewPlaceDetailDisplay()
{
    W3DisplayUI("uidMapPlaceDatetimeLabel");
    W3DisplayUI("uidMapPlaceDatetime");
    W3DisplayUI("uidMapPlaceRemarkLabel");
    W3DisplayUI("uidMapPlaceRemark");
}

function EJSetViewPlaceDetailHide()
{
    W3HideUI("uidMapPlaceDatetimeLabel");
    W3HideUI("uidMapPlaceDatetime");
    W3HideUI("uidMapPlaceRemarkLabel");
    W3HideUI("uidMapPlaceRemark");
}

function EJSetViewPlaceDetailDisable()
{
    W3DisableUI("uidMapPlaceDatetime");
    W3DisableUI("uidMapPlaceRemark");
    W3DisableUI("uidMapPlaceNote");
}

function EJSetViewPlaceDetailEnable()
{
    W3EnableUI("uidMapPlaceDatetime");
    W3EnableUI("uidMapPlaceRemark");
    W3EnableUI("uidMapPlaceNote");
}
