import matplotlib.pyplot as plt  
from const import *

Blue    = (       0, 101/255, 189/255 )
Green   = (  52/255, 129/255,  65/255 )
Orange  = ( 241/255,  89/255,  41/255 )


plot_qpsk = True

if plot_qpsk:

    data = []
    n_bits = 2
    for i in [ bin(k+2**n_bits)[3:] for k in range(0,2**n_bits) ]:
        for j in i:
            data.append(j)

    I_arr,Q_arr = qpsk(data)
    plt.scatter(I_arr,Q_arr,color=Blue)

    for i in range(len(I_arr)):
        plt.text(I_arr[i]+0.1,Q_arr[i],str(bin(i+4)[3:]),color=Orange, fontsize=12)

    plt.xlim(-1, 1) # Set x-axis
    plt.ylim(-1, 1) # Set y-axis  
    plt.title('QPSK Constellation')
    plt.xlabel('I')
    plt.ylabel('Q')
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.grid()
    plt.show()

plot_16qam = True

if plot_16qam:

    data = []
    n_bits = 4
    for i in [ bin(k+2**n_bits)[3:] for k in range(0,2**n_bits) ]:
        for j in i:
            data.append(j)


    I_arr,Q_arr = qam_16(data)
    plt.scatter(I_arr,Q_arr,color=Blue)

    for i in range(len(I_arr)):

        label = str(bin(i+2**n_bits)[3:])
        plt.text(I_arr[i]+0.1,Q_arr[i],label,color=Orange, fontsize=12)

    plt.xlim(-1, 1) # Set x-axis
    plt.ylim(-1, 1) # Set y-axis  
    plt.title('16-QAM Constellation')
    plt.xlabel('I')
    plt.ylabel('Q')
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.grid()
    plt.show()