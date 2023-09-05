# R.S.V.P.
using ChatGPT to rate a Sales call

# About the Project

> ***A backend script for Scoring and Analyzing the sales script recordings.
> Using OpenAI API for the transcription and generation of an AI model to rate the recordings.
> Creating and writing into excel file the ratings of the corresponding calls.***

# Features

+ ***Extracting the text from audio*** files in one of these formats: flac, mp3, mp4, mpeg, mpga, m4a, ogg, wav, or webm.
+ ***Transcribing the extracted text*** in form of a conversation between a Sales person and a user.
+ ***Analyzing the sales transcript and rating it*** based on certain parameters.
+ ***Maintaining an excel file*** mapping the rating of the recoring file with the file_id.
+ Open to suggestions to change the rating model according to certain parameters 
+ *Input -* A folder consisting of audio files
+ *Download result format -* **.xlsx**
+ *Private -* text extraction, transcription and quality score of call recordings happen 100% locally
+ *Fast -* uses [whisper-1](https://github.com/openai/whisper) model as the Whisper backend: get much faster transcription times on CPU!
+ *Local -* resultant excel file and transcripted files are stored locally!

# Setup

This code runs on python 3.x. So, please first consider installing python on your local machine before continuing.

The OpenAI Python library provides convenient access to the OpenAI API from applications written in the Python language.

```
pip install openai
```

```
pip install git+https://github.com/openai/whisper.git
```

Python has a built-in package called re, which can be used to work with Regular Expressions.

```
pip install regex
```

The OS module in Python provides functions for interacting with the operating system. OS comes under Python’s standard utility modules. 

```
pip install os-sys
```

 openpyxl - A Python library to read/write Excel 2010 xlsx/xlsm files

```
pip install openpyxl
```

# Instructions

Clone/Download the code to your local machine. Pull the code stubs/Unpack the file. Open your terminal/shell. Navigate to the project folder in your terminal.

> ***For Windows:*** 

***Open the Windows PowerShell as an Administrator and install the required packages given in the Setup section.*** 

And finally, run the `App.py` file in your terminal like below:

```
python App.py
```

The directory `/audioFiles` should contain the call recordings given as an input.

Bingo, now you have an excel file in the `/Results` directory named `data.xlsx` that contains the ratings of the recordings you were looking for. Enjoy! :tada:


## Areas of Improvement

+ Optimization of the rating model
+ Providing the feedback to the Sales person based on the conversation and the rating
+ Usage of different languages in recordings

## Future Scope

+ Creating a UI to display the statistics of the Sales team. (on team level/person-to-person level)
+ Saving the transcripts of some ideal calls done by the Sales team
+ Redefining the parameters that judge the quality of the calls
