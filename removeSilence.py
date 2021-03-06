from pydub import AudioSegment
from scipy.io.wavfile import write
import numpy as np
import sys


audio_path = sys.argv[1]
new_audio_path = sys.argv[2]
audio_format = "wav"


def detect_leading_silence(sound, silence_threshold=-50.0, chunk_size=10):
    trim_ms = 0  # ms

    assert chunk_size > 0  # to avoid infinite loop
    while sound[
        trim_ms : trim_ms + chunk_size
    ].dBFS < silence_threshold and trim_ms < len(sound):
        trim_ms += chunk_size

    return trim_ms


sound = AudioSegment.from_file(audio_path, format=audio_format)

start_trim = detect_leading_silence(sound)
end_trim = detect_leading_silence(sound.reverse())

duration = len(sound)
trimmed_sound = sound[start_trim : duration - end_trim]

trimmed_sound.export(new_audio_path, format=audio_format)

