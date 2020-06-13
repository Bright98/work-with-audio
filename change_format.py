from pydub import AudioSegment
import sys


audio_path = sys.argv[1]
new_audio_path = sys.argv[2]
audio_format = "m4a"
new_audio_format = "wav"

voice = AudioSegment.from_file(audio_path, format=audio_format)
voice.export(new_audio_path, new_audio_format)

