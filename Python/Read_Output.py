import numpy as np
from const import *
import matplotlib.pyplot as plt  

FileFolder = 'GnuRadio/FileOutput/'

n_points = int(1.2e4*19)
out_I    = np.fromfile(FileFolder+'I_16_qam.data',dtype=np.float32)[:n_points]
out_Q    = np.fromfile(FileFolder+'Q_16_qam.data',dtype=np.float32)[:n_points]

plt.plot(out_I)
plt.plot(out_Q)
plt.show()

data_in  = np.fromfile('Python/bits.data',dtype=np.float32)

def adc_2bit(data):

    data_out  = []
    threshold = (1/np.sqrt(2))*3/4

    for val in data:


        if val > 0.1:
            b1 = 1
            if abs(val) > threshold:
                b2 = 1
            else: 
                b2 = 0
        else:
            b1 = 0
            if abs(val) > threshold:
                b2 = 0
            else: 
                b2 = 1



        data_out.append(b1*2+b2)
    return data_out 

def remove_zero(data):

    i = 0
    for b in data:
        if b == 0:
            i += 1
        else:
            return data[i:]
    
    return data

bit_I = adc_2bit(out_I)
bit_Q = adc_2bit(out_Q)
     
data_in = remove_zero(data_in)

plt.plot(bit_Q)
plt.plot(3/np.sqrt(2)*(out_Q+(1/np.sqrt(2))),color='green', label='bit_Q')
plt.show()

# Create two subplots (2 rows, 1 column)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))

# First subplot: bit_I and bit_Q
ax1.plot(bit_I, color='red', label='bit_I')
ax1.plot(3/np.sqrt(2)*(out_Q+(1/np.sqrt(2))), color='green', label='bit_Q')
#ax1.plot(bit_Q, color='green', label='bit_Q')
ax1.legend()
ax1.set_title('bit_I and bit_Q')
# ax1.set_xlim(0, 500)  # optional

# Second subplot: data_in
ax2.plot(data_in, color='blue', label='data_in')
ax2.legend()
ax2.set_title('data_in')
# ax2.set_xlim(0, 500)  # optional

plt.tight_layout()
plt.show()
