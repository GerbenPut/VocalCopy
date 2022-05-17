import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy.io import wavfile
from pylab import *

def run(filename):
    fs, data = wavfile.read(filename)
    print(".wav file loaded")
    #(TODO: automatically mix stereo file into mono)
    a = data.T[0] # pick the first channel in a stereo file
    print("Normalising track...")
    peak = max(abs(a))
    b=[(ele*32767//peak) for ele in a]
    print("Track normalised")
    time = arange(0, len(a)/fs, 1/fs)
    plt.ylim([-32767, 32767])
    plt.xlim([0, len(a)/fs])
    plt.yticks(arange(-2**15, 2**15+1, 2**13))
    plt.plot(time, b)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.show()
    c = fft(b) # fast fourier transform
    print("Fourier transform successful")
    d = len(c)//2  # you only need half of the fft list (real signal symmetry)
    e = abs(c[:(d-1)])
    for i in e[::d//100]:
        print(round(i))
    k = arange(len(data)//2-1)
    T = len(k)/fs  # where fs is the sampling frequency
    plt.plot(e, k/T, 'r')
    plt.ylim([20,20000])
    plt.xlim([0, max(e)]) 
    plt.ylabel('Frequency (Hz)')
    plt.xlabel('Magnitude')
    plt.show()

file = input('bestandsnaam: ')
if not file.endswith('.wav'):
    file += '.wav'
run(file)
