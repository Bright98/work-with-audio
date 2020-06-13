import sounddevice as sd
from scipy.io.wavfile import write
import sys


fs = 11025  # write sample rate you want
duration = 3  # second
file_name = sys.argv[1]

signal = sd.rec(int(duration * fs), samplerate=fs, channels=2)
print("recording...")
sd.wait()

write(file_name, fs, signal)
print("recorded !")
