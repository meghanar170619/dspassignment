import matplotlib.pyplot as plt
import numpy as np

Fs=100
T=1/Fs
N =50;
n=np.arange(0,N);
w=.1*np.pi;
x_n=np.cos(w*n)


X_w=np.fft.fft(x_n/len(x_n))
X_w=X_w[range(int(len(x_n)))]

tp=len(x_n)
val=np.arange(int(tp/2))
tim_per=tp/Fs
fre=val/tim_per

plt.subplot(311)
plt.plot(x_n)
plt.subplot(312)
plt.magnitude_spectrum(x_n)
plt.subplot(313)
plt.phase_spectrum(x_n)
plt.show()
