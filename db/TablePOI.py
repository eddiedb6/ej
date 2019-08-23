{
    PDBConst.Name: "poi",
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
        PDBConst.Name: "Place",
        PDBConst.Attributes: ["int", "not null"]
    },
    {
        PDBConst.Name: "Note",
        PDBConst.Attributes: ["varchar(255)"]
    }]
}
