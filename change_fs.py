# change sample rete of audio


import librosa
from scipy.io.wavfile import write
import sys


new_fs = 11025   # you can put sample rate you want
audio_path = sys.argv[1]
new_audio_path = sys.argv[2]

signal, fs = librosa.load(audio_path, sr=new_fs)
write(new_audio_path, fs, signal)
