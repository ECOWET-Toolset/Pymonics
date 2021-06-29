import pymonics as pymo
import numpy as np
import matplotlib.pyplot as plt


frequencyComponents=np.array([50, 70, 100, 130, 200, 230, 250])    #Choose the frequency components present in the system; fundamental should be the first one.
amplitudes=np.array([1, 0.2, 0.3, 0.1, 0.05, 0.14, 0.10])
#Instantiate the class with following arguments (samplingRate,signalLength in seconds,numpy array of frequencyComponents,numpy array of amplitudes)
genSingal=pymo.Signal_generator(2400,1.5,frequencyComponents,amplitudes)

#generate sinusoidal signal with default noise of 120db
sinusoidalSig=genSingal.generateSin()

#generate cos signal with noise 100 db
cosSig=genSingal.generateCos(target_snr_db=100)


#plot the signals
fig, ax = plt.subplots(2)
ax[0].plot(sinusoidalSig, label='sin signal')
ax[0].set_title('sin signal')
ax[1].plot(cosSig, label='cos signal')
ax[1].set_title('cos signal')

plt.show()