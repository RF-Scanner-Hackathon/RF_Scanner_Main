import numpy as np
#import pandas as pd
from scipy import signal
import os

def convertIQtoCSV(iqPath):
    # Read IQ data from file
    iq_data = np.fromfile(iqPath, dtype=np.uint8)

    # Convert to complex array
    iq_data = iq_data.astype(np.complex64)
    iq_data -= 127.5 + 127.5j
    iq_data /= 127.5

    # Split IQ data into real and imaginary parts
    iq_real = np.real(iq_data)
    iq_imag = np.imag(iq_data)

    # Apply Hilbert transform to the real part only
    analytic_signal = signal.hilbert(iq_real)

    # Compute the spectrogram using a Hamming window and 50% overlap
    fs = 1e6  # sample rate
    f, t, psd = signal.spectrogram(np.abs(analytic_signal), fs=fs, nperseg=1024, noverlap=512)

    # Convert PSD values to dB scale
    psd = 10 * np.log10(psd)

    # Store PSD values in 2D array
    psd_array = np.column_stack((t.repeat(len(f)), np.tile(f, len(t)), psd.T.flatten()))

    # Reshape 2D array to match (times, 3) shape
    psd_array = psd.T

    # Save 2D array to CSV file
    file_name = os.path.splitext(os.path.basename(iqPath))[0]
    csv_path = os.path.join(os.path.dirname(iqPath), file_name + '.csv')
    np.savetxt(csv_path, psd_array, delimiter=',', fmt='%.6f')

    # Return absolute file path of CSV file
    return os.path.abspath(csv_path)


def spliceFreq(fileName):
    if(fileName.rfind('/')==-1):
        spliced = fileName.split("_")
        return spliced[2][:-2]
    lastDash = fileName.rfind('/')
    iqFile = fileName[lastDash+1:]
    #print("iqFile: ", iqFile)
    spliced = iqFile.split("_")
    return spliced[2][:-2]




