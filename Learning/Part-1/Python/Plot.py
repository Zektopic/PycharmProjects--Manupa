import numpy as np
import matplotlib.pyplot as plt
import math
from math import e

w = np.linspace(0, 2*math.pi,200)#omega
sine_ratio_dtft =  np.sin((5*w)/2)/np.sin(w/2)
dtft = e **(2j*w)*sine_ratio_dtft
plt. figure()
plt.xlabel("<--Amplitude (DTFT)-->")
plt.ylabel("<--Frequency-->")
plt.plot(w,abs(dtft))
plt.grid()
plt.show()
