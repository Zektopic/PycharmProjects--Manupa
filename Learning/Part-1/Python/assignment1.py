import wave
import numpy as np
import struct
import matplotlib.pyplot as plt
frequency = 1000
num_samples = 48000
sampling_rate = 48000.0
amplitude = 16000
file = "test.wav"
sine_wave = []
for x in range(num_samples):
    val = np.sin(2 * np.pi * frequency * x/sampling_rate)
    sine_wave.append(val)
nframes=num_samples
comptype="NONE"
compname="not compressed"
nchannels=1
sampwidth=2
wav_file=wave.open(file, 'w')
wav_file.setparams((nchannels, sampwidth, int(sampling_rate), nframes, comptype,
compname))
for s in sine_wave:
    wav_file.writeframes(struct.pack('h', int(s*amplitude)))