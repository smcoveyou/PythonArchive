# DB CONNECT - Python v3.6.2
# Author: Seth Coveyou      Owner: Cytherian LLC
#
# OBJ: Pre-defined commands to be used in dcmain to query and manipulate
#       data in the chosen Microsoft Access Database. Edit line 15 "connection ="
#       to change the DB being utilized.
#
# BEGIN SCRIPT:

#!/usr/bin/python

import pypyodbc

#Create connection
connection = pypyodbc.connect('DRIVER={Driver do Microsoft Access (*.mdb)};UID=admin;UserCommitSync=Yes;Threads=3;SafeTransactions=0;PageTimeout=5;MaxScanRows=8;MaxBufferSize=2048;FIL={MS Access};DriverId=25;DefaultDir=C:/Users/BK/Documents/Python;DBQ=C:/Users/BK/Documents/Python/All Covered_Aurora, IL.mdb;')
#Create cursor
cursor = connection.cursor()

#BEGIN COMMANDS
class command():
    def getCableLengths():
