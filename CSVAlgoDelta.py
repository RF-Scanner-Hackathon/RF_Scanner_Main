##Author Sean Vassi 2023
import csv
import sys
##ANDREW!!!!!!!!!!!!!
##Look up NumPy for the libraries for the 2D array
import numpy
import math




#file = sys.argv[1] + ".csv" #CSV File
#rowsToCheck = int(sys.argv[2]) #Amount of Rows that will be computed for the average
#transLengthThreshhold = int(sys.argv[3]) #in the return of function createEdges(), Will show edges higher or equal to this number (EX"  if number is "5", (2-4 Distance (2) NOT SHOWN (4-10 DIstance 6)) SHOWN)
#file = "" #CSV File
#rowsToCheck = 0#Amount of Rows that will be computed for the average
#transLengthThreshhold = 0 #in the return of function createEdges(), Will show edges higher or equal to this number (EX"  if number is "5", (2-4 Distance (2) NOT SHOWN (4-10 DIstance 6)) SHOWN)
noiseFloor = 0
maxTranmission = 0
CSVMatrix = []
aboveAverageRowNumber = 0
tranLengthAverage = 0
tranLengthGreatestDist = 0
traceTimeCalcVar = 62.4

##Function that will return the number of the row it belives to be above average
##Average range will take in how many rows to calulate for the average
def findAboveAverage(averageRange):
    runningTotal = 0
    burstDifference = 0
    rows = 0
    column = 0
    highRow = 0
    currentAverage = 0
    highAverage = 0
    lowAverage = 0
    midAverage = 0
    averageDivisor = 0
    middleColumn = 0
    maxFails = 0
    maxFailPercentage = 0.5
    averageThreshholdIncreasePercentage = 0
    passBoolean = False
    columnLength = numpy.size(CSVMatrix,0) ##length of columns (Vertically)
    print(columnLength)
    #rowCheckRange = (numpy.size(CSVMatrix,0) / 2) ##Amount of rows / 2
    rowCheckRange = (numpy.size(CSVMatrix,1) / 2) ##Amount of columbs / 2
    middleColumn = int(rowCheckRange) #WIll start in the middle of the CVS tranmission
    print(numpy.size(CSVMatrix,1))
    print(middleColumn)
    if rowCheckRange > 100:
        rowCheckRange = 100

    if (rowCheckRange/2) + middleColumn >= numpy.size(CSVMatrix,1):
        rowCheckRange = columnLength - rowCheckRange


    if(averageRange > columnLength): ##error avoidence
        averageRange = columnLength
    rowCheckRange = int(rowCheckRange)
    print("column check range =",end=" ")
    print(rowCheckRange)
    maxFails = rowCheckRange * maxFailPercentage
    returningHighRowsList = []
    burstDif = []
    averageSmallBucket=[]
    Minaverage = []
    highAverageBucket = []
    #[row][column]
    #The number in range() is how many numbers it takes into account for the average.
    #the larger the better but it also will be more costly

    testVar = 0
    for y in range(averageRange):
        #currentIndex = numpy.absolute(CSVMatrix[middleColumn][y])
        currentIndex = CSVMatrix[y][middleColumn]
        runningTotal = runningTotal + currentIndex
        averageSmallBucket.append(currentIndex)
        if(len(averageSmallBucket) % 5 == 0):
            global maxTranmission
            averageSmallBucket.sort()
            #averageSmallBucket.reverse() ## **will pop the smallest number, comment to reverse to remove largest number
            tempHighest = averageSmallBucket.pop()
            testVar = testVar + 1
            highAverageBucket.append(tempHighest)
            #will check the popped number (The highest) for the maximum tranmission value
            if((tempHighest > maxTranmission) or (maxTranmission == 0)):
                maxTranmission = tempHighest
            highAverageBucket.append(averageSmallBucket.pop())
            Minaverage.append(sum(averageSmallBucket) / len(averageSmallBucket))
            averageSmallBucket.clear()




    midAverage = numpy.round(runningTotal / averageRange, 4)
    lowAverage = numpy.round(sum(Minaverage) / len(Minaverage),4) #When above is commented out **
    mixedAverage = numpy.round((midAverage + lowAverage)/2,4)
    highAverage = numpy.round(sum(highAverageBucket) / len(highAverageBucket),4)
    global noiseFloor
    ##Establishes a noise floor value
    noiseFloor = lowAverage

    averageThreshholdIncreasePercentage = numpy.round(lowAverage / ((highAverage + mixedAverage) / 2), 4)
    currentAverage = highAverage

    #currentAverage = highAverage
    print("average = ")
    print(currentAverage)
    print("Low Average, Mid Average, Mixed Average, High Average, Max Trans, Transmission Threshold edge percentage")
    print(lowAverage)
    print(midAverage)
    print(mixedAverage)
    print(highAverage)
    print(getMaxTranmission())
    print(averageThreshholdIncreasePercentage)
    print("MAX fails")
    print(maxFails)
    passBoolean = False
    edgeBoolean = False
    rows = int(0)

    #Checks the top row
    for y in range(columnLength):
        passBoolean = False
        if isCloseCustom(CSVMatrix[y][middleColumn],currentAverage) or (CSVMatrix[y][middleColumn] > currentAverage):
            currentAverage = midAverage
            fail = 0
            # if it finds a potential row, checks a few y values
            for x in range(rowCheckRange):
                testBool = False
                if isCloseCustom(CSVMatrix[y][checkRowOffset(x) + middleColumn],currentAverage) or (CSVMatrix[y][checkRowOffset(x) + middleColumn] > currentAverage):
                    passBoolean = True
                else:
                    fail = fail + 1

                    if(fail > maxFails):
                        passBoolean = False
                        fail = 0
                        break
            if passBoolean:
                if edgeBoolean:
                    pass
                else:
                    edgeBoolean = True
                    returningHighRowsList.append(y)
                    #break
            else:
                if edgeBoolean:
                    lastElement = int(returningHighRowsList.pop())
                    if lastElement != y - 1:
                        returningHighRowsList.append(lastElement)
                        returningHighRowsList.append('-')
                        returningHighRowsList.append(y-1)
                        edgeBoolean = False
                        currentAverage = highAverage
                    else:
                        #print("single Row")
                        returningHighRowsList.append(lastElement)
        else:

            if edgeBoolean:

                lastElement = int(returningHighRowsList.pop())
                if lastElement != y - 1:
                    returningHighRowsList.append(lastElement)
                    returningHighRowsList.append('-')
                    returningHighRowsList.append(y-1)
                    edgeBoolean = False
                    currentAverage = highAverage
                else:

                    returningHighRowsList.append(lastElement)
            else:
                pass

        if CSVMatrix[y][middleColumn] > maxTranmission:
            maxTranmission = CSVMatrix[y][middleColumn]
        checkRowOffsetReset()
        edgeBoolean = passBoolean


    if edgeBoolean:
        lastElement = int(returningHighRowsList.pop())
        returningHighRowsList.append(lastElement)
        returningHighRowsList.append('-')
        returningHighRowsList.append(y)
        edgeBoolean = False

    return returningHighRowsList


class edge:
    distance = 0
    def __init__(self,start,end):
        self.start = start
        self.end = end
        self.distance = end - start

    def __str__(self):
        returnString = str(self.start)
        returnString += '-'
        returnString += str(self.end)
        returnString += "(Distance:"
        returnString += str(self.distance)
        returnString += ")"
        return returnString

    def combineEdgePrevious(self, otherEdge):
        self.start = otherEdge.start
        self.distance = self.end - self.start

    def returnData(self):
        returnList = []
        returnList.append(self.start)
        returnList.append(self.end)
        returnList.append(self.distance)
        return returnList






rowOffsetIterate = 0
returnNeg = False
lastInputCheckRowOffset = 0
def checkRowOffset(input):
    global lastInputCheckRowOffset
    global returnNeg
    global rowOffsetIterate
    if rowOffsetIterate == 0:
        rowOffsetIterate = 1
        lastInputCheckRowOffset = input
        returnNeg = True
        return 1

    if returnNeg:
        if lastInputCheckRowOffset != input:
            returnNeg = not returnNeg
        return rowOffsetIterate * -1
    else:
        if lastInputCheckRowOffset != input:
            returnNeg = not returnNeg
            rowOffsetIterate += 1
        return rowOffsetIterate


def checkRowOffsetReset():
    global rowOffsetIterate
    global lastInputCheckRowOffset
    rowOffsetIterate = 0
    lastInputCheckRowOffset = 0
#}
def checkRowOffsetTest():
    for x in range(20):
        print(checkRowOffset(x))


def isCloseCustom(a, b, rel_tol=1e-09, abs_tol=0.0):
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

## Needs a major overhaul depending on sampling rate. DO TESTS!!!
def getTraceTime():
    return numpy.round(numpy.size(CSVMatrix,0) / traceTimeCalcVar,4)

def getMaxTranmission():
    return numpy.round(maxTranmission)

def getNoiseFloor():
    return numpy.round(noiseFloor, 4)

def getTranLengthAverage():
    return numpy.round(tranLengthAverage, 4)

def getTranLengthBroadcast():
    return numpy.round(tranLengthGreatestDist,4)

def getTranmissionNoiseDifference():
    return numpy.round(getMaxTranmission()/getNoiseFloor(),4)

def getSecondsFromRows(rowDistance):
    return numpy.round(rowDistance / traceTimeCalcVar,4)

def createEdges(numberList,transLengthThreshhold):
    global tranLengthGreatestDist
    global tranLengthAverage
    tranAverage = []
    returnEdgeList = []
    distance = 0
    lastNumber = 0
    edgeBoolean = False
    for i in numberList:
        if i == '-':
            edgeBoolean = True

        elif edgeBoolean:
            distance = (i - lastNumber) + 1
            edgeTemp = edge(lastNumber,i)
            if(len(returnEdgeList) != 0):
                lastEdge = returnEdgeList.pop()
                if edgeTemp.start - lastEdge.end <= 10:
                    edgeTemp.combineEdgePrevious(lastEdge)
                else:
                    returnEdgeList.append(lastEdge)

            returnEdgeList.append(edgeTemp)
            #if(edgeTemp.distance >=10):
            tranAverage.append(edgeTemp.distance)
            if edgeTemp.distance > tranLengthGreatestDist:
                tranLengthGreatestDist = edgeTemp.distance

            distance = 0
            lastNumber = i
            edgeBoolean = False



        else:
            lastNumber = i

    if len(tranAverage) == 0:
        print("Trans Average Error")
    else:
        tranLengthAverage = sum(tranAverage) / len(tranAverage)
    return returnEdgeList

def printEdges(edgeList):
    print("Printing List")
    for index in edgeList:
        if(index.distance >= transLengthThreshhold):
            print(index)

    print("transmission Length Average")
    print(getTranLengthAverage())



## EXECUTION BEGINS HERE ##

#Open the CSV file and read it, place it in a 2D array
#CSVMatrix = numpy.array(x).astype("float") #Must be float, our numbers for the actual CSV files are floats!
def start(fileName, rows, lengthThreshhold):
    global CSVMatrix
    global file
    global rowsToCheck
    global transLengthThreshhold
    file = fileName
    rowsToCheck = rows
    transLengthThreshhold = lengthThreshhold
    CSVMatrix = numpy.genfromtxt(file,delimiter=',', dtype=float,invalid_raise=False)
    CSVMatrix = numpy.delete(CSVMatrix,4096,1)
##!! CSVMatrix IS A 2D MATRIX :) yay!
    print(CSVMatrix) ##Print the full matrix
##AboverAverageRowNumber is list
    aboveAverageRowNumber = findAboveAverage(rowsToCheck)
    edgeList = []
    edgeList = createEdges(aboveAverageRowNumber,transLengthThreshhold)
    #print(edgeList)
    printEdges(edgeList)
    mainTest()


#print(aboveAverageRowNumber)
def mainTest():
    print(" ")
    print("Noise Floor")
    print(noiseFloor)
    print("Trace Time (Seconds)")
    print(getTraceTime())
    print("Max Tranmission")
    print(getMaxTranmission())
    print("Tranmission / Noise Difference")
    print(getTranmissionNoiseDifference())
    print("Average Burst Length")
    print(getTranLengthAverage())
    print("Ave Burst Length in Seconds")
    print(getSecondsFromRows(getTranLengthAverage()))
    print("Broadcast / Longest Burst Recorded")
    print(getTranLengthBroadcast())
    print("Broadcast / Longest Burst in sec")
    print(getSecondsFromRows(getTranLengthBroadcast()))
    #print(checkRowOffsetTest())

#start(file, rowsToCheck, transLengthThreshhold)
#mainTest()
#print(len(aboveAverageRowNumber))
#print("out of")
#print(numpy.size(CSVMatrix,1))
