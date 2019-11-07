{
    # Journey Page - journey tab
    
    "uidJourneyTabJourneyPanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropSubUI: [
            "uidJourneyTabJourneyQueryPanel",
            "uidJourneyTabJourneyAddPanel"
        ]
    },

    # Query
    
    "uidJourneyTabJourneyQueryPanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropSubUI: [
            "uidJourneyFilterTable",
            "uidJourneyTable",
            "uidJourneyToMapPanel"
        ]
    },

    # Query: Jump to Map

    "uidJourneyToMapPanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropSubUI: [
            "uidJourneyGotoMapButton"
        ],
        W3Const.w3PropCSS: {
            "clear": "both",
            "padding-top": "5px",
            "float": "left"
        }
    },
    "uidJourneyGotoMapButton": {
        W3Const.w3PropType: W3Const.w3TypeButton,
        W3Const.w3PropString: "sidGotoMap",
        W3Const.w3PropEvent: {
            W3Const.w3EventClick: [
                "EJDisplaySelectedJourneyOnMap()"
            ]
        },
        W3Const.w3PropAttr: {
            W3Const.w3AttrDisabled: "true"
        }
    },

    # Query: Display

    "uidJourneyTable": {
        W3Const.w3PropType: W3Const.w3TypeTable,
        W3Const.w3PropSubUI: [
            ["uidNullLabel", "uidColumnName", "uidTableHeaderDatetime", "uidColumnTraveler", "uidColumnEvent", "uidTableHeaderBalance", "uidColumnNote", "uidTableHeaderInvisibleData"]
        ],
        W3Const.w3PropCSS: {
            "border": "1px solid"
        },
        W3Const.w3PropSinkApi: {
            W3Const.w3ApiID: "aidJourney",
            W3Const.w3SinkRow: [
            {
                # Empty no map
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeFunc,
                W3Const.w3ApiDataValue: "EJCreateJourneySelectBox(w3PlaceHolder_1, w3PlaceHolder_2)"
            },
            {
                # Column 2 map to API result field "name"
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
                W3Const.w3ApiDataValue: "name"
            },
            {
                # Column 3 map to API result field "datetime"
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
                W3Const.w3ApiDataValue: "datetime"
            },
            {
                # Column 4 map to API result field "traveler"
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
                W3Const.w3ApiDataValue: "traveler"
            },
            {
                # Column 5 map to API result field "event"
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
                W3Const.w3ApiDataValue: "event"
            },
            {
                # Column 6 map to API result field "balance"
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeNum,
                W3Const.w3ApiDataValue: "balance"
            },
            {
                # Column 7 map to API result field "note"
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
                W3Const.w3ApiDataValue: "note"
            },
            {
                # Column 8 map to API result field "id"
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeNum,
                W3Const.w3ApiDataValue: "id"
            }]
        }
    },

    # Query: Filter
    
    "uidJourneyFilterTable": {
        W3Const.w3PropType: W3Const.w3TypeTable,
        W3Const.w3PropSubUI: [
            [], # No header
            ["uidFromLabel", "uidJourneyFilterFromDatePicker", "uidToLabel", "uidJourneyFilterToDatePicker", "uidJourneyFilterGetButton", "uidJourneyFilterAddButton"]
        ]
    },
    "uidJourneyFilterFromDatePicker": {
        W3Const.w3PropType: W3Const.w3TypeDatePicker,
    },
    "uidJourneyFilterToDatePicker": {
        W3Const.w3PropType: W3Const.w3TypeDatePicker,
    },
    "uidJourneyFilterGetButton": {
        W3Const.w3PropType: W3Const.w3TypeButton,
        W3Const.w3PropString: "sidGet",
        W3Const.w3PropTriggerApi: [
        {
            W3Const.w3ApiID: "aidJourney",
            W3Const.w3ApiParams: [
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeUID,
                W3Const.w3ApiDataValue: "uidJourneyFilterFromDatePicker"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeUID,
                W3Const.w3ApiDataValue: "uidJourneyFilterToDatePicker"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeVar,
                W3Const.w3ApiDataValue: W3Const.w3Session
            }]
        }],
        W3Const.w3PropEvent: {
            W3Const.w3EventClick: [
                W3Const.w3PlaceHolder_1
            ]
        }
    },
    "uidJourneyFilterAddButton": {
        W3Const.w3PropType: W3Const.w3TypeButton,
        W3Const.w3PropString: "sidAdd",
        W3Const.w3PropEvent: {
            W3Const.w3EventClick: [
                "W3HideUI('uidJourneyTabJourneyQueryPanel')",
                "W3DisplayUI('uidJourneyTabJourneyAddPanel')"
            ]
        }
    },

    # Add
    
    "uidJourneyTabJourneyAddPanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropSubUI: [
            "uidJourneyAddTable",
            "uidJourneyAddOperationPanel"
        ],
        W3Const.w3PropCSS: {
            "display": "none"
        }
    },
    "uidJourneyAddOperationPanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropSubUI: [
            "uidJourneyAddOperationTable"
        ]
    },
    "uidJourneyAddOperationTable": {
        W3Const.w3PropType: W3Const.w3TypeTable,
        W3Const.w3PropSubUI: [
            [], # No header
            ["uidJourneyAddSubmitButton", "uidJourneyAddCancelButton"]
        ],
        W3Const.w3PropCSS: {
            "float": "right"
        }
    },
    "uidJourneyAddSubmitButton": {
        W3Const.w3PropType: W3Const.w3TypeButton,
        W3Const.w3PropString: "sidSubmit",
        W3Const.w3PropTriggerApi: [
        {
            W3Const.w3ApiID: "aidAddJourney",
            W3Const.w3ApiParams: [
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeUID,
                W3Const.w3ApiDataValue: "uidJourneyAddName"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeUID,
                W3Const.w3ApiDataValue: "uidJourneyAddDatetime"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeUID,
                W3Const.w3ApiDataValue: "uidJourneyAddTraveler"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeUID,
                W3Const.w3ApiDataValue: "uidJourneyAddEvent"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeUID,
                W3Const.w3ApiDataValue: "uidJourneyAddNote"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeVar,
                W3Const.w3ApiDataValue: W3Const.w3Session
            }]                                
        }],
        W3Const.w3PropEvent: {
            W3Const.w3EventClick: [
                W3Const.w3PlaceHolder_1
            ]
        }
    },
    "uidJourneyAddCancelButton": {
        W3Const.w3PropType: W3Const.w3TypeButton,
        W3Const.w3PropString: "sidCancel",
        W3Const.w3PropEvent: {
            W3Const.w3EventClick: [
                "W3HideUI('uidJourneyTabJourneyAddPanel')",
                "W3DisplayUI('uidJourneyTabJourneyQueryPanel')"
            ]
        }
    },
    "uidJourneyAddTable": {
        W3Const.w3PropType: W3Const.w3TypeTable,
        W3Const.w3PropSubUI: [
            [], # No header
            ["uidNameLabel",     "uidJourneyAddName"],
            ["uidDatetimeLabel", "uidJourneyAddDatetime"],
            ["uidTravelerLabel", "uidJourneyAddTraveler"],
            ["uidEventLabel",    "uidJourneyAddEvent"],
            ["uidNoteLabel",     "uidJourneyAddNote"]
        ]
    },
    "uidJourneyAddDatetime": {
        W3Const.w3PropType: W3Const.w3TypeDatePicker
    },
    "uidJourneyAddName": {
        W3Const.w3PropType: W3Const.w3TypeText
    },
    "uidJourneyAddNote": {
        W3Const.w3PropType: W3Const.w3TypeText
    },
    "uidJourneyAddTraveler": {
        W3Const.w3PropType: W3Const.w3TypeText
    },
    "uidJourneyAddEvent": {
        W3Const.w3PropType: W3Const.w3TypeText
    }
}
