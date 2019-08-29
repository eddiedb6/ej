{
    PDBConst.Name: "note",
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
        PDBConst.Name: "Title",
        PDBConst.Attributes: ["varchar(255)", "not null"]
    },
    {
        PDBConst.Name: "Tag",
        PDBConst.Attributes: ["tinyint", "not null"]
    },
    {
        PDBConst.Name: "Type",
        PDBConst.Attributes: ["tinyint", "not null"]
    },
    {
        PDBConst.Name: "Modified",
        PDBConst.Attributes: ["datetime", "not null"]
    },
    {
        PDBConst.Name: "Note",
        PDBConst.Attributes: ["longtext"]
    }]
}
