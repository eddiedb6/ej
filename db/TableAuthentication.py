{
    PDBConst.Name: "authentication",
    PDBConst.Columns: [
    {
        PDBConst.Name: "PID",
        PDBConst.Attributes: ["int", "not null", "primary key"]
    },
    {
        PDBConst.Name: "Authentication",
        PDBConst.Attributes: ["varchar(128)", "not null"]
    }]
}
