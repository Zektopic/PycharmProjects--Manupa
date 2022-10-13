import wave
import numpy as np
import struct
import matplotlib.pyplot as plt
frame_rate = 48000.0
infile = "test.wav"
num_samples = 48000
wav_file = wave.open(infile, 'r')
data = wav_file.readframes(num_samples)
wav_file.close()
data = struct.unpack('{n}h'.format(n=num_samples), data)
data = np.array(data)
data_fft = np.fft.fft(data)
frequencies = np.abs(data_fft)
plt.subplot(2,1,1)
plt.plot(data[:300])
plt.title("Original audio wave")
plt.subplot(2,1,2)
plt.plot(frequencies)
plt.title("Frequencies found")
plt.xlim(0,1200)
plt.show()