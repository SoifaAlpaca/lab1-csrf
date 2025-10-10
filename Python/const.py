import numpy as np
from sympy import *
from numba import njit, prange

gray_map     = [0, 1, 3, 2]
inv_gray_map = {0:0, 1:1, 3:2, 2:3}
pilot_cycle  = 12
qpsk_pilot   = np.array([ int(i % 2)/sqrt(2) for i in range(pilot_cycle) ])

qam16_norm   = float(sqrt(10))#abs( 3 + 3*I )
qam16_levels = np.array([-3, -1, 1, 3], dtype=float)/qam16_norm
qam16_pilot  = np.array([ qam16_levels[int(i % 2)*3] for i in range(pilot_cycle) ])

def modulate(data,mode):

    if mode == '16QAM':
        return mod_qam_16(data)
    
    if mode == 'QPSK':
        return mod_qpsk(data)

def add_pilot(data,mode):

    if mode == '16QAM':
        return np.concatenate((qam16_pilot,data))
    
    if mode == 'QPSK':
        return np.concatenate((qpsk_pilot,data))

def mod_qpsk(data,pilot=True):

    I_arr = []
    Q_arr = []
    
    for i in range(0, len(data),2):
        
        b1 = int(data[i])
        b2 = int(data[i+1])

        k = gray_map[2*b2 +b1]

        s = exp( np.pi*0.5*I*(k+0.5) )

        I_arr.append(re(s))
        Q_arr.append(im(s))

    if pilot:
        I_arr = add_pilot(I_arr,'QPSK')
        Q_arr = add_pilot(Q_arr,'QPSK')
    
    return I_arr,Q_arr

def mod_qam_16(data,pilot=True):

    assert len(data) % 4 == 0

    I_arr = []
    Q_arr = []
    

    for i in range(0,len(data),4):
        
        b1, b2, b3, b4 = map(int, data[i:i+4])   # b1,b2 -> Q ; b3,b4 -> I (your convention)

        q_s  = qam16_levels[
                gray_map[b1*2 + b2]
            ]
        i_s  = qam16_levels[
                gray_map[b3*2 + b4]
        ]

        I_arr.append(i_s)
        Q_arr.append(q_s)
    
    if pilot:
        I_arr = add_pilot(I_arr,'16QAM')
        Q_arr = add_pilot(Q_arr,'16QAM')

    return I_arr,Q_arr

def demodulate(I_arr,Q_arr,mode):

    if mode == '16QAM':
        return demod_qam_16(I_arr,Q_arr)
    
    #if mode == 'QPSK':
    #    return demod_qpsk(I_arr,Q_arr)


def demod_qam_16(I_arr,Q_arr):

    bitstream = []

    for I_idx, Q_idx in zip(I_arr, Q_arr):
        
        i_bin = inv_gray_map[int(I_idx)]
        q_bin = inv_gray_map[int(Q_idx)]
        
        b1 = (q_bin >> 1) & 1
        b2 = q_bin & 1
        b3 = (i_bin >> 1) & 1
        b4 = i_bin & 1
        
        bitstream += [b1, b2, b3, b4]
    
    return np.array(bitstream, dtype=int)


#signal already quantized
#f_ratio = f_gnu/f_bitstream
#ideally this would calculate f_ratio 

def extract_data(sig,f_ratio):

    data    = []
    pos_arr = []

    #find tone
    pos = 0
    for s in sig:
        if s <= 0:
            break 
        pos += 1
    
    # find 'duty cycle'
    pos_end = pos
    while( sig[pos_end] == 0 ):
        pos_end += 1
    
    i = int((pos_end + pos)/2)   # middle of peak
    #print((pos_end - pos)/2)
    while(i < len(sig)):

        data.append(sig[i])
        pos_arr.append(i)
        i += f_ratio
    
    return data#,pos_arr

def remove_pilot(data):

    return data[pilot_cycle:]

#def demod_qpsk(I_arr,Q_arr):
@njit(parallel=True)
def quantizer_2bit(data,norm=qam16_norm):

    arr_unscaled = data * norm
    n = arr_unscaled.size
    idxs = np.empty(n, dtype=np.int32)
    for i in prange(n):
        
        idx = int(round((arr_unscaled[i] + 3) / 2))
        idxs[i] = min(max(idx, 0), 3)

    return idxs
    data = np.asarray(data)
    arr_unscaled = data * norm
    
    # Vectorized computation of nearest level
    # Compute distance to each QAM16 level and pick argmin along axis=1
    idxs = np.argmin(np.abs(arr_unscaled[..., None] - qam16_levels), axis=-1)
    
    return idxs.astype(int)

def upsample(symbols,n_rep):

    symb = np.zeros(len(symbols)*n_rep)
    pos = 0
    for s in symbols:
        for _ in range(n_rep):
            symb[pos] = s
            pos += 1

    return symb