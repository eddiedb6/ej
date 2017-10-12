{
    PDBConst.Name: "exchangerate",
    PDBConst.Columns: [
    {
        PDBConst.Name: "Datetime",
        PDBConst.Attributes: ["datetime", "not null"]
    },
    {
        PDBConst.Name: "Currency",
        PDBConst.Attributes: ["tinyint", "not null"]
    },
    {
        PDBConst.Name: "Rate",
        PDBConst.Attributes: ["double(12,4)"]
    }],
    PDBConst.PrimaryKey: ["Datetime", "Currency"]
}
