{
    PDBConst.Name: "journeyplace",
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
        PDBConst.Name: "Latitude",
        PDBConst.Attributes: ["double(18,15)", "not null"]
    },
    {
        PDBConst.Name: "Longitude",
        PDBConst.Attributes: ["double(18,15)", "not null"]
    },
    {
        PDBConst.Name: "Altitude",
        PDBConst.Attributes: ["int"]
    }]
}
