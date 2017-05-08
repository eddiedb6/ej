{
    PDBConst.Name: "currency",
    PDBConst.Columns: [
    {
        PDBConst.Name: "ID",
        PDBConst.Attributes: ["tinyint", "not null", "auto_increment", "primary key"]
    },
    {
        PDBConst.Name: "Name",
        PDBConst.Attributes: ["char(3)", "not null"]
    },
    {
        PDBConst.Name: "SID",
        PDBConst.Attributes: ["varchar(128)", "not null"]
    }],
    PDBConst.Initials: [
        {"Name": "'CNY'", "SID": "'sidTableCurrency1'"},    # China Yuan
        {"Name": "'USD'", "SID": "'sidTableCurrency2'"},    # US Dollar
        {"Name": "'EUR'", "SID": "'sidTableCurrency3'"},    # Euro
        {"Name": "'JPY'", "SID": "'sidTableCurrency4'"},    # Japan Yen
        {"Name": "'KRW'", "SID": "'sidTableCurrency5'"},    # Korea Won
        {"Name": "'THB'", "SID": "'sidTableCurrency6'"},    # Thailand Baht
        {"Name": "'GBP'", "SID": "'sidTableCurrency7'"},    # Britain Pound
        {"Name": "'CAD'", "SID": "'sidTableCurrency8'"},    # Canada Dollar
        {"Name": "'AUD'", "SID": "'sidTableCurrency9'"},    # Australia Dollar
        {"Name": "'NZD'", "SID": "'sidTableCurrency10'"},    # New Zealand Dollar
        {"Name": "'RUR'", "SID": "'sidTableCurrency11'"},    # Russia Ruble
        {"Name": "'HKD'", "SID": "'sidTableCurrency12'"},    # Hong Kong Dollar
        {"Name": "'TWD'", "SID": "'sidTableCurrency13'"},    # Taiwan Dollar
        {"Name": "'IDR'", "SID": "'sidTableCurrency14'"},    # Indonesia Rupiah
        {"Name": "'MYR'", "SID": "'sidTableCurrency15'"},    # Malaysia Ringgit
        {"Name": "'PHP'", "SID": "'sidTableCurrency16'"},    # Philippines Peso
        {"Name": "'SGD'", "SID": "'sidTableCurrency17'"},    # Singapore Dollar
        {"Name": "'MOP'", "SID": "'sidTableCurrency18'"},    # Macau Pataca
        {"Name": "'LKR'", "SID": "'sidTableCurrency19'"}     # Sri Lanka Rupee
    ]
}
