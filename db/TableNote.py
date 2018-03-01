{
    PDBConst.Name: "note",
    PDBConst.Columns: [
    {
        PDBConst.Name: "Title",
        PDBConst.Attributes: ["varchar(255)", "not null", "primary key"]
    },
    {
        PDBConst.Name: "Tag",
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
