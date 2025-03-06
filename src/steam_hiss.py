from pydub.generators import WhiteNoise
from pydub import AudioSegment

hiss = WhiteNoise().to_audio_segment(duration=1000).apply_gain(-15)  # 1 giây tiếng xì

hiss_effect = hiss.fade_in(100).fade_out(200)

hiss_effect.export("steam_hiss.wav", format="wav")
print("✅ Done creating the hissing steam sound: steam_hiss.wav")