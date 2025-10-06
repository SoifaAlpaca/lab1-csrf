import numpy as np
from const import qpsk,qam_16

n_points = int(1e4)

np.random.seed(3141592)

data = np.random.randint(0, 2, n_points).astype(np.uint8)

gen_qpsk = True

if gen_qpsk:
    
    I_arr,Q_arr = qpsk(data)
    np.array(I_arr,dtype=np.float32).tofile('I_qpsk.data')
    np.array(Q_arr,dtype=np.float32).tofile('Q_qpsk.data')

ge_qam16 = True

if ge_qam16:
    
    I_arr,Q_arr = qam_16(data)
    np.array(I_arr,dtype=np.float32).tofile('I_16_qam.data')
    np.array(Q_arr,dtype=np.float32).tofile('Q_16_qam.data')
