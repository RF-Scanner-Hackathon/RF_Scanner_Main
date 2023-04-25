# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 14:56:50 2023

@author: Andrew Carvajal
"""

import numpy as np
import matplotlib.pyplot as plot
import struct


# Converts .iq File to ndarray
def readIQ(fileName):
    #return np.fromfile(fileName, np.complex64)
    return np.fromfile(fileName, dtype=np.uint)



# Writes ndarray to file
def writeArray(array, newFileName):
    return np.savetxt(newFileName, array, delimiter=',')


# Reads file into complex64 array
def readArray(fileName):
    return np.loadtxt(fileName, dtype='complex64')


def readArrayAsMatrix(fileName):
    # return np.genfromtxt(fileName, delimiter=',')
    return np.loadtxt(open(fileName, "rb"), delimiter=",", skiprows=1)


def convertAlgorithm(array):
    index = 1
    firstRow = array[0:512]
    for elem in firstRow:
        real = np.real(elem)
        imag = np.imag(elem)
        print(index, ':', bytes(real), bytes(imag))
        index = index + 1


def fftAlgorithm(iqArray):
    # Define parameters
    sampleLength = len(iqArray)
    # print('Sample Length', sampleLength)
    fft_size = int(np.power(2, 13))
    sampleRate = 1000000
    num_rows = int(sampleLength / fft_size)
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


def printTests():
    print('printTests')
    float32 = np.float32(0)
    print('bytes of float32 0:', bytes(float32))

    string = b'\\x00\\x00\\x00\\x00'
    decoded = string.decode()  # Data type is now String

    fromFloat = struct.pack('f', float32)
    print(fromFloat)

    print('to float32', np.float32(decoded))

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

    print(spectrogram)

    plot.imshow(spectrogram, aspect='auto')
    plot.xlabel("Frequency [MHz]")
    plot.ylabel("Time [s]")
    plot.show()


# Ready to hit run and reads txt file from same folder
def main():
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

# main()


