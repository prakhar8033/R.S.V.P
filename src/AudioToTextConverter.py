import openai


def textConverter(file_path):
    openai.api_key = '----your--openai--api--key----'

    # calling openai api to convert the audio into text
    audio_file= open(file_path, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    resText = transcript.text.strip()
    return resText

