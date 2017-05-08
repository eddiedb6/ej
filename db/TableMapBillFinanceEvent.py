{
    PDBConst.Name: "mapbillfinanceevent",
    PDBConst.Columns: [
    {
        PDBConst.Name: "Bill",
        PDBConst.Attributes: ["int", "not null"]
    },
    {
        PDBConst.Name: "Event",
        PDBConst.Attributes: ["int", "not null"]
    }],
    PDBConst.PrimaryKey: ["Bill", "Event"]
}
