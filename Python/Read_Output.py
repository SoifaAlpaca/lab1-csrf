import numpy as np
from const import *
import matplotlib.pyplot as plt  

FileFolder = 'GnuRadio/FileOutput/'
n_points = int(3.2e6*19)

qam16 = True

if qam16:

    out_I    = np.fromfile(FileFolder+'I_16_qam.data',dtype=np.float32)
    print(len(out_I) > n_points)
    out_I = out_I[:n_points]
    print(len(out_I))
    out_Q    = np.fromfile(FileFolder+'Q_16_qam.data',dtype=np.float32)[:n_points]

    data_in  = np.fromfile('Python/bits.data',dtype=np.float32)

    # Quantize, data points 

    norm_out_I = normalize_out(out_I)
    norm_out_Q = normalize_out(out_Q)

    bit_I = quantizer(norm_out_I,bits=2)
    bit_Q = quantizer(norm_out_Q,bits=2)

    #plt.plot(norm_out_I[:10000])
    #plt.plot(norm_out_Q[:10000])
    #plt.plot(norm_out_I[:10000])
    #plt.plot(bit_I[:10000])
    #plt.plot(bit_Q[:10000])

    #plt.show()
    
    bit_I = remove_pilot(extract_data(bit_I,19,'16QAM'))
    bit_Q = remove_pilot(extract_data(bit_Q,19,'16QAM'))

    bitstream = demodulate(bit_I,bit_Q,'16QAM')

    data_len = len(data_in)
    print(data_len < len(bitstream))

    error_num = np.sum(np.abs(data_in - bitstream[:data_len]))
    print(error_num)
    print( 100*error_num/data_len )

qpsk = False#True

if qpsk:

    out_I    = np.fromfile(FileFolder+'I_qpsk.data',dtype=np.float32)
    print(len(out_I) > n_points)
    out_I = out_I[:n_points]
    print(len(out_I))
    out_Q    = np.fromfile(FileFolder+'Q_qpsk.data',dtype=np.float32)[:n_points]

    data_in  = np.fromfile('Python/bits.data',dtype=np.float32)

    # Quantize, data points 

    norm_out_I = normalize_out(out_I)
    norm_out_Q = normalize_out(out_Q)

    bit_I = quantizer(norm_out_I,bits=1)
    bit_Q = quantizer(norm_out_Q,bits=1)

    #plt.plot(norm_out_I)
    #plt.plot(norm_out_Q)
    #plt.plot(norm_out_I[:10000])
    #plt.plot(bit_I)
    #plt.plot(bit_Q)

    #plt.show()

    bit_I = remove_pilot(extract_data(bit_I,19,'QPSK'))
    bit_Q = remove_pilot(extract_data(bit_Q,19,'QPSK'))

    bitstream = demodulate(bit_I,bit_Q,'QPSK')

    data_len = len(data_in)
    print(data_len < len(bitstream))
    error_num = np.sum(np.abs(data_in - bitstream[:data_len]))
    print(error_num)

    print(100*error_num/data_len)