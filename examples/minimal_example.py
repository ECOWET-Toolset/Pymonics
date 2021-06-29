#**following example code will read single csv file and prints the detected frequencies and amplitudes on the screen**
#Step-1: import pymonics package
import pymonics as pymo 
#Step-2: harmonic detection algorithm class object 
harmonicDetectAlogorithm=pymo.Memo_esprit() 
#Step-3: call frequency detection function
detected_freq_amp=harmonicDetectAlogorithm.frequency_detection_byCSV(2400,'inputSignalFile.csv')  #arguments: sampling frequency used of data collection and location of the csv file
#Step-4: print detected frequencies and amplitudes
print("Detected Amplitudes and Frequencies:", detected_freq_amp) 