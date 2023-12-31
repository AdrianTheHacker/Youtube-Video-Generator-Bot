from dotenv import dotenv_values
import requests

import json
import os

from Tools.StockFootageClipMaker import StockFootageClipMaker
from Tools.TextToSpeechEngine import TextToSpeechEngine


def getDataFromAPI() -> list:
    '''
    Retrieves stories from Reddit API.

    Returns:
        list: A list of various responces from the Reddit API.
    '''

    url = "https://socialgrep.p.rapidapi.com/search/posts"   
    querystring = {"query":"new,/r/horrorstories"}

    envValues: dict = dotenv_values("..\\secrets\\.env")
    rapidAPIKey = envValues["X-RapidAPI-Key"]
    rapidAPIHost = envValues["X-RapidAPI-Host"]

    headers = {
	    "X-RapidAPI-Key": rapidAPIKey,
	    "X-RapidAPI-Host": rapidAPIHost
    }

    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    print(data)
    return data


def formatTitleForFileName(title: str) -> str:
    '''
    Formats the title of the file name to only use friendly characters.

    Returns:
        str: The string of the title ommiting all unfriendly characters.
    '''

    forbiddenFileNameCharacters = ["<", ">", ":", '"', "/", '\ '.replace(" ", ""), "|", "?", "*"]

    for character in forbiddenFileNameCharacters:
        title = title.replace(character, "")
    title = title.replace(" ", "_")

    return title


def createAudioFile(outputAudioFilePath: str, storyTitle: str, storyText: str):
    '''
    Use TextToSpeechEngine to convert a given story into audio.

    Args:
        outputAudioFilePath (str): The file that the audio will be stored in.
        storyTitle (str): The title of the given story.
        storyText (str): The contents of the given story.
    '''

    textToSpeechEngine = TextToSpeechEngine()
    textToSpeechEngine.writeTextFileToAudioFile(f"{storyTitle}\n\n{storyText}", outputAudioFilePath)


def createVideo(stockFootageVideoFilePath: str, audioFilePath: str, outputVideoFilePath: str):
    '''
    Creates a video given a stock footage file and an audio file.

    Args:
        stockFootageVideoFilePath (str): The file path to the stock footage used.
        audioFilePath (str): The audio file that will be used in the final video.
        outputVideoFilePath (str): The path to the file where the final video will be saved.
    '''

    stockFootageClipMaker = StockFootageClipMaker(stockFootageVideoFilePath,
                                                  audioFilePath,
                                                  outputVideoFilePath)
    stockFootageClipMaker.makeVideoClip()
    os.remove(audioFilePath)


def main():
    data = getDataFromAPI()

    for storyNumber, storyContent in enumerate(data["data"]):
        if storyContent["selftext"] == None: continue
        if len(storyContent["selftext"]) < 20: continue

        title = storyContent["title"]
        text = storyContent["selftext"]

        fileNameTitle: str = f"Story{storyNumber}_{formatTitleForFileName(title)}"
        outputAudioFilePath = f"Media\\Output_Audio\\{fileNameTitle}.mp3":
        outputVideoFilePath = f"Media\\Output_Videos\\{fileNameTitle}.mp4"
        stockVideoFilePath = "Media\\Stock_Videos\\Video1-MinecraftParkour.mp4"
        
        createAudioFile(outputAudioFilePath, title, text)
        createVideo(stockVideoFilePath, outputAudioFilePath, outputVideoFilePath)


if __name__ == '__main__':
    main()
