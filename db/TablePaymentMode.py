{
    PDBConst.Name: "paymentmode",
    PDBConst.Columns: [
    {
        PDBConst.Name: "ID",
        PDBConst.Attributes: ["tinyint", "not null", "primary key"]
    },
    {
        PDBConst.Name: "Name",
        PDBConst.Attributes: ["varchar(128)", "not null"]
    },
    {
        PDBConst.Name: "SID",
        PDBConst.Attributes: ["varchar(128)", "not null"]
    }],
    PDBConst.Initials: [
        {"Name": "'Credit Card'", "ID": "1", "SID": "'sidTablePaymentMode1'"},
        {"Name": "'Cash'", "ID": "2", "SID": "'sidTablePaymentMode2'"},
        {"Name": "'Alipay'", "ID": "3", "SID": "'sidTablePaymentMode3'"},
        {"Name": "'WeChat Wallet'", "ID": "4", "SID": "'sidTablePaymentMode4'"},
        {"Name": "'Other'", "ID": "100", "SID": "'sidOther'"}
    ]
}
