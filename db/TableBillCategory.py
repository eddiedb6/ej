{
    PDBConst.Name: "billcategory",
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
        {"Name": "'Diet'", "ID": "1", "SID": "'sidTableBillCategory1'"},
        {"Name": "'Dress'", "ID": "2", "SID": "'sidTableBillCategory2'"}, 
        {"Name": "'Traffic'", "ID": "3", "SID": "'sidTableBillCategory3'"},
        {"Name": "'Living'", "ID": "4", "SID": "'sidTableBillCategory4'"},
        {"Name": "'Communication'", "ID": "6", "SID": "'sidTableBillCategory6'"},
        {"Name": "'Pet'", "ID": "7", "SID": "'sidTableBillCategory7'"},
        {"Name": "'Entertainment'", "ID": "8", "SID": "'sidTableBillCategory8'"},
        {"Name": "'Sports'", "ID": "9", "SID": "'sidTableBillCategory9'"},
        {"Name": "'Travel'", "ID": "10", "SID": "'sidTableBillCategory10'"},
        {"Name": "'Education'", "ID": "11", "SID": "'sidTableBillCategory11'"}, 
        {"Name": "'Healthy'", "ID": "12", "SID": "'sidTableBillCategory12'"},
        {"Name": "'Sociality'", "ID": "13", "SID": "'sidTableBillCategory13'"},
        {"Name": "'Reside'", "ID": "17", "SID": "'sidTableBillCategory17'"},
        {"Name": "'Other'", "ID": "100", "SID": "'sidOther'"}
    ]
}
