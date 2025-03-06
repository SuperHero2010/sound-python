from pydub.generators import WhiteNoise, Sine
from pydub import AudioSegment

hiss = WhiteNoise().to_audio_segment(duration=1200).apply_gain(-20)  # 1.2 giây tiếng xèo

bubble1 = Sine(600).to_audio_segment(duration=100).apply_gain(-15)
bubble2 = Sine(500).to_audio_segment(duration=120).apply_gain(-18)
bubble3 = Sine(450).to_audio_segment(duration=140).apply_gain(-20)

bubbles = bubble1 + AudioSegment.silent(50) + bubble2 + AudioSegment.silent(80) + bubble3

ooze_dissolve = hiss.overlay(bubbles)

ooze_dissolve.export("ooze_dissolve.wav", format="wav")
print("✅ Done creating water eroding ooze sound: ooze_dissolve.wav")
