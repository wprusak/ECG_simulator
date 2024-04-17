import numpy as np
import matplotlib.pyplot as plt

from ecg_base import generateBaseEcg 

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

plt.plot(signal)
plt.plot(np.zeros(len(signal)))
plt.legend(["ECG signal", "0 axis"])
plt.savefig("./files/plot.png")

print("Plot saved!")