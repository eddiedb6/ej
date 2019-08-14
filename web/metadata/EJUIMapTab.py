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
            "uidMapOperationTable",
            "uidSelectedPlacePanel",
        ]
    },
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
            ["uidNameLabel",      "uidMapPlaceName"],
            ["uidLatitudeLabel",  "uidMapPlaceLatitude"],
            ["uidLongitudeLabel", "uidMapPlaceLongitude"],
            ["uidDatetimeLabel",  "uidMapPlaceDatetime"],
            ["uidRemarkLabel",    "uidMapPlaceRemark"],
            ["uidNoteLabel",      "uidMapPlaceNote"],
            ["uidNullLabel",      "uidMapAddPlaceButton"]
        ]
    },
    "uidMapPlaceDatetime": {
        W3Const.w3PropType: W3Const.w3TypeDatePicker
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
    "uidRemarkLabel": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropString: "sidRemarkLabel",
        W3Const.w3PropClass: "cidRightLabel"
    },
    "uidMapPlaceName": {
        W3Const.w3PropType: W3Const.w3TypeLabel
    },
    "uidMapPlaceRemark": {
        W3Const.w3PropType: W3Const.w3TypeText
    },
    "uidMapPlaceLatitude": {
        W3Const.w3PropType: W3Const.w3TypeLabel
    },
    "uidMapPlaceLongitude": {
        W3Const.w3PropType: W3Const.w3TypeLabel
    },
    "uidMapPlaceNote": {
        W3Const.w3PropType: W3Const.w3TypeText
    },
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
    "uidMapOperationTable": {
        W3Const.w3PropType: W3Const.w3TypeTable,
        W3Const.w3PropSubUI: [
            [],
            ["uidMapSearchInput", "uidMapSearchButton"]
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
    "uidMapAddPlaceButton": {
        W3Const.w3PropType: W3Const.w3TypeButton,
        W3Const.w3PropString: "sidAddPlace",
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
                "W3HideUI('uidSelectedPlacePanel')"
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
            W3Const.w3AttrMapLocation: "39.918794, 116.398568",
            W3Const.w3AttrMapKey: "AixlydPEmOi786Yys1IYY5u36B-z1HdoglcnrS7HsohUY5bZorHmJlKBpNryPeM3"
        },
        W3Const.w3PropCSS: {
            "border": "2px solid",
            "min-width": "800px",
            "min-height": "600px"
        }
    }
}
