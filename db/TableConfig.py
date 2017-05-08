{
    PDBConst.Name: "config",
    PDBConst.Columns: [
    {
        PDBConst.Name: "Name",
        PDBConst.Attributes: ["varchar(128)", "not null", "primary key"]
    },
    {
        PDBConst.Name: "Value",
        PDBConst.Attributes: ["varchar(128)"]
    }],
    PDBConst.Initials: [
        {"Name": "'version'", "Value": "'0.1'"}
    ]
}
