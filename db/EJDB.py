[
    #############################################
    # User DB description should be added below #
    #############################################

    {
        PDBConst.Name: "ej",
        PDBConst.Tables: [
            ImportFile("TableConfig.py"),
            ImportFile("TablePaymentMode.py"),
            ImportFile("TableCurrency.py"),
            ImportFile("TableBillCategory.py"),
            ImportFile("TableIncomeCategory.py"),
            ImportFile("TableBill.py"),
            ImportFile("TableIncome.py"),
            ImportFile("TableFamily.py"),
            ImportFile("TablePerson.py"),
            ImportFile("TableFinanceEvent.py"),
            ImportFile("TableMapBillFinanceEvent.py"),
            ImportFile("TableDebt.py")
        ]
    }
    
    #############################################
    # User DB description should be added above #
    #############################################
]
