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
            "uidMapOperationTable"
        ]
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
