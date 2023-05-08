# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 14:56:50 2023

@author: Andrew Carvajal
"""

import numpy as np
import matplotlib.pyplot as plot
import struct
import pandas as pd

from scipy import signal


# Converts .iq File to ndarray
def readIQ(fileName):
    extentionIndex = fileName.rfind(".")
    if fileName[extentionIndex:] == '.cfile':
        return np.fromfile(fileName, dtype=np.complex64)
    return np.fromfile(fileName, dtype=np.uint)



# Writes ndarray to file
def writeArray(array, newFileName):
    return np.savetxt(newFileName, array, delimiter=',')


# Reads file into complex64 array
def readArray(fileName):
    return np.loadtxt(fileName, dtype='uint')

#Reads csv
def readArrayAsMatrix(fileName):
    # return np.genfromtxt(fileName, delimiter=',')
    return np.loadtxt(open(fileName, "rb"), delimiter=",", skiprows=1)

#Takes an iq file
def spliceFreq(fileName):
    if(fileName.rfind('/')==-1):
        spliced = fileName.split("_")
        return spliced[2][:-2]
    lastDash = fileName.rfind('/')
    iqFile = fileName[lastDash+1:]
    #print("iqFile: ", iqFile)
    spliced = iqFile.split("_")
    return spliced[2][:-2]

def convertAlgorithm(array):
    index = 1
    firstRow = array[0:512]
    for elem in array:
        if index < 10:
            I = np.real(elem)  # inphase
            Q = np.imag(elem)  # quadrature
            print(index, ':', I, "+", Q)
            index += 1
    I = np.real(array[0]) #inphase
    Q = np.imag(array[0]) #quadrature
    index = 0
    print("\n\n"+str(index), ':', I,"+", Q)
    power = np.power(I,2) + np.power(Q,2)
    print("pow:",np.power(I,2))
    print("power:",power)
    magnitude = np.sqrt(power)
    print("magnitude:",magnitude)
    phase = np.arctan(Q/I)
    print("Angle:", phase)
    multipliedByBaseband = 5.73e8 * array[0]
    print("Modulated Signal:",multipliedByBaseband)




    '''
        for elem in firstRow:
        real = np.real(elem)
        imag = np.imag(elem)
        print(index, ':', bytes(real), bytes(imag))
        index = index + 1
    '''



def fftAlgorithm(iqArray):
    # Define parameters
    sampleLength = len(iqArray)
    # print('Sample Length', sampleLength)
    fft_size = int(np.power(2, 13))
    sampleRate = 1000000
    num_rows = int(sampleLength / fft_size)
    print("numRows: ", num_rows)
    time = 5  # iq file was recorded for 5 seconds
    spectrogram = np.zeros((num_rows, fft_size));

    for i in range(num_rows):
        PSD = np.fft.fft(iqArray[i * fft_size:(i + 1) * fft_size])
        PSD_shifted = np.fft.fftshift(PSD)
        PSD_log = 10 * np.log10(np.abs(PSD_shifted) ** 2)
        spectrogram[i, :] = PSD_log
        # print('array',PSD_log)
        # mean = np.sum(PSD_log) / len(PSD_log)
    # print('mean:', mean)
    # mean = np.mean(spectrogram)
    # print('mean:', mean)
    return spectrogram

def printTests2():
    fileName = "AndrewCarvajal7641/2023-04-25-16-36-29_rtlsdr_573037735Hz_1000000Sps.iq"
    iqArray = readIQ(fileName)
    spectrogram = fftAlgorithm(iqArray)
    print(spectrogram)
    csvFile = fileName[:len(fileName)-2]+"csv"
    print("changed csvName:",fileName[:len(fileName)-2]+"csv")
    matrix = readArrayAsMatrix(csvFile)
    print("matrix:",matrix)
    scaleCSV(csvFile)

def printTests():
    fileName = 'AndrewCarvajal7641/RTL_1000000.0_K1_02_27_2023_16_00_18.cfile'
    iqArray = readIQ(fileName)
    counter = 1
    convertAlgorithm(iqArray)
    '''
        for x in iqArray:
        if counter < 512:
            print(str(counter) + ":", x)
            counter+=1
    '''

def pandaslmfao():
    iqData = np.fromfile('AndrewCarvajal7641/2023-04-25-16-36-29_rtlsdr_573037735Hz_1000000Sps.iq', dtype='uint')

    iqData = iqData.astype(np.complex64)
    iqData -= 127.5 + 127.5j
    iqData /= 127.5


    real = iqData.real
    imag = iqData.imag

    df = pd.DataFrame({'real':real, 'imag':imag})

    df.to_csv('iqSamples.csv', index=False)
    print(readArrayAsMatrix('iqSamples.csv'))
    displayPSD('iqSamples.csv')

def scaleCSV(fileName):
    df = pd.read_csv(fileName)

    iq_data = df['I'] + 1j * df['Q']
    iq_data /=127.5
    iq_data -= (1 + 1j)

    real = iq_data.real
    imag = iq_data.imag

    df_out = pd.DataFrame({'real':real,'imag':imag})
    df_out.to_csv(fileName, index=False)
    displayPSD(fileName)

def iqToCSV(filePath):

    dot = filePath.rfind('.')
    dash = filePath.rfind('/')

    initialFile = filePath[dash + 1::]                      #test3.iq
    extention = filePath[dot::]                             #.iq

    if (extention == '.csv'):
        return filePath
    else:
        if (dash == -1):
            nameFile = filePath[0:dot]                        #test3.iq or test3.cfile
        else:
            nameFile = filePath[dash + 1:dot]

        csvFile = nameFile + '.csv'                           #test3.csv

        if (dash == -1):
            absolutePath = csvFile
        else:
            parentFolder = filePath[0:dash]  # pwd
            absolutePath = parentFolder + '/' + csvFile  # Whole Path of file

        try:
            open(csvFile,'r')
            return absolutePath
        except:
            iqArray = readIQ(filePath)
            #if(extention == '.iq'):
                #iqArray = np.nan_to_num(iqArray, nan=0.01)
                #Ask the user to process a new csv file??

            spectrogram = fftAlgorithm(iqArray)

            writeArray(spectrogram, absolutePath)

            #displayPSD(spectrogram)

            return absolutePath





def displayPSD(fileName):
    spectrogram = readArrayAsMatrix(fileName)

    #print(spectrogram)

    plot.imshow(spectrogram, aspect='auto')
    plot.xlabel("Frequency [MHz]")
    plot.ylabel("Time [s]")
    plot.show()


# Ready to hit run and reads txt file from same folder
def main():
    #printTests()
    #printTests2()
    #pandaslmfao()
    '''
    anyPath = 'AndrewCarvajal7641/2023-04-25-16-36-29_rtlsdr_573037735Hz_1000000Sps.iq'
    print("input:",anyPath)
    print("it spit:",spliceFreq(anyPath))
    print("Datatype:", type(spliceFreq(anyPath)), "Needs ParseInt")
    '''



    '''
    iqArray = readArrayAsMatrix('AndrewCarvajal7641/Alpha.csv')
    counter = 1
    for x in iqArray[0]:
        counter+=1
        if(x == max(iqArray)):
            print("Max index:",counter)

    '''
    # iqArray = readIQ('march27Recording.iq')
    # iqArray = readIQ('RTL_1000000.0_K1_02_27_2023_16_00_18.cfile')
    # iqArray = readIQ('RTL_S1_K1.cfile')
    # newAbsolute = iqToCSV('C:\\Users\\Disc0 Heavy\\.spyder-py3\\meetingCFILE.cfile')
    # newAbsolute = iqToCSV('C:\\Users\\Disc0 Heavy\\.spyder-py3\\march27Recording.iq')
    # print('new csv Absolute Path:', newAbsolute)

    # displayPSD(newAbsolute)

    # csvArray = fftAlgorithm(iqArray)
    # fileName = 'float32_1.txt'
    # fileName = 'csvK1_02.csv'
    # writeArray(csvArray, fileName)
    # print('type of file: ', type(file))
    # fromFile = readArray(fileName)
    # convertAlgorithm(fromFile)
    # printTests()
    print('\nMain Finished')




