import sys
sys.path.append("..")
import PDBConst

pdbDB = {
    #############################################
    # User DB description should be added below #
    #############################################

    "ej": {
        "config": {
            PDBConst.pdbSchema: {
                "Name": ["varchar(128)", "not null", "primary key"],
                "Value": ["varchar(128)"]
            },
            PDBConst.pdbValues: [
                {"Name": "'version'", "Value": "'0.1'"}
            ]
        },
        
        "paymentmode": {
            PDBConst.pdbSchema: {
                "ID": ["tinyint", "not null", "primary key"],
                "Name": ["varchar(128)", "not null"],
                "SID": ["varchar(128)", "not null"]
            },
            PDBConst.pdbValues: [
                {"Name": "'Credit Card'", "ID": "1", "SID": "'sidTablePaymentmode1'"},
                {"Name": "'Cash'", "ID": "2", "SID": "'sidTablePaymentmode2'"},
                {"Name": "'Alipay'", "ID": "3", "SID": "'sidTablePaymentmode3'"},
                {"Name": "'WeChat Wallet'", "ID": "4", "SID": "'sidTablePaymentmode4'"},
                {"Name": "'Other'", "ID": "100", "SID": "'sidOther'"}
            ]
        },
        
        "billscene": {
            PDBConst.pdbSchema: {
                "ID": ["tinyint", "not null", "primary key"],
                "Name": ["varchar(128)", "not null"],
                "SID": ["varchar(128)", "not null"]
            },
            PDBConst.pdbValues: [
                {"Name": "'Online Shopping'", "ID": "1", "SID": "'sidTableBillscene1'"},
                {"Name": "'Supermarket'", "ID": "2", "SID": "'sidTableBillscene2'"},
                {"Name": "'Restaurant'", "ID": "3", "SID": "'sidTableBillscene3'"},
                {"Name": "'Mall'", "ID": "4", "SID": "'sidTableBillscene4'"},
                {"Name": "'Cafe'", "ID": "5", "SID": "'sidTableBillscene5'"},
                {"Name": "'Automatic'", "ID": "6", "SID": "'sidTableBillscene6'"},
                {"Name": "'Roadside Stall'", "ID": "7", "SID": "'sidTableBillscene7'"},
                {"Name": "'Gas Station'", "ID": "8", "SID": "'sidTableBillscene8'"},
                {"Name": "'Parking Lot'", "ID": "9", "SID": "'sidTableBillscene9'"},
                {"Name": "'Tourist Attraction'", "ID": "10", "SID": "'sidTableBillscene10'"},
                {"Name": "'Toll Station'", "ID": "11", "SID": "'sidTableBillscene11'"},
                {"Name": "'Theater'", "ID": "12", "SID": "'sidTableBillscene12'"},
                {"Name": "'Hospital'", "ID": "13", "SID": "'sidTableBillscene13'"},
                {"Name": "'Bookstore'", "ID": "14", "SID": "'sidTableBillscene14'"},
                {"Name": "'4S'", "ID": "15", "SID": "'sidTableBillscene15'"},
                {"Name": "'Fair'", "ID": "16", "SID": "'sidTableBillscene16'"},
                {"Name": "'Traffic Net'", "ID": "17", "SID": "'sidTableBillscene17'"},
                {"Name": "'Salon'", "ID": "18", "SID": "'sidTableBillscene18'"},
                {"Name": "'Hotel'", "ID": "19", "SID": "'sidTableBillscene19'"},
                {"Name": "'Other'", "ID": "100", "SID": "'sidOther'"}
            ]
        },
        
        "currency": {
            PDBConst.pdbSchema: {
                "ID": ["tinyint", "not null", "auto_increment", "primary key"],
                "Name": ["char(3)", "not null"],
                "SID": ["varchar(128)", "not null"]
            },
            PDBConst.pdbValues: [
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
        },
        
        "billcategory": {
            PDBConst.pdbSchema: {
                "ID": ["tinyint", "not null", "primary key"],
                "Name": ["varchar(128)", "not null"],
                "SID": ["varchar(128)", "not null"]
            },
            PDBConst.pdbValues: [
                {"Name": "'Diet'", "ID": "1", "SID": "'sidTableBillcategory1'"},
                {"Name": "'Dress'", "ID": "2", "SID": "'sidTableBillcategory2'"}, 
                {"Name": "'Traffic'", "ID": "3", "SID": "'sidTableBillcategory3'"},
                {"Name": "'Living'", "ID": "4", "SID": "'sidTableBillcategory4'"},
                {"Name": "'Communication'", "ID": "6", "SID": "'sidTableBillcategory6'"},
                {"Name": "'Pet'", "ID": "7", "SID": "'sidTableBillcategory7'"},
                {"Name": "'Entertainment'", "ID": "8", "SID": "'sidTableBillcategory8'"},
                {"Name": "'Sports'", "ID": "9", "SID": "'sidTableBillcategory9'"},
                {"Name": "'Travel'", "ID": "10", "SID": "'sidTableBillcategory10'"},
                {"Name": "'Education'", "ID": "11", "SID": "'sidTableBillcategory11'"}, 
                {"Name": "'Healthy'", "ID": "12", "SID": "'sidTableBillcategory12'"},
                {"Name": "'Sociality'", "ID": "13", "SID": "'sidTableBillcategory13'"},
                {"Name": "'Reside'", "ID": "17", "SID": "'sidTableBillcategory17'"},
                {"Name": "'Other'", "ID": "100", "SID": "'sidOther'"}
            ]
        },
        
        "incomecategory": {
            PDBConst.pdbSchema: {
                "ID": ["tinyint", "not null", "primary key"],
                "Name": ["varchar(128)", "not null"],
                "SID": ["varchar(128)", "not null"]
            },
            PDBConst.pdbValues: [
                {"Name": "'Salary'", "ID": "1", "SID": "'sidTableIncomecategory1'"},
                {"Name": "'Lucky Money'", "ID": "2", "SID": "'sidTableIncomecategory2'"},
                {"Name": "'Bonus'", "ID": "3", "SID": "'sidTableIncomecategory3'"},
                {"Name": "'Annual Bonus'", "ID": "4", "SID": "'sidTableIncomecategory4'"}, 
                {"Name": "'Other'", "ID": "100", "SID": "'sidOther'"}
            ]
        },
        
        "bill": {
            PDBConst.pdbSchema: {
                "ID": ["int", "not null", "auto_increment", "primary key"],
                "PID": ["int", "not null"],
                "Datetime": ["datetime", "not null"],
                "Amount": ["double(12,2)", "not null"],
                "Currency": ["tinyint", "not null", "default 1"],
                "Category": ["tinyint"],
                "Scene": ["tinyint"],
                "PaymentMode": ["tinyint"],
                "Note": ["varchar(255)"]
            }
        },

        "income": {
            PDBConst.pdbSchema: {
                "ID": ["int", "not null", "auto_increment", "primary key"],
                "PID": ["int", "not null"],
                "Datetime": ["datetime", "not null"],
                "Amount": ["double(12,2)", "not null"],
                "Currency": ["tinyint", "not null", "default 1"],
                "Category": ["tinyint"],
                "Note": ["varchar(255)"]
            }
        },

        "family": {
            PDBConst.pdbSchema: {
                "ID": ["int", "not null", "auto_increment", "primary key"],
                "Name": ["varchar(128)", "not null"]
            },
            PDBConst.pdbValues: [
                {"Name": "\"E&J\'s\""}
            ]
        },

        "person": {
            PDBConst.pdbSchema: {
                "ID": ["int", "not null", "auto_increment", "primary key"],
                "FID": ["int", "not null"],
                "Name": ["varchar(128)", "not null"],
                "Sex": ["tinyint", "not null"],
                "Role": ["tinyint", "not null"]
            },
            PDBConst.pdbValues: [
                {"Name": "'Joan'", "FID": "1", "Sex": "0", "Role": "0"},
                {"Name": "'Ed'", "FID": "1", "Sex": "1", "Role": "1"}
            ]
        },

        "financeevent": {
            PDBConst.pdbSchema: {
                "ID": ["int", "not null", "auto_increment", "primary key"],
                "FID": ["int", "not null"],
                "Name": ["varchar(128)", "not null"],
                "Budget": ["double(12,2)", "not null"],
                "Note": ["varchar(255)"]
            }
        },
        
        "mapbillfinanceevent": {
            PDBConst. pdbSchema: {
                "Bill": ["int", "not null"],
                "Event": ["int", "not null"],
                "PRIMARY KEY": ["Bill", "Event"] 
            }
        },

        "debt": {
            PDBConst.pdbSchema: {
                "ID": ["int", "not null", "auto_increment", "primary key"],
                "FID": ["int", "not null"],
                "Start": ["datetime", "not null"],
                "End": ["datetime", "not null"],
                "Amount": ["double(12,2)", "not null"],
                "Balance": ["double(12,2)"],
                "Note": ["varchar(255)"]
            }
        }
    } 
    
    #############################################
    # User DB description should be added above #
    #############################################
}
