from app import transcribe_audio, get_gpt3_response, text_to_speech

url = "https://gepetovoicedemo.blob.core.windows.net/voicemp3/output20231219033922970.mp3"
test = transcribe_audio(url)
print(test)

