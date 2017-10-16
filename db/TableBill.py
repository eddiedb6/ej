{
    PDBConst.Name: "bill",
    PDBConst.Columns: [
    {
        PDBConst.Name: "ID",
        PDBConst.Attributes: ["int", "not null", "auto_increment", "primary key"]
    },
    {
        PDBConst.Name: "PID",
        PDBConst.Attributes: ["int", "not null"]
    },
    {
        PDBConst.Name: "Datetime",
        PDBConst.Attributes: ["datetime", "not null"]
    },
    {
        PDBConst.Name: "Amount",
        PDBConst.Attributes: ["double(12,2)", "not null"]
    },
    {
        PDBConst.Name: "Currency",
        PDBConst.Attributes: ["tinyint", "not null", "default 1"]
    },
    {
        PDBConst.Name: "Category",
        PDBConst.Attributes: ["tinyint"]
    },
    {
        PDBConst.Name: "PaymentMode",
        PDBConst.Attributes: ["tinyint"]
    },
    {
        PDBConst.Name: "Note",
        PDBConst.Attributes: ["varchar(255)"]
    }]
}
