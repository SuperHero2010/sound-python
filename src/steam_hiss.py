from pydub.generators import Sine, WhiteNoise
from pydub import AudioSegment

part1 = Sine(1500).to_audio_segment(duration=500).apply_gain(-10).fade_in(100)

part2_sine = Sine(300).to_audio_segment(duration=1500).apply_gain(-15)
part2_noise = WhiteNoise().to_audio_segment(duration=1500).apply_gain(-25)
part2 = part2_sine.overlay(part2_noise)

part3 = Sine(500).to_audio_segment(duration=500).apply_gain(-20).fade_out(100)

final_sound = part1.append(part2, crossfade=100).append(part3, crossfade=100)

final_sound.export("steam_hiss.wav", format="wav")
