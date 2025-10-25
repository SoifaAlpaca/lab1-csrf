import numpy as np
import matplotlib.pyplot as plt  
from scipy.special import erfc

Blue    = (       0, 101/255, 189/255 )
Green   = (  52/255, 129/255,  65/255 )
Orange  = ( 241/255,  89/255,  41/255 )

n_arr   = np.array([0.2,0.3,0.4,0.6,0.8,1,1.2,1.8,2])
snr_arr = 20 * np.log10(1/n_arr)
Pe_arr_16qam = np.array([ 0.0016,0.12743333333333334,1.2444,9.461433333333334,17.338866666666668,20.4246,23.5777,26.555733333333333,27.242233333333335 ])/100 # Not norm
#Pe_arr_16qam  = np.array([ 0.0034,0.158033,1.08706,5.37286,15.9121,21.52793,26.033066,28.36003,30.0617667,31.5278668,35.19463336,36.208833 ])/100

Pe_arr_qpsk  = np.array([ 0.0,0.0001,0.0135,0.7241,3.2046,6.836,10.59,19.9,22.265 ])/100


# --- Theoretical BER ---
EbN0_dB = np.linspace(-5, 25, 200)
EbN0_lin = 10**(EbN0_dB / 10)

BER_qpsk_theory = 0.5 * erfc(np.sqrt(EbN0_lin))

BER_16qam_theory = (3/8) * erfc(np.sqrt((0.4 * EbN0_lin)))

# Plot
plt.figure(figsize=(9, 6))

plt.semilogy(snr_arr, Pe_arr_16qam, 'o',color=Blue, label='16QAM')
plt.semilogy(snr_arr[1:], Pe_arr_qpsk[1:], 'x',color=Orange, label='QPSK')


plt.semilogy(EbN0_dB, BER_16qam_theory, '--',color=Blue, label='16QAM Theory')
plt.semilogy(EbN0_dB, BER_qpsk_theory, '--',color=Orange, label='QPSK Theory')

# Formatting
plt.grid(True, which='both', linestyle=':', linewidth=0.7)
plt.xlabel(r'$E_b/N_0$ (dB)', fontsize=12)
plt.ylabel('Bit Error Rate (BER)', fontsize=12)
plt.title(r'BER vs $E_b/N_0$', fontsize=14)
plt.legend(loc='lower left', fontsize=10)
plt.xlim(-7,17)
plt.ylim(1e-7, 1)

plt.show()


# a_3

a_3_arr_16qam = np.array([ 0.0161111,0.0175,0.018,0.02,0.025, 0.03,0.04,0.05 ,0.06])

Pe_arr_16qam  = np.array([0,6.666666666666667e-05,0.0002666666666666667,0.027566666666666666,1.4691,7.955,12.505066666666666,12.505066666666666,12.784133333333333]) / 100

# Plot
plt.figure(figsize=(9, 6))

plt.semilogy(a_3_arr_16qam, Pe_arr_16qam, 'o--',color=Blue, label='16QAM')

plt.axvline(x=0.0161111, color=Orange, linestyle='--', linewidth=1.5, label=r'$1$ dB')
# Formatting
plt.grid(True, which='both', linestyle=':', linewidth=0.7)
plt.xlabel(r'$a_3$', fontsize=12)
plt.ylabel('Bit Error Rate (BER)', fontsize=12)
plt.title(r'BER vs $a_3$', fontsize=14)
plt.legend(loc='lower right', fontsize=10)

plt.show()