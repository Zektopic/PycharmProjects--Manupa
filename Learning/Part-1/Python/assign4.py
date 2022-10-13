import wave
import struct
import numpy as np
import matplotlib.pyplot as plt

#generating orginal audio and noise signals and combining them

frequency = 1000
noisy_freq = 50
num_samples = 48000
sampling_rate = 48000.0
#Create the sine wave and noise
sine_wave = [np.sin(2 * np.pi * frequency * x1 / sampling_rate) for x1 in range(num_samples)]
sine_noise = [np.sin(2 * np.pi * noisy_freq * x1/ sampling_rate) for x1 in range(num_samples)]
sine_wave = np.array(sine_wave)
sine_noise = np.array(sine_noise)
combined_signal = sine_wave + sine_noise

#using fft to convert to frequency domain
data = combined_signal
data = np.array(data)
data_fft = np.fft.fft(data)
frequencies = np.abs(data_fft)

#filtering the frequencies
filtered = []

for index, f in enumerate(frequencies):
    if index >950 and index < 1050:
        filtered.append(f)
    else:
        filtered.append(0)

recovered = np.fft.ifft(filtered)

fig, ax=plt.subplots(3,1, figsize=(10,10))
ax[0].plot(combined_signal[:3000])
ax[0].set_title("Original Audio Signal with Noise")
ax[1].plot(frequencies)
ax[1].set_title("Frequencies found")
ax[1].axis(xmin=0,xmax=1200)
ax[2].plot(filtered)
ax[2].set_title("Frequencies filtered")
ax[2].axis(xmin=0,xmax=1200)
plt.show()