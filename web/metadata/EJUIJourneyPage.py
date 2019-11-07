{
    "uidPageJourney": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropSubUI: [
            "uidJourneyTab"
        ]
    },
    "uidJourneyTab": {
        W3Const.w3PropType: W3Const.w3TypeTab,
        W3Const.w3PropSubUI: [
            ["uidJourneyTabJourneyLabel", "uidJourneyTabJourneyPanel"],
            ["uidJourneyTabMapLabel",     "uidJourneyTabMapPanel"]
        ],
        W3Const.w3PropCSS: {
            # CSS for tab only support these format
            "border-width": "1px",
            "border-style": "solid",
            "background-color": "white"
        }
    },
    "uidJourneyTabJourneyLabel": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropString: "sidJourneyTabJourney",
        W3Const.w3PropClass: "cidLRPadding"
    },
    "uidJourneyTabMapLabel": {
        W3Const.w3PropType: W3Const.w3TypeLabel,
        W3Const.w3PropString: "sidJourneyTabMap",
        W3Const.w3PropClass: "cidLRPadding"
    },

    "JourneyTab": ImportPartial("EJUIJourneyTab.py"),
    "MapTab": ImportPartial("EJUIMapTab.py")
}
