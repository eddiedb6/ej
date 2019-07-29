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
            "uidCalendar"
        ]
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
        W3Const.w3PropString: "sidSubmit"
    },
    "uidCalendarAddTable": {
        W3Const.w3PropType: W3Const.w3TypeTable,
        W3Const.w3PropSubUI: [
            [] # No header
        ]
    }
}
