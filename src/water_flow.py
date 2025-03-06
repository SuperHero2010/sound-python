from pydub.generators import Sine
from pydub import AudioSegment

water_flow = Sine(300).to_audio_segment(duration=1000).apply_gain(-25).fade_in(200).fade_out(200)

water_flow.export("water_flow.wav", format="wav")
print("✅ Water sound created: water_flow.wav")