# stt_module.py
from vosk import Model, KaldiRecognizer
import wave
import json
# Read the Audio and Recognize Speech in Chunks
def transcribe_audio(file_path, model_path="models/vosk-model-small-en-us-0.15"):
    wf = wave.open(file_path, "rb")
    model = Model(model_path)
    rec = KaldiRecognizer(model, wf.getframerate())
    results = []
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            results.append(json.loads(rec.Result()))
    results.append(json.loads(rec.FinalResult()))
    transcript = " ".join([res.get('text', '') for res in results])
    return transcript.lower()
