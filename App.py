import re
import os
import src.AudioToTextConverter as AudioToTextConverter
import src.TranscriptMaker as TranscriptMaker
import src.Ratings as Ratings
import src.WriteInExcel as WriteInExcel
import src.ReadDataFromExcel as ReadDataFromExcel

# Define the folder path where the audio files are located
folder_path = "audioFiles"

# List all files in the folder
audio_files = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith((".mp3", ".wav", ".ogg"))]

# printing the names of audio and text file.
def print_audio_file(file_path, file_name):
    # Replace this with your actual code to process the audio file
    print(f"Processing audio file: {file_name} located at: {file_path}")

# Iterate through the list of audio files
for audio_file in audio_files:
    file_name = os.path.basename(audio_file)

    # generating the name for text file
    text_file_name = file_name.split('.')[0]
    text_file_name = text_file_name + '.txt'

    # call in the print method
    print_audio_file(audio_file, text_file_name)

    # calling the textConverter method to convert audio to text
    textData = AudioToTextConverter.textConverter(audio_file)

    # calling the TranscriptorGenerator method to convert the normal text to transcript conversation
    transcript = TranscriptMaker.TranscriptGenerator(textData)

    # calling the RatingChecker method to rate the generated transcript
    feedback = Ratings.RatingChecker(transcript)

    # print(feedback)

    input_string = feedback

    # extracting the rating from the feedback
    # Use a regular expression to find the digit before '/'
    match = re.search(r'(\d+)/\d+', input_string)
    ratingsInNumber = -1
    if match:
        digit_before_slash = match.group(1)
        ratingsInNumber = digit_before_slash
        print("digit_before_slash")
        print(digit_before_slash)
    else:
        print(" ")

    if(os.path.exists('Reports/data.xlsx')):
        #reading data from the excel file
        alreadyPresentData = ReadDataFromExcel.readData()
        #if data for this file is already present in the excel file
        if(file_name in alreadyPresentData):
            print("Already present: " + file_name)
        else:
            # writing the rating along with the file name to the excel file
            WriteInExcel.writeExcelData(file_name, text_file_name, ratingsInNumber)
    else:
        # writing the rating along with the file name to the excel file
        WriteInExcel.writeExcelData(file_name, text_file_name, ratingsInNumber)
