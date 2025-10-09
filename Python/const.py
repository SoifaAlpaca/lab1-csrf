import numpy as np
from sympy import *

gray_map = [0, 1, 3, 2]


def mod_qpsk(data):

    I_arr = []
    Q_arr = []

    for i in range(0, len(data),2):
        
        b1 = int(data[i])
        b2 = int(data[i+1])

        k = gray_map[2*b2 +b1]

        s = exp( np.pi*0.5*I*(k+0.5) )

        I_arr.append(re(s))
        Q_arr.append(im(s))

    return I_arr,Q_arr

def mod_qam_16(data):

    I_arr = []
    Q_arr = []
    
    norm = abs( 3 + 3*I )
    for i in range(0,len(data),4):
        
        b1 = int(data[i])
        b2 = int(data[i+1])
        b3 = int(data[i+2])
        b4 = int(data[i+3])

        q_s  = gray_map[b1 + 2*b2]*2-3
        i_s  = gray_map[b3 + 2*b4]*2-3

        s = i_s + q_s*I
        s = s/norm

        I_arr.append(re(s))
        Q_arr.append(im(s))

    return I_arr,Q_arr


def upsample(symbols,n_rep):

    symb = np.zeros(len(symbols)*n_rep)
    pos = 0
    for s in symbols:
        for _ in range(n_rep):
            symb[pos] = s
            pos += 1

    return symb