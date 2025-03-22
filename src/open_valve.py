import numpy as np
import soundfile as sf
from scipy.signal import chirp
import matplotlib.pyplot as plt

sample_rate = 44100 
duration = 0.8 

t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

part1 = 0.1 * np.sin(2 * np.pi * np.random.uniform(300, 500) * t[:int(0.15 * len(t))])

part2 = 0.6 * chirp(t[int(0.15 * len(t)):int(0.4 * len(t))], f0=500, f1=1500, t1=0.25, method='linear')

part3 = 0.8 * np.sin(2 * np.pi * np.random.uniform(300, 700) * t[int(0.4 * len(t)):int(0.55 * len(t))])
part3 += 0.02 * np.random.normal(size=len(part3))

part4 = 0.1 * np.sin(2 * np.pi * np.random.uniform(100, 300) * t[int(0.55 * len(t)):])

audio_signal = np.concatenate((part1, part2, part3, part4))

audio_signal /= np.max(np.abs(audio_signal))

sf.write("open_valve.wav", audio_signal, sample_rate)

plt.figure(figsize=(10, 4))
plt.plot(t, audio_signal)
plt.title("Waveform - Generated Sound")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.show()
