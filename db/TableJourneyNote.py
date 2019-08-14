{
    PDBConst.Name: "journeynote",
    PDBConst.Columns: [
    {
        PDBConst.Name: "Journey",
        PDBConst.Attributes: ["int", "not null"]
    },
    {
        PDBConst.Name: "Place",
        PDBConst.Attributes: ["int", "not null"]
    },
    {
        PDBConst.Name: "Remark",
        PDBConst.Attributes: ["tinyint"]
    },
    {
        PDBConst.Name: "Note",
        PDBConst.Attributes: ["longtext"]
    }],
    PDBConst.PrimaryKey: ["Journey", "Place"]
}
