{
    PDBConst.Name: "calendar",
    PDBConst.Columns: [
    {
        PDBConst.Name: "ID",
        PDBConst.Attributes: ["int", "not null", "auto_increment", "primary key"]
    },
    {
        PDBConst.Name: "Name",
        PDBConst.Attributes: ["varchar(255)", "not null"]
    },
    {
        PDBConst.Name: "Datetime",
        PDBConst.Attributes: ["datetime", "not null"]
    },
    {
        PDBConst.Name: "RepeatMonth",
        PDBConst.Attributes: ["tinyint", "not null"]
    },
    {
        PDBConst.Name: "Note",
        PDBConst.Attributes: ["varchar(255)"]
    }]
}
