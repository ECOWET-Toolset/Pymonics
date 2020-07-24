# -*- coding: utf-8 -*-
# Developer: Venkatesh Pampana
# Contributor: Ankit Srivastava

"""**This is main function.** 
function name: memo-esprit
---

# List of variables used in this program:
*Inputs:*

**inputSignal**= electric signal voltage/current values

**autocorrelationMatrixSize**=size of autocorelation matrix (optional) default value is 100

**fs**= Sampling Frequency

*outputs:*

**frequencies**= detected frequencies

**amplitudes**= corresponding frequencies

# Other intermediate variable
**inputDataSamples**=array containing inputsignal


**hankelMatrix**=hankel matrix

**e_lambda**= eigen values

**e_Vector**=eigen vector
"""

import pandas as pd
import numpy as np
import scipy.linalg as LA
from scipy.linalg import hankel
import math as math
import cmath


class Memo_esprit:
    def frequency_detection_byCSV(self,samplingFrequency, filepath, fileheader=None, autocorrelationMatrixSize=100):
        # reading uploaded input csv file
        inputSignal = pd.read_csv(filepath, header=fileheader)
        # array containing inputsignal)
        inputDataSamples = inputSignal.iloc[0, :]
        #print(inputDataSamples.shape)
        inputDataSamples = np.transpose(inputDataSamples)
        #print(inputDataSamples.shape)		
        return self.detectionAlgorithm(samplingFrequency, inputDataSamples, autocorrelationMatrixSize)

        # frequency detection by passing signal string

    def frequency_detection_byString(self,samplingFrequency, inputSignalString, autocorrelationMatrixSize=100):
        inputDataSamples = np.transpose(inputSignalString.split(','))
        return self.detectionAlgorithm(samplingFrequency, inputDataSamples, autocorrelationMatrixSize)

    def frequency_detection_byNParray(self,samplingFrequency, inputDataSamples, autocorrelationMatrixSize=100):
        return self.detectionAlgorithm(samplingFrequency, inputDataSamples, autocorrelationMatrixSize)

    def detectionAlgorithm(self,samplingFrequency, inputDataSamples, autocorrelationMatrixSize):
        # Creating the hankel matrix
        #hankelMatrix=hankel(inputDataSamples[1:inputDataSamples.size-autocorrelationMatrixSize+1], inputDataSamples[0:autocorrelationMatrixSize])
        hankelMatrix = np.zeros(
            (inputDataSamples.size-autocorrelationMatrixSize, autocorrelationMatrixSize))
        for i in range(0, inputDataSamples.size-autocorrelationMatrixSize):
            for j in range(0, autocorrelationMatrixSize):
                hankelMatrix[i, j] = inputDataSamples[i+j+1]
                j = j+1
            i = i+1
        # print("hankelMatrix")
        # print(hankelMatrix)

        # create autocoorelation matrix
        # hankelDataFrame=pd.DataFrame(hankelMatrix)
        # Rx=hankelDataFrame.corr()
        Rx = (1/(inputDataSamples.size-autocorrelationMatrixSize)) * \
            ((hankelMatrix.conj().transpose()).dot(hankelMatrix))
        # print("Rx")
        # print(Rx)

        # eigenvalue decomposistion
        # e_lambda= eigen values , e_Vector=eigen vector
        e_lambda, e_Vector = LA.eig(Rx)
        #print("Eigen Values")
        # print(e_lambda)

        # eigen value sorting in decending order and their respective eigen vectors with preserved indeces
        idx = e_lambda.argsort()[::-1]  # sort eigen values in decending order
        # print("idx")
        # print(idx)
        s_lambda = (e_lambda[idx])  # sorted eigen values
        sorted_E_Vector = e_Vector[:, idx]  # sorted eigen vector

        # Implementing equation
        RD = np.zeros(math.ceil(autocorrelationMatrixSize/2) -
                      1, dtype=np.complex)
        RDI = np.zeros(math.ceil(autocorrelationMatrixSize/2)-1)
        # print("Rd")
        # print(RD)
        # Remember!! range() function in python doesn't return end value so -1 instead of-2
        for i in range(0, math.ceil(autocorrelationMatrixSize/2)-1):
            a1 = (s_lambda[2*i]+s_lambda[2*i+1])/2
            a2 = (s_lambda[2*i+2]+s_lambda[2*i+3])/2
            a = (a1-a2)/a1
            RDI[i] = i
            RD[i] = a

        # sorting RD in descending order.
        # sorted_RD=np.sort(RD)[::-1]

        # finding out then largest RD and corresponding RDI
        maxRDI = np.argmax(np.abs(RD), axis=0)
        maxRD = np.amax(np.abs(RD))
        # print("maxRDI")
        # print(maxRDI)
        # print("maxRD")
        # print(maxRD)
        # ploting RD vs RDI
        #plt.plot(np.abs(RD), label='RD')
        # plt.show()

        # esprit
        order = maxRDI+1
        # print("order")
        # print(order)
        Esig = np.zeros((autocorrelationMatrixSize, 2*order), dtype=np.complex)

        for i in range(0, autocorrelationMatrixSize):
            for j in range(0, 2*order):
                Esig[i, j] = sorted_E_Vector[i, j]
                j = j+1
            i = i+1
        # print("Esig")
        # print(Esig.shape)

        # creating identity matrix of order M-ds
        ds = 1
        iM = np.eye(autocorrelationMatrixSize-ds)
        # print(iM)

        # creating the distance matrix.
        ds = 1
        ods = np.zeros((1, autocorrelationMatrixSize-ds))
        # print(ods)

        # transposing the distance matrix
        od = np.transpose(ods)
        # print(od.shape)
        # transposing the distance matrix
        s1 = np.concatenate((iM, od), 1)
        s2 = np.concatenate((od, iM), 1)

        R1 = s1.dot(Esig)
        R2 = s2.dot(Esig)

        Psi1 = (R1.conj().transpose()).dot(R1)
        # print("Psi1")
        # print(Psi1)
        Psi1_inv = LA.inv(Psi1)
        Psi2 = (R1.conj().transpose()).dot(R2)
        Psi = Psi1_inv.dot(Psi2)
        # print("Psi")
        # print(Psi)

        Z, vec = LA.eig(Psi)
        # print("Z")
        # print(Z)
        temp = complex(1, 1)
        temp_frequencies1 = np.zeros((2*order, 1))
        for f in range(0, 2*order):
            temp = (cmath.log(Z[f]))
            temp_frequencies1[f] = (temp.imag)/(2 * math.pi)
            f = f+1

        temp_frequencies = samplingFrequency*temp_frequencies1
        # sort in decendng order
        sorted_frequencies = -np.sort(-temp_frequencies, axis=0)
        frequencies = np.zeros((int(sorted_frequencies.size/2), 1))
        for i in range(0, frequencies.size):
            frequencies[i] = sorted_frequencies[i]
        frequencies_rounded = np.around(frequencies)

        #print("frequencies")
        #print(frequencies)
        #print("Rounded frequencies")
        #print(frequencies_rounded)

        # sort frequencies without samplingFrequency in decendng order
        frequencies_without_fs = -np.sort(-temp_frequencies1, axis=0)

        Rs1 = Rx[:, autocorrelationMatrixSize -
                 2*order:autocorrelationMatrixSize]
        # print(Rs1)

        V = np.zeros((autocorrelationMatrixSize, 2*order), dtype=np.complex)
        # print(frequencies_without_fs.shape)

        for k in range(0, autocorrelationMatrixSize):
            tempx = np.exp(((2*math.pi*(k))*frequencies_without_fs)*1j)
            # print(tempx)
            # convert tempx column vector to row vector by reshapeing and copy the resultant as a K'th row
            V[[k], :] = tempx.reshape(1, -1)

        VH = (V.conj().transpose()).conj()
        Amplitude = (LA.inv(VH.dot(V))).dot(VH).dot(Rs1)
        namp = (2*np.sqrt(Amplitude[:, 0])).conj().transpose()
        namp1 = np.abs(namp)
        amplitudes = np.zeros((int(namp1.size/2), 1))
        for i in range(0, amplitudes.size):
            amplitudes[i] = namp1[i]
        # frequencies_rounded=np.around(frequencies)
        # print("Amplitude")
        # print(namp)
        # print(amplitudes)
        return amplitudes, frequencies
