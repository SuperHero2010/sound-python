from pydub.generators import Sine
from pydub import AudioSegment

clunk_freq = 1500  
clunk = Sine(clunk_freq).to_audio_segment(duration=120).apply_gain(-10)

clunk.export("close_valve.wav", format="wav")
print("✅ Valve closing sound created: close_valve.wav")