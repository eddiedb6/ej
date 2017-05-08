{
    PDBConst.Name: "debt",
    PDBConst.Columns: [
    {
        PDBConst.Name: "ID",
        PDBConst.Attributes: ["int", "not null", "auto_increment", "primary key"]
    },
    {
        PDBConst.Name: "FID",
        PDBConst.Attributes: ["int", "not null"]
    },
    {
        PDBConst.Name: "Start",
        PDBConst.Attributes: ["datetime", "not null"]
    },
    {
        PDBConst.Name: "End",
        PDBConst.Attributes: ["datetime", "not null"]
    },
    {
        PDBConst.Name: "Amount",
        PDBConst.Attributes: ["double(12,2)", "not null"]
    },
    {
        PDBConst.Name: "Balance",
        PDBConst.Attributes: ["double(12,2)"]
    },
    {
        PDBConst.Name: "Note",
        PDBConst.Attributes: ["varchar(255)"]
    }]
}
