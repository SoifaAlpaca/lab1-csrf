import numpy as np
from const import qpsk,qam_16,downsample

FileFolder = 'GnuRadio/FileInput/'
n_points   = int(1e4)
np.random.seed(3141592)

# Parameters
freq_samp = 768e3
Sig_freq  = 20e3
rep       = int(freq_samp/(2*Sig_freq))
print(rep)


data = np.random.randint(0, 2, n_points).astype(np.uint8)

ring = np.array([ i % 2 for i in range(12) ])

data = np.concatenate((ring,data))

gen_qpsk = True

if gen_qpsk:
    
    I_arr,Q_arr = qpsk(data)
    I_arr = downsample(I_arr,rep)
    Q_arr = downsample(Q_arr,rep)
    
    np.array(I_arr,dtype=np.float32).tofile(FileFolder+'I_qpsk.data')
    np.array(Q_arr,dtype=np.float32).tofile(FileFolder+'Q_qpsk.data')

ge_qam16 = True

if ge_qam16:
    
    I_arr,Q_arr = qam_16(data)
    I_arr = downsample(I_arr,rep)
    Q_arr = downsample(Q_arr,rep)
    
    np.array(I_arr,dtype=np.float32).tofile(FileFolder+'I_16_qam.data')
    np.array(Q_arr,dtype=np.float32).tofile(FileFolder+'Q_16_qam.data')

data = np.array(downsample(data,rep),dtype=np.float32).tofile('Python/bits.data')