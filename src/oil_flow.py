from pydub.generators import Sine
from pydub import AudioSegment

oil_flow = Sine(100).to_audio_segment(duration=1500).apply_gain(-20)  # Tần số thấp, 1.5s
oil_modulation = Sine(50).to_audio_segment(duration=1500).apply_gain(-25)  # Sóng thấp hơn để tạo cảm giác đặc

oil_sound = oil_flow.overlay(oil_modulation).fade_in(200).fade_out(300)

oil_sound.export("oil_flow.wav", format="wav")
print("✅ Oil flowing sound created: oil_flow.wav")