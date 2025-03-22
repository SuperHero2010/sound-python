from pydub.generators import Sine, WhiteNoise
from pydub import AudioSegment

part1 = Sine(950).to_audio_segment(duration=350).apply_gain(-6)

part2 = Sine(450).to_audio_segment(duration=250).apply_gain(-12)

noise = WhiteNoise().to_audio_segment(duration=600).apply_gain(-20)

final_sound = part1.append(part2, crossfade=80).overlay(noise)

final_sound.export("ooze_dissolve.wav", format="wav")
