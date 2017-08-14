import os
import sys

thisDir = os.path.split(os.path.realpath(__file__))[0]

pdbDir = os.path.join(thisDir, "../pdb")
sys.path.append(pdbDir)
import PDBConst
from metadata import PDBConfig
from schema import SchemaChecker

w3Dir = os.path.join(thisDir, "../w3")
sys.path.append(w3Dir)
import W3Util

# Check database definition schema first
schemaPath = os.path.join(pdbDir, "PDBSchema.py")
dbDefinitionPath = PDBConfig.pdbDefinitionPath
constPath = os.path.join(pdbDir, "PDBConst.py")
configChecker = SchemaChecker.SchemaChecker(dbDefinitionPath, schemaPath, constPath)
configCheckResult, schema = configChecker.Check()
if not configCheckResult:
    exit("PDB schema check error!")

# Copy DB definition
ejDB = {
    PDBConst.Name: "ej",
    PDBConst.Tables: []
}
for table in schema[0][PDBConst.Tables]:
    tableCopy = {}
    tableCopy[PDBConst.Name] = table[PDBConst.Name]
    tableCopy[PDBConst.Columns] = table[PDBConst.Columns]
    ejDB[PDBConst.Tables].append(tableCopy)

# Generate DB php file
dbPhpPath = os.path.join(thisDir, "../web/php/ejdb.php")
dbPhp = open(dbPhpPath, "w")
dbPhp.write("<?php\n\n")
dbPhp.write("$ejDB = ")
dbPhp.write(W3Util.W3ValueToPHP(ejDB, 1))
dbPhp.write(";\n\n")
dbPhp.write(" ?>")
dbPhp.close()

# Generate DB js file
dbJSPath = os.path.join(thisDir, "../web/js/ejdb.js")
dbJS = open(dbJSPath, "w")
dbJS.write("var ejDB = ")
dbJS.write(W3Util.W3ValueToJS(ejDB, 1))
dbJS.write(";")
dbJS.close()
