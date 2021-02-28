import winsound

from scipy.signal import butter, lfilter
import numpy as np
from scipy import fft
from scipy.io import wavfile



# Function to Decode by forier frequancy Transform
def decode_fft(y_data, chars, letters, fs=44000):
    sample_length = len(y_data)

    T = 0.04
    N = int(fs * T)
    step = N

    start = 0
    end = N
    decoded_sting = ''
    for c in range(0, int(sample_length / step)):

        z = y_data[start:end]
        yf = fft(z)
        start += step
        end += step

        index = int(fs / step)
        freq = []

        for i in range(5, int(len(yf))):
            if int(abs(yf[i])) > 1:
                freq.append(i * index)

        for i in range(0, 26): # 26 is the number of charachter from a-z im define it in GUI2
            if (int(chars[0][letters[i]]) == freq[0]) & (int(chars[1][letters[i]]) == freq[1]) & ( #char[0]letter[0]==a and his frequancy in low
                    int(chars[2][letters[i]]) == freq[2]):
                decoded_sting += letters[i]

    return decoded_sting

#decoding using Band pass filter
def decode_BPF(y_data, chars, letters, fs=44000):
    sample_length = len(y_data)
    T = 0.04
    N = int(fs * T)
    step = N
    start = 0
    end = N
    decoded_sting = ''
    low_frequencies = [400, 600, 800] # give the best 3 low frequancy
    middle_frequencies = [1000, 1200, 1500]# give the best 3 MID frequancy
    high_frequencies = [2000, 3000, 4000]# give the best 3 HIGH frequancy

    for c in range(0, int(sample_length / step)):

        for f in low_frequencies:
            if check_freq(y_data, f, start, end):
                low = f

        for f in middle_frequencies:
            if check_freq(y_data, f, start, end):
                middle = f

        for f in high_frequencies:
            if check_freq(y_data, f, start, end):
                high = f

        for i in range(0, 26):
            if (int(chars[0][letters[i]]) == low) & (int(chars[1][letters[i]]) == middle) & (
                    int(chars[2][letters[i]]) == high):
                decoded_sting += letters[i]

        start += step
        end += step

    return decoded_sting


def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a


def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y


def BPF(y_data, center, start, end):
    lowcut = center - 50
    highcut = center + 50
    fs = 44000.0
    for order in [3, 6, 9]:
        b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    x = y_data[start:end]
    y = butter_bandpass_filter(x, lowcut, highcut, fs, order=6)
    return y


def check_freq(y_data, center, start, end):
    y = BPF(y_data, center, start, end)
    z = np.array(y)
    yf = fft(z)
    # my_plot_2(yf)

    for k in range(0, int(len(yf) / 2)):
        if int(abs(yf[k])) > 100:
            if k * 25 > center - 10 & k * 25 < center + 10:
                return True
    return False

#Fuction to read a wav signal and save in array Y_data
def read_wav_signal(file_name):
    rate, data = wavfile.read(file_name)
    y_data = []
    length = len(data)
    for i in range(0, length):
        y_data.append(0.019961328125 * data[i] - 2.090138671875)
    y_data = np.array(y_data, dtype=float)

    return y_data

