#!/usr/bin/python

import pypyodbc

#Create connection
connection = pypyodbc.connect('DRIVER={Driver do Microsoft Access (*.mdb)};UID=admin;UserCommitSync=Yes;Threads=3;SafeTransactions=0;PageTimeout=5;MaxScanRows=8;MaxBufferSize=2048;FIL={MS Access};DriverId=25;DefaultDir=C:/Users/BK/Documents/Python;DBQ=C:/Users/BK/Documents/Python/All Covered_Aurora, IL.mdb;')
#Create cursor
cursor = connection.cursor()
#Create commands
class command():
    def printMdf(self):
        #Create Query
        cursor.execute('SELECT [First Node Cabinet], [First Node Item], [First Node Port], [Last Node Cabinet], [Last Node Item], [Last Node Port] FROM Table1')

        #Format
        print('\n\n\n')
        print('A Cab#\t    A Device  A Port\t B Cab#\t   B Device\tB Port')

        for row in cursor.fetchall():
            print('--------------------------------------------------------------------------------------------------------')
            for field in row:
                print(field, end="\t")
            print('\n')
        print('\n\n\n')
    def printCab(self):
        cabnum = input("Enter the cabinet number: ")
        #Create Query
        cursor.execute('SELECT [First Node Cabinet], [First Node Item], [First Node Port], [Last Node Cabinet], [Last Node Item], [Last Node Port] FROM Table1 WHERE [First Node Cabinet]='+cabnum)
        #Format
        print('\n\n\n')
        print('A Cab#\t\tA Device\t\tA Port\t\tB Cab#\t\tB Device\t\tB Port')
        for row in cursor.fetchall():
         print('--------------------------------------------------------------------------------------------------------')
         for field in row:
             print(field, end="\t\t")
         print('\n')
        print('\n\n\n')

exit = False;
exitCount = 0;
newcommand = command();

while exit == False:
    print('\n\n')
    cmd = input("Ready for next command: ")
    if cmd == "exit":
        print("Program will close. \n  Closing...")
        exit = True;
        #Close connection to unlock database
        connection.close()
    elif cmd == "printmdf":
        newcommand.printMdf()
    elif cmd == "printcab":
        newcommand.printCab()
    else:
        if exitCount == 0:
            print('\n\n')
            print("ERROR: " + cmd + " is not a valid command. 3 more wrong commands and the program will close. \nYou may close sooner with the command \'exit\'.")
            exitCount = exitCount+1

        elif exitCount == 1:
            print('\n\n')
            print("ERROR: " + cmd + " is not a valid command. 2 more wrong commands and the program will close. \nYou may close sooner with the command \'exit\'.")
            exitCount = exitCount+1

        elif exitCount == 2:
            print('\n\n')
            print("ERROR: " + cmd + " is not a valid command. 1 more wrong commands and the program will close. \nYou may close sooner with the command \'exit\'.")
            exitCount = exitCount+1

        else:
            print('\n\n')
            print("ERROR: "+ cmd + " is not a valid command. Program will close. \n  Closing...")
            print('\n\n')
            exit = True
