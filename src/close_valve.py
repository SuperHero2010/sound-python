from pydub.generators import Sine, WhiteNoise
from pydub import AudioSegment

part1 = Sine(1000).to_audio_segment(duration=300).apply_gain(-5)

part2 = Sine(400).to_audio_segment(duration=200).apply_gain(-15)

noise = WhiteNoise().to_audio_segment(duration=500).apply_gain(-25)

final_sound = part1.append(part2, crossfade=50).overlay(noise)

final_sound.export("close_valve.wav", format="wav")
