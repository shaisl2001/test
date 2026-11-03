import numpy as np
import matplotlib.pyplot as plt
import pydicom
from skimage import filters
from scipy.io import loadmat

data=loadmat('S1_A1_E1.mat')
emg=data['emg']
stim=data['stimulus']
print(emg)
emg1=emg[:,0]
emg2=emg[:,1]
emg3=emg[:,2]
emg4=emg[:,3]

maxima1=np.max(emg1)
print(maxima1)
all_maxima=np.diff(emg1)
print(all_maxima)


plt.figure(1)
plt.grid(True)
plt.plot(emg1, lw=0.5)
plt.plot(emg2, lw=0.5)
plt.plot(emg3, lw=0.5)
plt.plot(emg4, lw=0.5)


plt.figure(2)
plt.plot(all_maxima, lw=0.5)
plt.grid(True)
plt.show()