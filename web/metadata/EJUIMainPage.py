{
    W3Const.w3UIBody: {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropSubUI: [
            "uidHeader",
            "uidMain",
            "uidFooter"
        ],
        W3Const.w3PropDefaultPage: "uidPageLogin",
        W3Const.w3PropDefaultErrorPage: "uidPageError",
        W3Const.w3PropDefaultAuthenticationPage: "uidPageLogin"
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
            "uidNaviNote",
            "uidLineBreak",
            "uidNaviCalendar",
            "uidLineBreak",
            "uidNaviJourney",
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
        W3Const.w3PropTriggerApi: [
        {
            W3Const.w3ApiID: "aidPage",
            W3Const.w3ApiCall: W3Const.w3ApiDirect,
            W3Const.w3ApiParams: [
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
                W3Const.w3ApiDataValue: "uidPageFinance"
            }]
        }],
        W3Const.w3PropEvent: {
            W3Const.w3EventClick: [
                W3Const.w3PlaceHolder_1
            ]
        }
    },
    "uidNaviNote": {
        W3Const.w3PropType: W3Const.w3TypeLink,
        W3Const.w3PropString: "sidNaviNote",
        W3Const.w3PropTriggerApi: [
        {
            W3Const.w3ApiID: "aidPage",
            W3Const.w3ApiCall: W3Const.w3ApiDirect,
            W3Const.w3ApiParams: [
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
                W3Const.w3ApiDataValue: "uidPageNote"
            }]
        }],
        W3Const.w3PropEvent: {
            W3Const.w3EventClick: [
                W3Const.w3PlaceHolder_1
            ]
        }
    },
    "uidNaviCalendar": {
        W3Const.w3PropType: W3Const.w3TypeLink,
        W3Const.w3PropString: "sidNaviCalendar",
        W3Const.w3PropTriggerApi: [
        {
            W3Const.w3ApiID: "aidPage",
            W3Const.w3ApiCall: W3Const.w3ApiDirect,
            W3Const.w3ApiParams: [
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
                W3Const.w3ApiDataValue: "uidPageCalendar"
            }]
        }],
        W3Const.w3PropEvent: {
            W3Const.w3EventClick: [
                W3Const.w3PlaceHolder_1
            ]
        }
    },
    "uidNaviJourney": {
        W3Const.w3PropType: W3Const.w3TypeLink,
        W3Const.w3PropString: "sidNaviJourney",
        W3Const.w3PropTriggerApi: [
        {
            W3Const.w3ApiID: "aidPage",
            W3Const.w3ApiCall: W3Const.w3ApiDirect,
            W3Const.w3ApiParams: [
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeString,
                W3Const.w3ApiDataValue: "uidPageJourney"
            }]
        }],
        W3Const.w3PropEvent: {
            W3Const.w3EventClick: [
                W3Const.w3PlaceHolder_1
            ]
        }
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
