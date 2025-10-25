import numpy as np
from const import *
import matplotlib.pyplot as plt  

FileFolder = 'GnuRadio/FileInput/'
n_points   = int(3e6)
np.random.seed(3141592)

# Parameters
freq_samp = 768e3
Sig_freq  = 20e3
rep       = int(freq_samp/(2*Sig_freq))
print(rep)

#Create random data
data = np.random.randint(0, 2, n_points).astype(np.uint8)

gen_qpsk = True

if gen_qpsk:
    
    I_arr,Q_arr = modulate(data,'QPSK')
    I_arr = upsample(I_arr,rep)
    Q_arr = upsample(Q_arr,rep)
    
    np.array(I_arr,dtype=np.float32).tofile(FileFolder+'I_qpsk.data')
    np.array(Q_arr,dtype=np.float32).tofile(FileFolder+'Q_qpsk.data')

gen_qam16 = True

if gen_qam16:
    
    I_arr,Q_arr = modulate(data,'16QAM')
    I_arr = upsample(I_arr,rep)
    Q_arr = upsample(Q_arr,rep)
    
    #plt.plot(I_arr)
    #plt.plot(Q_arr)
    #plt.show()
    np.array(I_arr,dtype=np.float32).tofile(FileFolder+'I_16_qam.data')
    np.array(Q_arr,dtype=np.float32).tofile(FileFolder+'Q_16_qam.data')


data = np.array(data,dtype=np.float32).tofile('Python/bits.data')