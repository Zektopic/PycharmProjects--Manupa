import wave
import numpy as np
import struct
import matplotlib.pyplot as plt
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
plt.subplot(3,1,1)
plt.title("Original sine wave")
plt.subplots_adjust(hspace=.5)
plt.plot(sine_wave[:500])
plt.subplot(3,1,2)
plt.title("Noisy wave")
plt.plot(sine_noise[:4000])
plt.subplot(3,1,3)
plt.title("Original Audio Signal with Noise")
plt.plot(combined_signal[:3000])
plt.show()