{
    "uidPageNote": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropSubUI: [
            "uidNotePanel",
            "uidNoteOperationPanel"
        ]
    },

    "uidNotePanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropFunc: {
            W3Const.w3FuncCreator: "EJCreateNoteTab"
        }
    },

    "uidNoteOperationPanel": {
        W3Const.w3PropType: W3Const.w3TypePanel,
        W3Const.w3PropSubUI: [
            "uidNoteAddButton"
        ],
        W3Const.w3PropCSS: {
            "clear": "both",
            "padding-top": "5px",
            "float": "right"
        }
    },

    "uidNoteAddButton": {
        W3Const.w3PropType: W3Const.w3TypeButton,
        W3Const.w3PropString: "sidAdd",
        W3Const.w3PropEvent: {
            W3Const.w3EventClick: [
                #"W3HideUI('uidFinanceTabBillQueryPanel')",
                #"W3DisplayUI('uidFinanceTabBillAddPanel')"
            ]
        }
    }
}
