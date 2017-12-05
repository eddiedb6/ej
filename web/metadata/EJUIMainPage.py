{
    W3Const.w3UIBody: {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropSubUI: [
            "uidHeader",
            "uidMain",
            "uidFooter"
        ],
        W3Const.w3PropDefaultPage: "uidPageLogin",
        W3Const.w3PropDefaultErrorPage: "uidPageError"
    },
    "uidHeader": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropSubUI: [
            "uidTitle",
            "uidLine"
        ],
        W3Const.w3PropCSS: {
            "text-align": "center",
        }
    },
    "uidTitle": {
        W3Const.w3PropType: W3Const.w3TypeHeadline,
        W3Const.w3PropAttr: {
            W3Const.w3AttrHeadlineLevel : "1"
        },
        W3Const.w3PropString: "sidTitle" 
    },
    "uidFooter": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropSubUI: [
            "uidLine",
            "uidCopyright"
        ],
        W3Const.w3PropCSS: {
            "text-align": "center",
            "clear": "both",
            "padding-top": "5px",
        }
    },
    "uidCopyright": {
        W3Const.w3PropType: W3Const.w3TypeParagraph,
        W3Const.w3PropString: "sidCopyright"
    },
    "uidMain": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropSubUI: [
            "uidNavigation",
            "uidPage"
        ]
    },
    "uidNavigation": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropSubUI: [
            "uidNaviFinance",
            "uidLineBreak",
            "uidNaviDebug",
            "uidLineBreak"
        ],
        W3Const.w3PropClass: "cidLeftBorder",
        W3Const.w3PropCSS: {
            "padding-right": "15px"
        }
    },
    "uidPage": {
        W3Const.w3PropType: W3Const.w3TypePage,
        W3Const.w3PropClass: "cidLeftBorder",
        W3Const.w3PropCSS: {
            "padding-left": "5px",
            "padding-right": "5px"
        }
    },
    
    # Navigation
    "uidNaviFinance": {
        W3Const.w3PropType: W3Const.w3TypeLink,
        W3Const.w3PropString: "sidNaviFinance",
        W3Const.w3PropTriggerApi: {
            W3Const.w3ApiID: "aidPage",
            W3Const.w3ApiParams: [
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
                W3Const.w3ApiDataValue: "uidPageFinance"
            }]
        }
    },
    "uidNaviDebug": {
        W3Const.w3PropType: W3Const.w3TypeLink,
        W3Const.w3PropString: "sidNaviDebug",
        W3Const.w3PropTriggerApi: {
            W3Const.w3ApiID: "aidPage",
            W3Const.w3ApiParams: [
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
                W3Const.w3ApiDataValue: "uidPageDebug"
            }]
        }
    },

    # Debug Page
    "uidPageDebug": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropSubUI: [
            "uidDebugContent",
            "uidLineBreak",
            "uidButtonBack"
        ],
        W3Const.w3PropCSS: {
            "text-align": "center",
        }
    },
    "uidDebugContent": {
        W3Const.w3PropType: W3Const.w3TypeParagraph,
        W3Const.w3PropString: "sidDebugContent"
    },

    # Error Page
    "uidPageError": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropSubUI: [
            "uidErrorContent",
            "uidLineBreak",
            "uidButtonBack"
        ],
        W3Const.w3PropCSS: {
            "text-align": "center",
        }
    },
    "uidErrorContent": {
        W3Const.w3PropType: W3Const.w3TypeParagraph,
        W3Const.w3PropString: "sidErrorContent"
    }
}
