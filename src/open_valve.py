from pydub.generators import Sine
from pydub import AudioSegment

click_freq = 4000 
click = Sine(click_freq).to_audio_segment(duration=100).apply_gain(-10)

click.export("open_valve.wav", format="wav")
print("✅ Valve opening sound created: open_valve.wav")