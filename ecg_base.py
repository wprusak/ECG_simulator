import numpy as np 

def waveGenerator(timeData,amplitude,timeConstant,std,C):
    return amplitude*np.exp(-((timeData-timeConstant)**2/(std**2))) + C 

def generateBaseEcg(wavesLengths,Amplitudes,Times,Stds,C):
    signal = np.array([])
    Amplitudes = np.array(Amplitudes)
    Times = np.array(Times)
    Stds = np.array(Stds)
    C = np.array(C)
    for waveNr in range(5) :
        t = np.linspace(0,wavesLengths[waveNr],wavesLengths[waveNr])
        wave = np.zeros(wavesLengths[waveNr])
        wave += waveGenerator(t,Amplitudes[0,waveNr],Times[0,waveNr],Stds[0,waveNr],C[0,waveNr])
        wave += waveGenerator(t,Amplitudes[1,waveNr],Times[1,waveNr],Stds[1,waveNr],C[1,waveNr])
        signal = np.append(signal,wave)
    return signal