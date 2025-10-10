import numpy as np
from const import *
import matplotlib.pyplot as plt  

FileFolder = 'GnuRadio/FileOutput/'

n_points = int(1.2e4*19)
out_I    = np.fromfile(FileFolder+'I_16_qam.data',dtype=np.float32)[:n_points]
out_Q    = np.fromfile(FileFolder+'Q_16_qam.data',dtype=np.float32)[:n_points]
in_I     = np.fromfile(FileFolder+'I_symb_in.data',dtype=np.float32)[:n_points]
in_Q     = np.fromfile(FileFolder+'Q_symb_in.data',dtype=np.float32)[:n_points]

data_in  = np.fromfile('Python/bits.data',dtype=np.float32)

# Quantize, data points 
bit_I = quantizer_2bit(out_I)
bit_Q = quantizer_2bit(out_Q)

bit_I = remove_pilot(extract_data(bit_I,19))
bit_Q = remove_pilot(extract_data(bit_Q,19))

bitstream = demod_qam_16(bit_I,bit_Q)

print( sum(data_in - bitstream[:10000]) )