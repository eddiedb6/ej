{
    PDBConst.Name: "person",
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
        PDBConst.Name: "Sex",
        PDBConst.Attributes: ["tinyint", "not null"]
    },
    {
        PDBConst.Name: "Role",
        PDBConst.Attributes: ["tinyint", "not null"]
    }],
    PDBConst.Initials: [
        {"Name": "'Joan'", "FID": "1", "Sex": "0", "Role": "0"},
        {"Name": "'Ed'", "FID": "1", "Sex": "1", "Role": "1"}
    ]
}
