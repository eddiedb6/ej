{
    PDBConst.Name: "mapjourneyperson",
    PDBConst.Columns: [
    {
        PDBConst.Name: "Journey",
        PDBConst.Attributes: ["int", "not null"]
    },
    {
        PDBConst.Name: "Person",
        PDBConst.Attributes: ["int", "not null"]
    }],
    PDBConst.PrimaryKey: ["Journey", "Person"]
}
