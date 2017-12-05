{
    "uidPageLogin": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropSubUI: [
            "uidLoginTable"
        ]
    },

    "uidLoginTable": {
        W3Const.w3PropType: W3Const.w3TypeTable,
        W3Const.w3PropSubUI: [
            [], # No header
            ["uidUsernameLabel", "uidUsername"],
            ["uidPasswordLabel", "uidPassword"],
            ["uidNullLabel",     "uidLoginButton"]
        ]
    },

    "uidUsername": {
        W3Const.w3PropType: W3Const.w3TypeText
    },

    "uidPassword": {
        W3Const.w3PropType: W3Const.w3TypePassword
    },

    "uidLoginButton": {
        W3Const.w3PropType: W3Const.w3TypeButton,
        W3Const.w3PropString: "sidLogin",
        W3Const.w3PropTriggerApi: {
            W3Const.w3TriggerEvent: W3Const.w3EventClick,
            W3Const.w3ApiID: "aidLogin",
            W3Const.w3ApiParams: [
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeUID,
                W3Const.w3ApiDataValue: "uidUsername"
            },
            {
                W3Const.w3ApiDataType: W3Const.w3ApiDataTypeUID,
                W3Const.w3ApiDataValue: "uidPassword"
            }]
        }
    }
}
