from pydub.generators import WhiteNoise, Sine
from pydub import AudioSegment

noise = WhiteNoise().to_audio_segment(duration=900).apply_gain(-20)

sine_wave = Sine(200).to_audio_segment(duration=900).apply_gain(-35)

flowing_water = noise.overlay(sine_wave)

flowing_water.export("water_flow.wav", format="wav")
