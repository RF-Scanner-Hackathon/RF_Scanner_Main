# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 14:32:27 2023

@author: Andrew Carvajal
"""
import numpy as np
import matplotlib.pyplot as plot
import codecs
import struct

def firstTen(array):
    for index in range(40):
        print(index,":", array[index])

#Writes ndarray to file
def writeArray(array, newFileName):
    np.savetxt(newFileName, array, fmt='%f', delimiter='\n') #%.4e is complex64 4 bytes
    
#Reads file into complex64 array
def readArray(fileName):
    return np.loadtxt(fileName, dtype='complex64')

def fftAlgorithm(iqArray):
    #Define parameters
    sampleLength = len(iqArray)
    #print('Sample Length', sampleLength)
    fft_size = int(np.power(2,10))
    sampleRate = 1000000
    num_rows = int(sampleLength/fft_size)
    time = 5 #iq file was recorded for 5 seconds
    spectrogram = np.zeros((num_rows, fft_size));
    
    for i in range(num_rows):
        PSD = np.fft.fft(iqArray[i*fft_size:(i+1)*fft_size])
        PSD_shifted = np.fft.fftshift(PSD)
        PSD_log = 20*np.log10(np.abs(PSD_shifted)**2)
        spectrogram[i,:] = PSD_log
        print('array',PSD_log)
        mean = np.sum(PSD_log) / len(PSD_log)
        #print('mean:', mean)
    #mean = np.mean(spectrogram)
   # print('mean:', mean)
    return spectrogram
    
    

def main():

    #Create 1D Array from iq file
    #iqFileName = 'march27Recording.iq'
    iqFileName = 'RTL_1000000.0_K1_02_27_2023_16_00_18.cfile'

    iqFileName = 'RTL_S1_K1.cfile'
    iqArray = np.fromfile(iqFileName, np.complex64)
    iqArray = np.nan_to_num(iqArray, nan=0.00000001)
    #print(iqArray)
    
    #Print first 10 of iq array
    firstTen(iqArray)
    
    #Create Spectrogram
    spectrogram = fftAlgorithm(iqArray)

    #writeArray(spectrogram, 'march27_spectrogram_v02.txt')
    
    #Create Plot
    plot.imshow(spectrogram, aspect='auto')
    plot.xlabel("Frequency HELLO [MHz]")
    plot.ylabel("Time [s]")
    plot.show()    
    print('Main Terminated')



'''
fft_size = 512 #Number of column
num_rows = int(np.floor(sampleLength)/fft_size)
spectrogram = np.zeros((num_rows, fft_size))
samples = samples * np.hamming(sampleLength)
for i in range(num_rows):
    spectrogram[i,:] = 10*np.log10(np.abs(np.fft.fftshift(np.fft.fft(samples[i*fft_size:(i+1)*fft_size])))**2)
print (spectrogram)
'''



#'''


'''


    
    

    

#for i in range(sampleLength):
    #spectrogram[i,:] = 10*np.log10(np.abs(np.fft.fftshift(np.fft.fft(samples[i*fft_size:(i+1)*fft_size])))**2)

print('final type',bytes(spectrogram[0][0]))
 
#print('fft values:\n',arrayToNan)

#10*np.log10(np.abs(np.fft.fftshift(np.fft.fft(samples[i*fft_size:(i+1)*fft_size])))**2)

#print(x)

#Fs = 1000000
#freq = np.fft.fftfreq(sampleLength, 1/Fs)


#plot.plot(freq, np.fft.fft(samples), '.')
#plot.grid(True)
#plot.show()
'''
