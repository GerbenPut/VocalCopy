import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy.io import wavfile
from pylab import *
import sys
import csv
import numpy as np

def run(filename):
    fs, data = wavfile.read(filename)
    print(".wav file loaded")
    #(TODO: automatically mix stereo file into mono)
    a = data.T[0] # pick the first channel in a stereo file
    print("Normalising track...")
    peak = max(abs(a))
    b=[(ele*32767//peak) for ele in a]
    print("Track normalised")
    with open('labels.txt', 'r') as f:
        file = [int(i) for i in f.readlines()]
        if file:
            klass = f"{str(max(file)+1)}\n"
        else:
            klass = '0\n'
    loop = len(b)//fs-1
    for i in range(loop):
        print(f'iteration {i} out of {loop} ({i/loop*100}%)')
        arr = b[i*fs:(i+1)*fs]
        with open('ffdata.csv','a') as f:
            ff = fft(arr)
            output = abs(ff[:len(ff)])
            csv.writer(f).writerow(output)
        with open('wavdata.csv', 'a') as f:
            csv.writer(f).writerow(arr)
        with open('labels.txt', 'a') as f:
            f.write(klass)

file = sys.argv[1]
if not file.endswith('.wav'):
    file += '.wav'
run(file)
