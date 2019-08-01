{
    "uidPageCalendar": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropSubUI: [
            "uidCalendarPanel",
            "uidCalendarAddPanel"
        ]
    },

    # Calendar
    
    "uidCalendarPanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropSubUI: [
            "uidCalendar",
            "uidCalendarAddEventButton"
        ]
    },

    "uidCalendarAddEventButton": {
        W3Const.w3PropType: W3Const.w3TypeButton,
        W3Const.w3PropString: "sidAdd",
        W3Const.w3PropCSS: {
            "float": "right",
            "margin-top": "10px"
        },
        W3Const.w3PropEvent: {
            W3Const.w3EventClick: [
                "W3HideUI('uidCalendarPanel')",
                "W3DisplayUI('uidCalendarAddPanel')"
            ]
        }
    },

    "uidCalendar": {
        W3Const.w3PropType: W3Const.w3TypeCalendar
    },

    # Add
    
    "uidCalendarAddPanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropSubUI: [
            "uidCalendarAddTable",
            "uidCalendarAddOperationPanel"
        ],
        W3Const.w3PropCSS: {
            "display": "none"
        }
    },
    "uidCalendarAddOperationPanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropSubUI: [
            "uidCalendarAddOperationTable"
        ]
    },
    "uidCalendarAddOperationTable": {
        W3Const.w3PropType: W3Const.w3TypeTable,
        W3Const.w3PropSubUI: [
            [], # No header
            ["uidCalendarAddSubmitButton", "uidCalendarAddCancelButton"]
        ],
        W3Const.w3PropCSS: {
            "float": "right"
        }
    },
    "uidCalendarAddCancelButton": {
        W3Const.w3PropType: W3Const.w3TypeButton,
        W3Const.w3PropString: "sidCancel",
        W3Const.w3PropEvent: {
            W3Const.w3EventClick: [
                "W3HideUI('uidCalendarAddPanel')",
                "W3DisplayUI('uidCalendarPanel')"
            ]
        }
    },
    "uidCalendarAddSubmitButton": {
        W3Const.w3PropType: W3Const.w3TypeButton,
        W3Const.w3PropString: "sidSubmit",
        W3Const.w3PropTriggerApi: [
        {
            W3Const.w3ApiID: "aidAddCalendarEvent",
            W3Const.w3ApiParams: [
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeUID,
                W3Const.w3ApiDataValue: "uidCalendarEventName"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeUID,
                W3Const.w3ApiDataValue: "uidCalendarEventDate"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeUID,
                W3Const.w3ApiDataValue: "uidCalendarEventRepeat"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeUID,
                W3Const.w3ApiDataValue: "uidCalendarEventNote"
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
    "uidCalendarAddTable": {
        W3Const.w3PropType: W3Const.w3TypeTable,
        W3Const.w3PropSubUI: [
            [], # No header
            ["uidNameLabel",     "uidCalendarEventName"],
            ["uidDatetimeLabel", "uidCalendarEventDate"],
            ["uidRepeatLabel",   "uidCalendarEventRepeat"],
            ["uidNoteLabel",     "uidCalendarEventNote"]
        ]
    },
    "uidCalendarEventDate": {
        W3Const.w3PropType: W3Const.w3TypeDatePicker
    },
    "uidCalendarEventName": {
        W3Const.w3PropType: W3Const.w3TypeText
    },
    "uidCalendarEventRepeat": {
        W3Const.w3PropType: W3Const.w3TypeText
    },
    "uidCalendarEventNote": {
        W3Const.w3PropType: W3Const.w3TypeText
    }
}
