from TTS.api import TTS

# Running a multi-speaker and multi-lingual model

# List available 🐸TTS models and choose the first one
models = TTS(cs_api_model="XTTS").list_models()
# Init TTS with the target studio speaker
tts = TTS(model_name="coqui_studio/en/Torcull Diarmuid/coqui_studio", progress_bar=False, gpu=False)
# Run TTS
models = TTS(cs_api_model="V1").list_models()
# Run TTS with emotion and speed control
# Emotion control only works with V1 model
tts.tts_to_file(text="This is a test.", file_path=OUTPUT_PATH, emotion="Happy", speed=1.5)