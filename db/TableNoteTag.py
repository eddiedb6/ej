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
        {"Tag": "'Reading'", "ID": "6", "SID": "'sidTableNoteTag6'"},
        {"Tag": "'Graphic'", "ID": "7", "SID": "'sidTableNoteTag7'"},
        {"Tag": "'Math'", "ID": "8", "SID": "'sidTableNoteTag8'"},
        {"Tag": "'Mobile'", "ID": "9", "SID": "'sidTableNoteTag9'"},
        {"Tag": "'Other'", "ID": "100", "SID": "'sidOther'"}
    ]
}
