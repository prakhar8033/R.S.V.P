import openai

def TranscriptGenerator(text):
    openai.api_key = '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'
    # calling chatgpt openai
    response = openai.Completion.create(

    engine="text-davinci-003",
    # prompt to convert the text into a conversation between sales person and user.
    prompt=f""" {text}

    This is a conversation between a Sales person working at Crio talking to a user. Divide and provide the transcript of hte conversation. 

    Make the output of the transcription this way -  

    Sales person: 
    User:
    Sales person:
    User:

    in this way. """,
    max_tokens=100,
        temperature=0.6
    )

    transcript = response.choices[0].text.strip()
    return transcript