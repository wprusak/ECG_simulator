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
    return smooth(signal[150:820],10)

def addFlat(signal,hearthRate,samplingRate):
    tp = np.linspace(0,0.6,len(signal))
    t = np.linspace(0,0.6,round(0.6*samplingRate))
    s = np.interp(t,tp,signal)

    oneBeatPeriod = 1/(hearthRate/60)
    flatPeriod = oneBeatPeriod - 0.6
    if flatPeriod >=0 : 
        zeros = np.zeros(round(flatPeriod*samplingRate))
        signalAppended = np.append(s,zeros)
    else :
        signalAppended = s
    return signalAppended

def calculateTime(signal, samplingRate):
    time = np.linspace(0,len(signal)/samplingRate,len(signal))
    return time

def smooth(y, box_pts):
    box = np.ones(box_pts)/box_pts
    y_smooth = np.convolve(y, box, mode='same')
    return y_smooth

def createMultiplePeriods(periods,hearthRate,samplingRate):
    A = [[-0.313,	-4.680,	1.057,	-0.500,	0.345],
    [0.373	,4.726	,0.690	,0.228	,-0.223]]
    T = [[282.660,	87.180,	30.640,	11.120,	177.252],
        [264.160,	88.000,	15.400,	1.000,	248.027]]
    S = [[	43.672,	19.990,	14.110,	18.060,	92.944],
            [50.571,	20.580,	14.110,	5.676,	46.880]]
    Lengths = [300,88,48,77,429]
    C = [[0.011,-0.04,-0.27,0.017,-0.001],
        [0,0,0,0,0]]
    
    signal = generateBaseEcg(Lengths,A,T,S,C)
    s = addFlat(signal,hearthRate,samplingRate)
    sOut = np.concatenate([s for i in range(periods)])
    tOut = calculateTime(sOut,samplingRate)
    return tOut,sOut
    
