#!/usr/bin/python
import re

#Reverse label regex sub = "\\2<=>\\1"
regexReverse = r"(\S*)<=>(\S*)"
#Seperate ID and Label. Group 1 is ID. Group 2 is Label
regexIndex = r"(\d+)\s(\S*)"

#Open file for read MAKE SURE TO CHANGE BASED ON FILE
fileRead = open("C:\\Users\\BK\\Documents\\NW1Labels.txt","r")

#State string arrays
strIDArray=[]
strLabelArray=[]
strReverseLabelArray=[]

#Create i incrementor for loop
i = 0

#BEGIN FOR LOOP - READ THROUGH FILE LINE BY LINE - APPEND AND ADD DATA TO ARRAYS
for line in fileRead:
    #Append each array for another index/value
    strIDArray.append(i)
    strLabelArray.append(i)
    strReverseLabelArray.append(i)

    #Import line and convert to string
    strLine = str(line)

    #Grab ID for ID array
    strIDArray[i] = re.sub(regexIndex, "\\1", strLine, 0)

    #Grab Label for Label array
    strLabelArray[i] = re.sub(regexIndex, "\\2", strLine, 0)

    #Take Reverse of Label for Reverse label array
    strReverseLabelArray[i] = re.sub(regexReverse,"\\2<=>\\1",strLabelArray[i],0)

    #increment i for next loop
    i+=1

#END OF FOR LOOP
i=1
#BEGIN FOR LOOP - READ THROUGH LABEL ARRAY AND REVERSE LABEL ARRAY AND FIND MATCHES
for x in range(len(strLabelArray)):
    for y in range(len(strReverseLabelArray)):
        if strLabelArray[x] == strReverseLabelArray[y]:
            count = str(i)
            print("DUPLICATION FOUND.\n ID of Duplicate Record: " + strIDArray[y] + "\n Label: " + strLabelArray[x] + "\n Label Copy: " + strLabelArray[y] + "\n\n")
            i += 1
        #END IF
    #END Y FOR LOOP
#END X FOR LOOP
print("Total duplicates = " + count)

#Close fileRead
fileRead.close()
