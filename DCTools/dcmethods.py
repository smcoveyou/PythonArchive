# DC METHODS - Python v3.6.2
# Author: Seth Coveyou      Owner: Cytherian LLC
#
# OBJ: Determine cable lengths between devices based on:
#   1. Cabinet Dimensions
#   2. Port Orientations of Devices (Assuming cables come down on left side of devices)
#   3. Rack Elevation of the Devices
#   4. Measurement from the Ladder Rack to the top of the cabinet and whether
#       the Ladder Rack is in the middle or left/right of cabinet.
#
# BEGIN SCRIPT:

#!/usr/bin/python
import math

#CONSTANTS
CABINET_DIM = [0, 1, 2]
T_CAB_IF = ""
T_CABINET_DIM = [0, 1, 2]
DEV_1_FR = ""
DEV_2_FR = ""
DEV_1_PORT_ORIENT = ""
DEV_2_PORT_ORIENT = ""
DEV_1_RU = 0
DEV_2_RU = 0
LADDER_RACK_HEIGHT = 0
LADDER_RACK_ORIENTATION = ""


# DETERMINE CABINET DIMENSIONS
def cabDimensions ():
    #SET CABINET DIMENSION ARRAY CONST
    CABINET_DIM [0] = input("Enter the height of the cabinet in inches: ")
    CABINET_DIM [1] = input("Enter the depth of the cabinet in inches: ")
    CABINET_DIM [2] = input("How many RUs does the cabinet have?: ")
    #ARE BOTH DEVICES IN THE SAME CABINET?
    T_CAB_IF = input("Are both devices in the same cabinet (y/n)? ")
    #IF THERE IS ANOTHER CABINET -----> GET THAT CABINETS DIMENSIONS
    if T_CAB_IF == "n" or T_CAB_IF == "N":
        T_CABINET_DIM [0] = input("Enter the height of the second cabinet in inches: ")
        T_CABINET_DIM [1] = input("Enter the depth of the second cabinet in inches: ")
        T_CABINET_DIM [2] = input("How many RUs does the second cabinet have?: ")

def portOrientation ():
    #ARE THE PORTS FRONT OR REAR FACING?
    DEV_1_FR = input("Are the ports front or rear facing on device 1 (f/r)?: ")
    DEV_1_FR = DEV_1_FR.upper()
    DEV_2_FR = input("Are the ports front or rear facing on device 2 (f/r)?: ")
    DEV_2_FR = DEV_2_FR.upper()
    DEV_1_PORT_ORIENT = input("What is the orientation of the ports on device 1 (v/h)?: ")
    DEV_1_PORT_ORIENT = DEV_1_PORT_ORIENT.upper()
    DEV_2_PORT_ORIENT = input("What is the orientation of the ports on device 2 (v/h)?: ")
    DEV_2_PORT_ORIENT = DEV_2_PORT_ORIENT.upper()

def rackElevations ():
    #DETERMINE THE RACK ELEVATIONS OF THE DEVICES
    DEV_1_RU = input("What is the rack elevation of device 1?: ")
    if DEV_1_RU > CABINET_DIM [2]:
        print("\n\nERROR! Your input is out of range for the already determined RUS in the cabinet!\n")
        print("You entered " + DEV_1_RU + ", but the maximum number is "+ CABINET_DIM[2] + "\n\n")
        rackElevations()
    DEV_2_RU = input("What is the rack elevation of device 2?: ")
    if T_CAB_IF == "N" or T_CAB_IF == "n":
        if DEV_2_RU > T_CABINET_DIM [2]:
            print("\n\nERROR! Your input is out of range for the already determined RUS in the cabinet!\n")
            print("You entered " + DEV_2_RU + ", but the maximum number is "+ T_CABINET_DIM[2] + "\n\n")
            rackElevations()
    else:
        if DEV_2_RU > CABINET_DIM [2]:
            print("\n\nERROR! Your input is out of range for the already determined RUS in the cabinet!\n")
            print("You entered " + DEV_2_RU + ", but the maximum number is "+ CABINET_DIM[2])
            rackElevations()

def ladderRack ():
    LADDER_RACK_HEIGHT = input("Enter the measurement from the ladderRack to the top of cabinet 1?: ")
    LADDER_RACK_ORIENTATION = input("Enter the orientation of the ladder rack (front/middle/rear): ")
    LADDER_RACK_ORIENTATION = LADDER_RACK_ORIENTATION.upper()
    if LADDER_RACK_ORIENTATION == "FRONT" or "MIDDLE" or "REAR":
        print("\n")
    else:
        print("\n\nERROR! You did not enter an acceptable orientation for the ladder rack.\n")
        print("Please try again. This time enter front, middle or rear.")
        LADDER_RACK_ORIENTATION=""
        ladderRack()

def determineBank (PORT_ORIENT,deviceNumber):
    deviceNumber = str(deviceNumber)
    deviceBank = 0
    if PORT_ORIENT == "V":
        devicePortNumber = input("What is the port number for device " + deviceNumber + "?: ")
        if devicePortNumber in range (1,16):
            deviceBank = 1
        elif devicePortNumber in range (17,32):
            deviceBank = 2
        else:
            deviceBank = 3
        return deviceBank
    else:
        devicePortNumber = input("What is the port number for device " + deviceNumber + "?: ")
        if devicePortNumber in range (1,8):
            deviceBank = 1
        elif devicePortNumber in range (25,32):
            deviceBank = 1
        elif devicePortNumber in range (9,16):
            deviceBank = 2
        elif devicePortNumber in range (33,40):
            deviceBank = 2
        else:
            deviceBank = 3
        return deviceBank

def frCalc(DEV_1_FR, DEV_2_FR):
    if DEV_1_FR == "F":
        if DEV_2_FR == "F":
            #do nothing
        else:
            #add length to total lengths
    else:
        if DEV_2_FR == "R":
            #do nothing
        else:
            #add length to total lengths

def ladderRackCalc(LADDER_RACK_HEIGHT, LADDER_RACK_ORIENTATION):
    if LADDER_RACK_ORIENTATION == "FRONT":
        #DO THIS
    else if LADDER_RACK_ORIENTATION == "MIDDLE":
        #DO THIS
    else:
        #DO THIS
