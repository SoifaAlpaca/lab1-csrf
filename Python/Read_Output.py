import numpy as np
from const import *
import matplotlib.pyplot as plt  

FileFolder = 'GnuRadio/FileOutput/'

qam16 = True

if qam16:

    n_points = int(1.2e4*19)
    out_I    = np.fromfile(FileFolder+'I_16_qam.data',dtype=np.float32)[:n_points]
    print(len(out_I))
    out_Q    = np.fromfile(FileFolder+'Q_16_qam.data',dtype=np.float32)[:n_points]

    data_in  = np.fromfile('Python/bits.data',dtype=np.float32)

    # Quantize, data points 

    norm_out_I = normalize_out(out_I)
    norm_out_Q = normalize_out(out_Q)

    bit_I = quantizer(norm_out_I,bits=2)
    bit_Q = quantizer(norm_out_Q,bits=2)

    plt.plot(norm_out_I)
    #plt.plot(norm_out_I[:10000])
    plt.plot(bit_I)

    plt.show()

    bit_I = remove_pilot(extract_data(bit_I,19))
    bit_Q = remove_pilot(extract_data(bit_Q,19))

    bitstream = demodulate(bit_I,bit_Q,'16QAM')

    data_len = len(data_in)

    error_num = sum(abs(data_in - bitstream[:data_len]))

    print( 100*error_num/data_len )

qpsk = True

if qpsk:

    n_points = int(1.2e4*19)
    out_I    = np.fromfile(FileFolder+'I_qpsk.data',dtype=np.float32)[:n_points]
    print(len(out_I))
    out_Q    = np.fromfile(FileFolder+'Q_qpsk.data',dtype=np.float32)[:n_points]

    data_in  = np.fromfile('Python/bits.data',dtype=np.float32)

    # Quantize, data points 

    norm_out_I = normalize_out(out_I)
    norm_out_Q = normalize_out(out_Q)

    bit_I = quantizer(norm_out_I,bits=1)
    bit_Q = quantizer(norm_out_Q,bits=1)

    plt.plot(norm_out_I)
    #plt.plot(norm_out_I[:10000])
    plt.plot(bit_I)

    plt.show()

    bit_I = remove_pilot(extract_data(bit_I,19))
    bit_Q = remove_pilot(extract_data(bit_Q,19))

    bitstream = demodulate(bit_I,bit_Q,'QPSK')

    data_len = len(data_in)

    error_num = sum(abs(data_in - bitstream[:data_len]))
    print(100*error_num/data_len)