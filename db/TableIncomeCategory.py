{
    PDBConst.Name: "incomecategory",
    PDBConst.Columns: [
    {
        PDBConst.Name: "ID",
        PDBConst.Attributes: ["tinyint", "not null", "primary key"]
    },
    {
        PDBConst.Name: "Name",
        PDBConst.Attributes: ["varchar(128)", "not null"]
    },
    {
        PDBConst.Name: "SID",
        PDBConst.Attributes: ["varchar(128)", "not null"]
    }],
    PDBConst.Initials: [
        {"Name": "'Salary'", "ID": "1", "SID": "'sidTableIncomeCategory1'"},
        {"Name": "'Lucky Money'", "ID": "2", "SID": "'sidTableIncomeCategory2'"},
        {"Name": "'Bonus'", "ID": "3", "SID": "'sidTableIncomeCategory3'"},
        {"Name": "'Annual Bonus'", "ID": "4", "SID": "'sidTableIncomeCategory4'"}, 
        {"Name": "'Other'", "ID": "100", "SID": "'sidOther'"}
    ]
}
