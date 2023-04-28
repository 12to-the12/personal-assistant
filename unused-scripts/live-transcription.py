# import whisper
# import pyaudio
# import numpy as np

# # Set up the ASR model
# asr = whisper.load_model("base.en")

# # Set up the PyAudio stream
# audio = pyaudio.PyAudio()
# stream = audio.open(format=pyaudio.paInt24, channels=1, rate=16000, input=True, frames_per_buffer=4096)

# # Loop to continuously transcribe streaming audio
# print('start')
# while True:
#     # Read audio data from the stream
#     data = stream.read(4096)
#     audio_data = np.frombuffer(data, dtype=np.int16).astype(np.float32) / 32768.0
#     # Pass the audio data to the ASR model for transcription
#     transcription = asr.transcribe(audio_data)

#     # Print the transcription
#     print(transcription)
