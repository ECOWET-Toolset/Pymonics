import numpy as np
import math as math

"""
Signal_generator:
Generates Sin/Cos signals with desired frequency components. Instantiates with (samplingRate,signalLength in seconds,frequencyComponents,amplitudes).
"""
class Signal_generator:
    def __init__(self,samplingFrequency,signalLength,frequencyComponents,amplitudes):
      self.samplingFrequency=samplingFrequency
      self.signalLength=signalLength
      self.frequencyComponents=frequencyComponents
      self.amplitudes=amplitudes
    """
    generateSin:
    Generates Sin signal with desired frequency components. returns signal as numpy array
    """
    def generateSin(self,target_snr_db=120):
      ts=1/self.samplingFrequency       # Sampling time. added self. because its related to instantiated object.
      
      Nf=self.frequencyComponents.size  # No. of frequencies present in the test signal
      phfd=np.zeros(Nf)
      phf=(math.pi/180)*phfd
      N=math.ceil(self.signalLength*self.samplingFrequency)
      ti=0
      t=np.zeros(N)
      for i in range(0, N):
        t[i]=ti
        ti=t[i]+ts

      temp=2*math.pi*self.frequencyComponents
      signal=np.zeros(N)
      for i in range(0, N):
        temp2=(temp*t[i])+phf
        signal[i]=(np.sin(temp2)).dot(self.amplitudes.conj().transpose())
      return self.awgn(signal,target_snr_db)

    """
    generateCosy:
    Generates Cos signal with desired frequency components. returns signal as numpy array
    """
    def generateCos(self,target_snr_db=120):
      ts=1/self.samplingFrequency       # Sampling time
      
      Nf=self.frequencyComponents.size  # No. of frequencies present in the test signal
      phfd=np.zeros(Nf)
      phf=(math.pi/180)*phfd
      N=math.ceil(self.signalLength*self.samplingFrequency)
      ti=0
      t=np.zeros(N)
      for i in range(0, N):
        t[i]=ti
        ti=t[i]+ts

      temp=2*math.pi*self.frequencyComponents
      signal=np.zeros(N)
      for i in range(0, N):
        temp2=(temp.dot(t[i]))+phf
        signal[i]=(np.cos(temp2)).dot(self.amplitudes.conj().transpose())
      return self.awgn(signal,target_snr_db)
      
    """
    generateSin:
    Generates Sin signal with desired frequency components and noise. returns signal as numpy array
    """
    #def generateSinWithNoise(self,target_snr_db=120):
    #  return self.awgn(self.generateSin(),target_snr_db)

    """
    generateCos:
    Generates Cos signal with desired frequency components and noise. returns signal as numpy array
    """
    #def generateCosWithNoise(self,target_snr_db=120):
    #  return self.awgn(self.generateCos(),target_snr_db)
      
    """
    awgn:
    Generates gaussian noise. returns numpy array of signal
    """
    def awgn(self,signal,target_snr_db):
      # convert voltage or current signal into power 
      x_watts=signal ** 2
      # Calculate signal power and convert to dB 
      sig_avg_watts = np.mean(x_watts)
      sig_avg_db = 10 * np.log10(sig_avg_watts)
      # Calculate noise according to [2] then convert to watts
      noise_avg_db = sig_avg_db - target_snr_db
      noise_avg_watts = 10 ** (noise_avg_db / 10)
      # Generate an sample of white noise
      mean_noise = 0
      noise_volts = np.random.normal(mean_noise, np.sqrt(noise_avg_watts), len(x_watts))
      # Noise up the original signal
      noised_signal = signal + noise_volts
      return noised_signal
