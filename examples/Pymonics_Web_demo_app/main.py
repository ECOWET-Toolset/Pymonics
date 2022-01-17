import os
import pymonics as pymo
from flask import Flask, render_template, request,flash, jsonify, redirect, url_for
from random import choice
import pprint
import numpy as np #added Juan
import pandas as pd

#my_secret = os.environ['okkk']

web_site = Flask(__name__)
#web_site.secret_key =my_secret

harmonicDetectAlogorithm=pymo.Memo_esprit()

#passivefilters=pymo.Passive_filters()

#frequency detection by passing csv file. arguments: sampling frequency used for data collection and location of the csv file
inputSignal=""

@web_site.route('/')
def index():
    placeholder_signal = 'signal sample'
    
    global single
    global high_pass
    
    # declare filter constants
    global h
    global qc
    global q
    global f
    global v

    amplitudes = np.zeros(96)
    frequencies = np.zeros(96)

    # initialize filter constants
    h=16
    qc=2.0
    q=0.8
    f=50.0
    v=11

    # initialize values filters
    single = [2, 15, 100]
    high_pass = [2, 15, 100]

    return render_template('index.html', placeholder_signal=placeholder_signal, amplitudes=amplitudes, frequencies=frequencies, single=single, high_pass=high_pass, h=h, qc=qc, q=q, f=f, v=v)
#@web_site.route('/', methods=['POST','GET'])
#def my_form_post():
#    inputSignal = request.form['signal']
#    sampling_freq=2400
#    #print("hiiii")
#    print(inputSignal)
#    flash("Detected Amplitues and Frequencies:")
#    flash(harmonicDetectAlogorithm.frequency_detection_byString(sampling_freq,inputSignal))
#    #processed_text = inputSignal.upper()
#    return render_template('index.html')

@web_site.route('/', methods=['POST','GET'])
def my_form_post():
    placeholder_signal = 'signal sample'

    inputSignal = []
    sampling_freq = ''

    sample_signal = ''
    sample_frequency = ''

    #initialize signal
    amplitudes = ''
    frequencies = ''
    signal1 = ''
    nComponents = 0
    #filter constants
    global h
    global qc
    global q
    global f
    global v

    # initialize values filters
    single = [2, 15, 100]
    high_pass = [2, 15, 100]

    if request.form['submit'] == 'Analyze':
        try:
            inputSignal = request.form['signal']
        except:
            flash('Verify input signal')
        #sampling_freq=2400    
        try:
            sampling_freq=int(request.form['frequency'])
        except:
            flash('Verify sampling frequency')
        #print("hiiii")
        print(sampling_freq)
        #flash("Detected Amplitues and Frequencies:")
        #flash(harmonicDetectAlogorithm.frequency_detection_byString(sampling_freq,inputSignal))
        try:
            signal = harmonicDetectAlogorithm.frequency_detection_byString(sampling_freq,inputSignal)
            amplitudes = np.round(signal[0], decimals=2)
            frequencies = np.round(signal[1], decimals=2)
            signal1 = zip(amplitudes, frequencies)
            nComponents = len(frequencies)  
        except:
            flash('Verify input data')
            return redirect(url_for('index'))

    if request.form['submit'] == 'Try Sample':
        inputSignalDf = pd.read_csv('Sample.csv', sep=';', header=None)

        sampling_freq = inputSignalDf[0].values
        inputSignal = inputSignalDf[1].values[0]

        signal = harmonicDetectAlogorithm.frequency_detection_byString(sampling_freq,inputSignal)

        placeholder_signal = 'In csv format [2.4,5.6,6.7...]'
        sample_frequency = sampling_freq[0]
        
        amplitudes = np.round(signal[0], decimals=2)
        frequencies = np.round(signal[1], decimals=2)
        signal1 = zip(amplitudes, frequencies)
        nComponents = len(frequencies)

    if request.form['submit'] == 'Calculate':
        try:
            h=float(request.form['h'])
            qc=float(request.form['qc'])
            q=float(request.form['q'])
            f=float(request.form['f'])
            v=float(request.form['v'])
            
        except:
            flash('Verify input data')

        try:
            #filter design:(venky)
            passivefilters=pymo.Passive_filters()
            #single_tuned_filter(h,Qc,Q,f,V)    returns: [C,L,R]

            print(passivefilters.single_tuned_filter(h,qc,q,f,v)) #single tuned filter design
            print(passivefilters.high_pass_filter(h,qc,q,f,v))  #highpass filter design

            single=np.round(passivefilters.single_tuned_filter(h,qc,q,f,v), decimals=6)
            high_pass=np.round(passivefilters.high_pass_filter(h,qc,q,f,v), decimals=6)
            
        except:
            flash('Verify input data')
        
    c_single = 2
    l_single = 15
    r_single = 100

    #filter design:(venky)
    #passivefilters=pymo.Passive_filters()
    #single_tuned_filter(h,Qc,Q,f,V)    returns: [C,L,R]

    #print(passivefilters.single_tuned_filter(7,2.0,0.8,50.0,11)) #single tuned filter design
    #print(passivefilters.high_pass_filter(7,2.0,0.8,50.0,11))  #highpass filter design
	
    return render_template('index.html', amplitudes=amplitudes, frequencies=frequencies, signal1=signal1, nComponents=nComponents, placeholder_signal=placeholder_signal, sample_frequency=sample_frequency, single=single, high_pass=high_pass, h=h, qc=qc, q=q, f=f, v=v)

@web_site.route('/filters', methods=['POST','GET'])
def filters():
    global single
    global high_pass
    global h
    
    try:
        h=float(request.form['h'])
        qc=float(request.form['qc'])
        q=float(request.form['q'])
        f=float(request.form['f'])
        v=float(request.form['v'])
    except:
        flash('Verify input data')

    try:
        #filter design:(venky)
        passivefilters=pymo.Passive_filters()
        #single_tuned_filter(h,Qc,Q,f,V)    returns: [C,L,R]

        print(passivefilters.single_tuned_filter(h,qc,q,f,v)) #single tuned filter design
        print(passivefilters.high_pass_filter(h,qc,q,f,v))  #highpass filter design

        single=passivefilters.single_tuned_filter(h,qc,q,f,v)
        high_pass=passivefilters.high_pass_filter(h,qc,q,f,v)
    except:
        flash('Verify input data')

    #return redirect(request.referrer)
    #return render_template('index.html', h=h)
    return redirect(url_for('index'))


@web_site.route('/user/', defaults={'username': None})
@web_site.route('/user/<username>')
def generate_user(username):
	if not username:
		username = request.args.get('username')

	if not username:
		return 'Sorry error something, malformed request.'

	return render_template('personal_user.html', user=username)


web_site.run(host='0.0.0.0', port=8080)
