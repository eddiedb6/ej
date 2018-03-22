{
    PDBConst.Name: "notetag",
    PDBConst.Columns: [
    {
        PDBConst.Name: "ID",
        PDBConst.Attributes: ["tinyint", "not null", "primary key"]
    },
    {
        PDBConst.Name: "Tag",
        PDBConst.Attributes: ["varchar(128)", "not null"]
    },
    {
        PDBConst.Name: "SID",
        PDBConst.Attributes: ["varchar(128)", "not null"]
    }],
    PDBConst.Initials: [
        {"Tag": "'Language'", "ID": "1", "SID": "'sidTableNoteTag1'"},
        {"Tag": "'Linux'", "ID": "2", "SID": "'sidTableNoteTag2'"},
        {"Tag": "'Windows'", "ID": "3", "SID": "'sidTableNoteTag3'"}, 
        {"Tag": "'LAMP'", "ID": "4", "SID": "'sidTableNoteTag4'"},
        {"Tag": "'Utility'", "ID": "5", "SID": "'sidTableNoteTag5'"},
        {"Tag": "'Life'", "ID": "80", "SID": "'sidTableNoteTag80'"},
        {"Tag": "'Travel'", "ID": "90", "SID": "'sidTableNoteTag90'"},
        {"Tag": "'Other'", "ID": "100", "SID": "'sidOther'"}
    ]
}
