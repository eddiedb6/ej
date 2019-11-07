{
    PDBConst.Name: "notetype",
    PDBConst.Columns: [
    {
        PDBConst.Name: "ID",
        PDBConst.Attributes: ["tinyint", "not null", "primary key"]
    },
    {
        PDBConst.Name: "Type",
        PDBConst.Attributes: ["varchar(128)", "not null"]
    },
    {
        PDBConst.Name: "SID",
        PDBConst.Attributes: ["varchar(128)", "not null"]
    }],
    PDBConst.Initials: [
        {"Type": "'html'", "ID": "1", "SID": "'sidTableNoteType1'"},
        {"Type": "'pdf'", "ID": "2", "SID": "'sidTableNoteType2'"}
    ]
}
