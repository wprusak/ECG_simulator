import numpy as np
import json

from ecg_base import createEcg 

json_file = open('generation_config.json')

config = json.load(json_file)

print("Config in run_generation.py: ")
print(config)

print(config['time'])

time = int(config['time'])
hr = int(config['hr'])
sr = int(config['sr'])
net_noise = float(config['network_noise'])
noise = float(config['noise'])
breath_freq = float(config['breath_freq'])
breath_amp = float(config['breath_amp'])

time, signal = createEcg(maxTime=time, hearthRate=hr, samplingRate=sr, networkNoise=net_noise, noise = noise, breathFreq=breath_freq, breathAmplitude=breath_amp)

np.save("time.npy", time)
np.save("signal.npy", signal)