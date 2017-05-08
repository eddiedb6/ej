{
    PDBConst.Name: "financeevent",
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
        PDBConst.Name: "Name",
        PDBConst.Attributes: ["varchar(128)", "not null"]
    },
    {
        PDBConst.Name: "Budget",
        PDBConst.Attributes: ["double(12,2)", "not null"]
    },
    {
        PDBConst.Name: "Note",
        PDBConst.Attributes: ["varchar(255)"]
    }]
}
