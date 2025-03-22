from pydub.generators import Sine, WhiteNoise, Sawtooth
from pydub import AudioSegment

part1 = Sawtooth(850).to_audio_segment(duration=350).apply_gain(-6)

part2 = Sine(420).to_audio_segment(duration=270).apply_gain(-10)

noise = WhiteNoise().to_audio_segment(duration=500).apply_gain(-22)

final_sound = part1.append(part2, crossfade=40).overlay(noise)

final_sound.export("open_valve.wav", format="wav")
