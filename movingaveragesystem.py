import scipy.io
from matplotlib import pyplot as plt
from scipy.io import wavfile
import numpy as np
#y=10*np.random.rand(10)
y=[1,2,1,2,3,4]
z=np.zeros(len(y))
M=int(input('enter order'))
for n in range(0,len(y)):
	S=0.0
	q=[]
	for k in range(0,M):
		if n-k>=0:
			q.append(y[n-k])
			S=S+y[n-k]
	z[n]=S/M
print(y)
print(z)
plt.subplot(211)
plt.stem(y)
plt.subplot(212)
plt.stem(z)
plt.show()

