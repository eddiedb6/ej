{
    # Journey Page - map tab
    
    "uidJourneyTabMapPanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropSubUI: [
            "uidMapOperationPanel",
            "uidMapPanel"
        ]
    },

    # Operation
    
    "uidMapOperationPanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropSubUI: [
            "uidSelectedJourneyPanel",
            "uidMapSearchPanel",
            "uidSelectedPlacePanel",
        ]
    },

    # Operation - place

    "uidSelectedPlacePanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropSubUI: [
            "uidSelectedPlaceTable"
        ],
        W3Const.w3PropCSS: {
            "display": "none"
        }
    },
    "uidSelectedPlaceTable": {
        W3Const.w3PropType: W3Const.w3TypeTable,
        W3Const.w3PropSubUI: [
            [], # No header
            ["uidNameLabel",             "uidMapPlaceName"],
            ["uidLatitudeLabel",         "uidMapPlaceLatitude"],
            ["uidLongitudeLabel",        "uidMapPlaceLongitude"],
            ["uidMapPlaceDatetimeLabel", "uidMapPlaceDatetime"],
            ["uidMapPlaceRemarkLabel",   "uidMapPlaceRemark"],
            ["uidMapPlaceNoteLabel",     "uidMapPlaceNote"],
            ["uidSelectedPOIID",     "uidMapPlaceOperationTable"]
        ]
    },
    "uidLatitudeLabel": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropString: "sidLatitudeLabel",
        W3Const.w3PropClass: "cidRightLabel"
    },
    "uidLongitudeLabel": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropString: "sidLongitudeLabel",
        W3Const.w3PropClass: "cidRightLabel"
    },
    "uidMapPlaceDatetimeLabel": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropString: "sidDatetimeLabel",
        W3Const.w3PropClass: "cidRightLabel",
        W3Const.w3PropCSS: {
            "display": "none"
        }
    },
    "uidMapPlaceRemarkLabel": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropString: "sidRemarkLabel",
        W3Const.w3PropClass: "cidRightLabel",
        W3Const.w3PropCSS: {
            "display": "none"
        }
    },
    "uidMapPlaceNoteLabel": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropString: "sidNoteLabel",
        W3Const.w3PropClass: "cidRightLabel"
    },
    "uidMapPlaceName": {
        W3Const.w3PropType: W3Const.w3TypeText,
        W3Const.w3PropAttr: {
            W3Const.w3AttrDisabled: "true"
        }
    },
    "uidMapPlaceLatitude": {
        W3Const.w3PropType: W3Const.w3TypeLabel
    },
    "uidMapPlaceLongitude": {
        W3Const.w3PropType: W3Const.w3TypeLabel
    },
    "uidMapPlaceDatetime": {
        W3Const.w3PropType: W3Const.w3TypeDatePicker,
        W3Const.w3PropCSS: {
            "display": "none"
        },
        W3Const.w3PropAttr: {
            W3Const.w3AttrDisabled: "true"
        }
    },
    "uidMapPlaceRemark": {
        W3Const.w3PropType: W3Const.w3TypeText,
        W3Const.w3PropCSS: {
            "display": "none"
        },
        W3Const.w3PropAttr: {
            W3Const.w3AttrDisabled: "true"
        }
    },
    "uidMapPlaceNote": {
        W3Const.w3PropType: W3Const.w3TypeText,
        W3Const.w3PropAttr: {
            W3Const.w3AttrDisabled: "true"
        }
    },
    "uidSelectedPOIID": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropCSS: {
            "display": "none",
            "width": "0"
        }
    },
    "uidMapPlaceOperationTable": {
        W3Const.w3PropType: W3Const.w3TypeTable,
        W3Const.w3PropSubUI: [
            [],
            ["uidMapAddPlaceButton", "uidMapSwitchToPlacePanelButton", "uidMapConfirmAddPlaceButton", "uidMapAddPOIButton"]
        ]
    },
    "uidMapAddPlaceButton": {
        W3Const.w3PropType: W3Const.w3TypeButton,
        W3Const.w3PropString: "sidAddJourneyPlace",
        W3Const.w3PropTriggerApi: [
        {
            W3Const.w3ApiID: "aidAddJourneyPlace",
            W3Const.w3ApiParams: [
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeUID,
                W3Const.w3ApiDataValue: "uidSelectedJourneyID"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeUID,
                W3Const.w3ApiDataValue: "uidMapPlaceName"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeUID,
                W3Const.w3ApiDataValue: "uidMapPlaceDatetime"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeUID,
                W3Const.w3ApiDataValue: "uidMapPlaceLatitude"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeUID,
                W3Const.w3ApiDataValue: "uidMapPlaceLongitude"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeUID,
                W3Const.w3ApiDataValue: "uidMapPlaceRemark"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeUID,
                W3Const.w3ApiDataValue: "uidMapPlaceNote"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeVar,
                W3Const.w3ApiDataValue: W3Const.w3Session
            }]
        }],
        W3Const.w3PropEvent: {
            W3Const.w3EventClick: [
                W3Const.w3PlaceHolder_1,
                "EJResetMap()"
            ]
        },
        W3Const.w3PropAttr: {
            W3Const.w3AttrDisabled: "true"
        },
        W3Const.w3PropCSS: {
            "display": "none"
        }
    },
    "uidMapAddPOIButton": {
        W3Const.w3PropType: W3Const.w3TypeButton,
        W3Const.w3PropString: "sidAddPOI",
        W3Const.w3PropTriggerApi: [
        {
            W3Const.w3ApiID: "aidAddPOI",
            W3Const.w3ApiParams: [
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeUID,
                W3Const.w3ApiDataValue: "uidMapPlaceName"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeUID,
                W3Const.w3ApiDataValue: "uidMapPlaceLatitude"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeUID,
                W3Const.w3ApiDataValue: "uidMapPlaceLongitude"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeUID,
                W3Const.w3ApiDataValue: "uidMapPlaceNote"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeVar,
                W3Const.w3ApiDataValue: W3Const.w3Session
            }]
        }],
        W3Const.w3PropEvent: {
            W3Const.w3EventClick: [
                W3Const.w3PlaceHolder_1,
                "EJResetMap()"
            ]
        },
        W3Const.w3PropAttr: {
            W3Const.w3AttrDisabled: "true"
        }
    },
    "uidMapSwitchToPlacePanelButton": {
        W3Const.w3PropType: W3Const.w3TypeButton,
        W3Const.w3PropString: "sidAddJourneyPlace",
        W3Const.w3PropEvent: {
            W3Const.w3EventClick: [
                "EJDisplayPOIOnPlacePanel()"
            ]
        },
        W3Const.w3PropAttr: {
            W3Const.w3AttrDisabled: "true"
        },
        W3Const.w3PropCSS: {
            "display": "none"
        }
    },
    "uidMapConfirmAddPlaceButton": {
        W3Const.w3PropType: W3Const.w3TypeButton,
        W3Const.w3PropString: "sidSubmit",
        W3Const.w3PropTriggerApi: [
        {
            W3Const.w3ApiID: "aidAddPOIToJourney",
            W3Const.w3ApiParams: [
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeUID,
                W3Const.w3ApiDataValue: "uidSelectedPOIID"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeUID,
                W3Const.w3ApiDataValue: "uidSelectedJourneyID"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeUID,
                W3Const.w3ApiDataValue: "uidMapPlaceDatetime"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeUID,
                W3Const.w3ApiDataValue: "uidMapPlaceRemark"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeUID,
                W3Const.w3ApiDataValue: "uidMapPlaceNote"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeVar,
                W3Const.w3ApiDataValue: W3Const.w3Session
            }]
        }],
        W3Const.w3PropEvent: {
            W3Const.w3EventClick: [
                W3Const.w3PlaceHolder_1,
                "EJResetMap()"
            ]
        },
        W3Const.w3PropAttr: {
            W3Const.w3AttrDisabled: "true"
        },
        W3Const.w3PropCSS: {
            "display": "none"
        }
    },

    # Operation - journey

    "uidSelectedJourneyPanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropSubUI: [
            "uidSelectedJourneyTable"
        ],
        W3Const.w3PropCSS: {
            "display": "none"
        }
    },
    "uidSelectedJourneyTable": {
        W3Const.w3PropType: W3Const.w3TypeTable,
        W3Const.w3PropSubUI: [
            [],
            ["uidJourneyLabel", "uidSelectedJourneyName", "uidSelectedJourneyDatetime", "uidSelectedJourneyTraveler", "uidSelectedJourneyID", "uidDisplayJourneyButton"]
        ]
    },
    "uidJourneyLabel": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropString: "sidJourneyLabel",
        W3Const.w3PropClass: "cidRightLabel",
        W3Const.w3PropCSS: {
            "font-weight": "bold"
        }
    },
    "uidSelectedJourneyName": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropClass: "cidLRPadding"
    },
    "uidSelectedJourneyDatetime": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropClass: "cidLRPadding"
    },
    "uidSelectedJourneyTraveler": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropClass: "cidLRPadding"
    },
    "uidSelectedJourneyID": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropCSS: {
            "display": "none",
            "width": "0"
        }
    },
    "uidDisplayJourneyButton": {
        W3Const.w3PropType: W3Const.w3TypeButton,
        W3Const.w3PropString: "sidGotoMap",
        W3Const.w3PropEvent: {
            W3Const.w3EventClick: [
                "EJDisplayCurrentJourneyOnMap()"
            ]
        }
    },

    # Operation - search

    "uidMapSearchPanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropSubUI: [
            "uidMapSearchTable"
        ]
    },
    "uidMapSearchTable": {
        W3Const.w3PropType: W3Const.w3TypeTable,
        W3Const.w3PropSubUI: [
            [],
            ["uidMapSearchInput", "uidMapSearchButton", "uidMapShowAllPlaceButton", "uidMapShowAllPOIButton", "uidMapClearButton"]
        ]
    },
    "uidMapSearchInput": {
        W3Const.w3PropType: W3Const.w3TypeText
    },
    "uidMapSearchButton": {
        W3Const.w3PropType: W3Const.w3TypeButton,
        W3Const.w3PropString: "sidSearch",
        W3Const.w3PropEvent: {
            W3Const.w3EventClick: [
                "EJMapSearch('uidMapSearchInput')"
            ]
        }
    },
    "uidMapShowAllPlaceButton": {
        W3Const.w3PropType: W3Const.w3TypeButton,
        W3Const.w3PropString: "sidShowAllPlace",
        W3Const.w3PropEvent: {
            W3Const.w3EventClick: [
                "EJShowAllPlaces()"
            ]
        }
    },
    "uidMapShowAllPOIButton": {
        W3Const.w3PropType: W3Const.w3TypeButton,
        W3Const.w3PropString: "sidShowAllPOI",
        W3Const.w3PropEvent: {
            W3Const.w3EventClick: [
                "EJShowAllPOIs()"
            ]
        }
    },
    "uidMapClearButton": {
        W3Const.w3PropType: W3Const.w3TypeButton,
        W3Const.w3PropString: "sidClear",
        W3Const.w3PropEvent: {
            W3Const.w3EventClick: [
                "EJResetMap()"
            ]
        }
    },

    # Map
    
    "uidMapPanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropSubUI: [
            "uidMSMap"
        ]
    },
    "uidMSMap": {
        W3Const.w3PropType: W3Const.w3TypeMap,
        W3Const.w3PropMap: {
            W3Const.w3AttrMapHandler: "EJMapHandler(w3PlaceHolder_1)",
            W3Const.w3AttrMapLocation: [],
            W3Const.w3AttrMapKey: ""
        },
        W3Const.w3PropCSS: {
            "border": "2px solid",
            "min-width": "800px",
            "min-height": "600px"
        }
    }
}
