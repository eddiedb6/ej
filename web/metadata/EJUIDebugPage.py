{    
    "uidPageDebug": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropSubUI: [
            "uidDebugContent",
            "uidLineBreak",
            "uidButtonDebug",
            "uidButtonBack"
        ],
        W3Const.w3PropCSS: {
            "text-align": "center",
        }
    },
    "uidDebugContent": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropSubUI: [
            "uidDebugDefaultContent"
        ]
    },
    "uidButtonDebug": {
        W3Const.w3PropType: W3Const.w3TypeButton,
        W3Const.w3PropString: "sidButtonDebug",
        W3Const.w3PropEvent: {
            W3Const.w3EventClick: [
                "W3GoBack()"
            ]
        }
    },
    "uidDebugDefaultContent": {
        W3Const.w3PropType: W3Const.w3TypeParagraph,
        W3Const.w3PropString: "sidDebugContent"
    }        
}
