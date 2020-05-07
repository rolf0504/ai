# https://docs.scipy.org/doc/numpy/reference/generated/numpy.fft.fft.html
import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(precision=4, suppress=True)
t = np.arange(0, 10*np.pi, 0.1*np.pi)
ft = np.sin(t)
fi = np.fft.ifft(ft)
print('ft=', ft)
print('fi=', fi)
