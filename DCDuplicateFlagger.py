#!/usr/bin/python
import re

regex = r"(\d+)\s(R\d.U\d+)\s(\S*)\s(\S*)\s(\S*)"

def flag(x,y):
    x=x
    y=y
    #Get name of complete data file for read in
    filename = input("Enter file path")
    #Open the named file for reading
    fileRead = open("filename","r")
    #Open another file to right the flagged connections to
    fileWrite = open("FlaggedConnections.txt","a")
    #Find length of fileRead
    fileReadLength = sum (1 for line in file)
    #Read through file and find lines that start with flagged IDs.
    #Print those lines to fileWrite (FlaggedConnections.txt)
    for i in range (0,fileReadLength):
        if line.startswith(x,y):
            fileWrite.write(line)
    #Close both files
    fileRead.close()
    fileWrite.close()

#filename = input("Enter file path")
fileRead = open("C:\\Users\\BK\\Documents\\Python\\NW1DataIndex.txt","r")

strIDArray=[]
strSourceArray=[]
strTargetArray=[]

for line in fileRead:
    for i in range(len(line)):
        #Append each array for another index/value
        strIDArray.append(i)
        strSourceArray.append(i)
        strTargetArray.append(i)
        #import the line and convert to string
        strLine = str(line)
        #Group 1 of the line string is the ID of the line
        strIDArray[i] = re.sub(regex,"\\1",strLine, 0)
        #Group 2 of the line string is the source cabinet
        #and Group 3 is the source port
        strSourceArray[i] = re.sub(regex,"\\2 \\3",strLine,0)
        #Group 4 of the line string is the target cabinet
        #and Group 5 is the target port
        strTargetArray[i] = re.sub(regex,"\\4 \\5",strLine,0)

        #print (strIDArray[i]+strSourceArray[i]+strTargetArray[i])

    for x in range(strSourceArray):
        for y in range(strTargetArray):
            if strSourceArray[x] == strTargetArray[y]:
                print(strIDArray[x])
