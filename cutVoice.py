from pydub import AudioSegment
import sys


audio_path = sys.argv[1]
new_audio_path = sys.argv[2]
audio_format = "wav"

# set start and end of audio you want
start = 0  # ms
end = 2000  # ms

newAudio = AudioSegment.from_wav(audio_path)
newAudio = newAudio[start:end]
newAudio.export(new_audio_path, format=audio_format)

