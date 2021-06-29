#**following example code will read single csv file and prints the detected frequencies and amplitudes on the screen**
#Step-1: import pymonics package
import pymonics as pymo 
#Step-2: class object 
passivefilters=pymo.Passive_filters()
#Step-3: Filter Designing
print(passivefilters.single_tuned_filter(7,2.0,0.8,50.0,11)) #single tuned filter design
print(passivefilters.high_pass_filter(7,2.0,0.8,50.0,11))  #highpass filter design