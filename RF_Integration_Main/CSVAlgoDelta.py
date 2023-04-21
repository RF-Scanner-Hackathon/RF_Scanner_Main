##Author Sean Vassi 2023
import csv
import sys
##ANDREW!!!!!!!!!!!!!
##Look up NumPy for the libraries for the 2D array
import numpy
import math




#file = sys.argv[1] + ".csv" #CSV File
#rowsToCheck = int(sys.argv[2]) #Amount of Rows that will be computed for the average
#transLengthThreshhold = int(sys.argv[3]) #in the return of function PrintHighrows(), Will show edges higher or equal to this number (EX"  if number is "5", (2-4 Distance (2) NOT SHOWN (4-10 DIstance 6)) SHOWN)
file = "" #CSV File
rowsToCheck = 0#Amount of Rows that will be computed for the average
transLengthThreshhold = 0 #in the return of function PrintHighrows(), Will show edges higher or equal to this number (EX"  if number is "5", (2-4 Distance (2) NOT SHOWN (4-10 DIstance 6)) SHOWN)
noiseFloor = 0
maxTranmission = 0
CSVMatrix = []
aboveAverageRowNumber = 0
tranLengthAverage = 0

##Function that will return the number of the row it belives to be above average
##Average range will take in how many rows to calulate for the average
def findAboveAverage(averageRange):
    runningTotal = 0
    burstDifference = 0
    rows = 0
    column = 0
    highRow = 0
    currentAverage = 0
    lowAverage = 0
    midAverage = 0
    averageDivisor = 0
    middleColumn = 0
    passBoolean = False
    #columnLength = numpy.size(CSVMatrix,1) ##amount of Rows in the matrix
    columnLength = numpy.size(CSVMatrix,0) ##length of columns (Vertically)
    print(columnLength)
    #rowCheckRange = (numpy.size(CSVMatrix,0) / 2) ##Amount of columbs / 2
    rowCheckRange = (numpy.size(CSVMatrix,1) / 2) ##Amount of columbs / 2
    middleColumn = int(rowCheckRange) #WIll start in the middle of the CVS tranmission
    print(numpy.size(CSVMatrix,1))
    print(middleColumn)
    if rowCheckRange > 100:
        rowCheckRange = 100
    if rowCheckRange + middleColumn >= columnLength:
        rowCheckRange = columnLength - rowCheckRange

    #rows = rowCheckRange
    if(averageRange > columnLength): ##error avoidence
        averageRange = columnLength
    rowCheckRange = int(rowCheckRange)
    print("column check range =",end=" ")
    print(rowCheckRange)
    returningHighRowsList = []
    burstDif = []
    averageSmallBucket=[]
    Minaverage = []
    #[row][column]
    #The number in range() is how many numbers it takes into account for the average.
    #the larger the better but it also will be more costly
    #print(CSVMatrix[:, middleColumn])
    #print(CSVMatrix[middleColumn,:])
    for y in range(averageRange):
        #currentIndex = numpy.absolute(CSVMatrix[middleColumn][y])
        currentIndex = numpy.absolute(CSVMatrix[y][middleColumn])
        runningTotal = runningTotal + currentIndex
        averageSmallBucket.append(currentIndex)
        if(len(averageSmallBucket) % 5 == 0):
            global maxTranmission
            averageSmallBucket.sort()
            #averageSmallBucket.reverse() ## **will pop the smallest number, comment to reverse to remove largest number
            tempHighest = averageSmallBucket.pop()
            #will check the popped number (The highest) for the maximum tranmission value
            if(tempHighest > maxTranmission):
                maxTranmission = tempHighest
            averageSmallBucket.pop()
            Minaverage.append(sum(averageSmallBucket) / len(averageSmallBucket))
            averageSmallBucket.clear()




    midAverage = numpy.floor(runningTotal / averageRange)
    lowAverage = numpy.floor(sum(Minaverage) / len(Minaverage)) #When above is commented out **
    mixedAverage = (midAverage + lowAverage)/2
    global noiseFloor
    ##Establishes a noise floor value
    noiseFloor = mixedAverage
    #highAverage = sum(average) / len(average) #Comment out when above is commented in
    #currentAverage = math.ceil(mixedAverage)

    currentAverage = midAverage

    #currentAverage = highAverage
    print("average = ")
    print(currentAverage)
    print("Low Average, Mid Average")
    print(lowAverage)
    print(midAverage)
    passBoolean = False
    edgeBoolean = False
    rows = int(0)

    #Checks the top row
    for y in range(columnLength):
        passBoolean = False
        #column = 0
        #print(x)
        #print(rows)

        #if numpy.absolute(CSVMatrix[middleColumn][x]) > currentAverage:
        #print(CSVMatrix[:][y])
        #print(y)
        #print(middleColumn)
        #[left-Right][Up-Down]
        #print(CSVMatrix[y,:])
        #print("Checking 1 ...")
        #print(middleColumn)
        #print(y)
        #print(numpy.absolute(CSVMatrix[y][middleColumn]))
        #print(">=")
        #print(currentAverage)
        if isCloseCustom(numpy.absolute(CSVMatrix[y][middleColumn]),currentAverage) or (numpy.absolute(CSVMatrix[y][middleColumn]) < currentAverage):
            #print(numpy.absolute(CSVMatrix[middleColumn][x]))
            #currentAverage = lowAverage
            #currentAverage = numpy.floor(lowAverage * 0.70)
            #currentAverage = lowAverage * 0.96
            currentAverage = lowAverage * 1.07
            #rowCheckFormulaOffset = 0

            #currentAverage = lowAverage * 0.70
            #print("LOW AVERAGE")
            #print(currentAverage)
            #will begin calulating rows based on the mid average. This is so if the tranmitter has an off weak
            #signal, will still attempt to account for such
            #currentAverage = midAverage
            #column = x #search this column for numbers
            fail = 0
            # if it finds a potential row, checks a few y values
            for x in range(rowCheckRange):

                #if numpy.absolute(CSVMatrix[x + middleColumn][y]) > float(currentAverage):
                #print("Checking 2 ...")
                #print(x + middleColumn)
                #print(y)
                #print(numpy.absolute(CSVMatrix[y][x + middleColumn]))
                #print(">=")
                #print(currentAverage)
                #if isCloseCustom(numpy.absolute(CSVMatrix[y][x + middleColumn]),currentAverage):
                    #print("Custom Passed")
                #if numpy.absolute(CSVMatrix[y][x + middleColumn]) > currentAverage:
                    #print("normal > Passed")
                checkRowOffsetReset()
                testBool = False
                #if isCloseCustom(numpy.absolute(CSVMatrix[y][checkRowOffset(x) + middleColumn]),currentAverage) or (numpy.absolute(CSVMatrix[y][checkRowOffset(x) + middleColumn]) < currentAverage):
                if isCloseCustom(numpy.absolute(CSVMatrix[y][x + middleColumn]),currentAverage) or (numpy.absolute(CSVMatrix[y][x + middleColumn]) < currentAverage):
                    #print(numpy.absolute(CSVMatrix[y][x + middleColumn]))
                    #print("Higher than")
                    #print(currentAverage)
                #if numpy.absolute(CSVMatrix[y][x + middleColumn]) > currentAverage:
                    passBoolean = True
                else:
                    fail = fail + 1
                    if(fail > (rowCheckRange / 0.5)):

                        passBoolean = False
                        fail = 0
                        #break


                if passBoolean:
                    #print("passBoolean True")
                    if edgeBoolean:
                        pass
                    else:
                        #print("passBoolean False")
                        #print("adding")
                        #print(y)
                        edgeBoolean = True
                        returningHighRowsList.append(y)
                        break
        else:
            #print(numpy.absolute(CSVMatrix[y][middleColumn]))
            #print("Lower than")
            #print(currentAverage)

            if edgeBoolean:
                #print("Edge boolean was true")
                lastElement = int(returningHighRowsList.pop())
                if lastElement != y - 1:
                    returningHighRowsList.append(lastElement)
                    returningHighRowsList.append('-')
                    returningHighRowsList.append(y-1)
                    edgeBoolean = False
                    currentAverage = midAverage
                else:
                    #print("single Row")
                    returningHighRowsList.append(lastElement)
            else:
                pass

                #print("Edge boolean was false")

        edgeBoolean = passBoolean
        #print("edgeBoolean")
        #print(edgeBoolean)
    #print("edgeBoolean")
    #print(edgeBoolean)
    checkRowOffsetReset()
    if edgeBoolean:
        #print("Edge boolean was true")
        lastElement = int(returningHighRowsList.pop())
        returningHighRowsList.append(lastElement)
        returningHighRowsList.append('-')
        returningHighRowsList.append(y)
        edgeBoolean = False

            #print("single Row")

            #highRow = x
            #Would eventually like this to be a list of multuple columns it finds. Will work on this next
            #returningHighRowsList.append(CSVMatrix[0][x])
    #returningHighRowsList.append(currentAverage)
    #number = int(returningHighRowsList.pop)
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
#Couldnt get this to work the way i wanted it to
def returnCol(number):
    return CSVMatrix[:,number]

## Needs a major overhaul depending on sampling rate. DO TESTS!!!
def getTraceTime():
    return numpy.size(CSVMatrix,0) / 510

def getMaxTranmission():
    return maxTranmission

def getNoiseFloor():
    return noiseFloor

def getTranLengthAverage():
    return tranLengthAverage

def printHighRows(numberList,transLengthThreshhold):
    global tranLengthAverage
    tranAverage = []
    returnEdgeList = []
    distance = 0
    lastNumber = 0
    edgeBoolean = False
    for i in numberList:
        if i == '-':
            edgeBoolean = True
            #print(lastNumber,end="-")
            #print(i,end=",")
        elif edgeBoolean:
            distance = (i - lastNumber) + 1
            if(distance >= transLengthThreshhold):
                #print(lastNumber,end='-')
                #print(i,end="(Distance ")
                #print (distance,end=")")
                #print("",end=",")
                edgeTemp = edge(lastNumber,i)
                returnEdgeList.append(edgeTemp)
                tranAverage.append(edgeTemp.distance)
                distance = 0
                lastNumber = i
                edgeBoolean = False

            else:
                edgeBoolean = False

        else:
            lastNumber = i
            #print(i,end=",")
            ##print CSVMatrix[:,i]
    if(len(tranAverage) != 0):
        tranLengthAverage = sum(tranAverage) / len(tranAverage)
    else:
        tranLengthAverage = 0
    return returnEdgeList

def printEdges(edgeList):
    print("Printing List")
    for index in edgeList:
        print(index)

## EXECUTION BEGINS HERE ##

#Open the CSV file and read it, place it in a 2D array
#reader = csv.reader(open("simpleMatrix.csv", "rb"), delimiter=",")
#x = list(reader)
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
##!! CSVMatrix IS A 2D MATRIX :) yay!
#print(CSVMatrix) ##Print the full matrix
#print(CSVMatrix[0][0]) ##Print a index [row][column]
#print(CSVMatrix[1][0])
#print(CSVMatrix[0][1])
##AboverAverageRowNumber is list
    aboveAverageRowNumber = findAboveAverage(rowsToCheck)
    edgeList = []
    edgeList = printHighRows(aboveAverageRowNumber,transLengthThreshhold)
    #print(edgeList)
    printEdges(edgeList)


#print(aboveAverageRowNumber)
def mainTest():
    ##print CSVMatrix[:,aboveAverageRow] ## by using :, it prints the whole column
    #print aboveAverageRowNumber
    #printHighRows(aboveAverageRowNumber,transLengthThreshhold)
    aboveAverageRowNumber = findAboveAverage(rowsToCheck)
    printEdges(printHighRows(aboveAverageRowNumber,transLengthThreshhold))
    print(" ")
    print("Noise Floor")
    print(noiseFloor)
    print("Trace Time (Seconds)")
    print(getTraceTime())
    print("Max Tranmission")
    print(getMaxTranmission())
    #print(checkRowOffsetTest())

#start("test3.csv", 100, 50)
#mainTest()
#print(len(aboveAverageRowNumber))
#print("out of")
#print(numpy.size(CSVMatrix,1))
