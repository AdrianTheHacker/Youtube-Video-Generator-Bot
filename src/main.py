from dotenv import dotenv_values

import requests
import json
import os

from Tools.StockFootageClipMaker import StockFootageClipMaker
from Tools.TextToSpeechEngine import TextToSpeechEngine


def main():
    # url = "https://socialgrep.p.rapidapi.com/search/posts"

    # querystring = {"query":"/r/horrorstories"}

    # envValues: dict = dotenv_values("..\\secrets\\.env")
    # rapidAPIKey = envValues["X-RapidAPI-Key"]
    # rapidAPIHost = envValues["X-RapidAPI-Host"]

    # headers = {
	  #   "X-RapidAPI-Key": "Check .ENV",
	  #   "X-RapidAPI-Host": "Check .ENV"
    # }

    # response = requests.get(url, headers=headers, params=querystring)
    # data = response.json()

    file: str = ".\\test.json"

    with open(file, "r", encoding="utf8") as dataFile:
        data = json.load(dataFile)
    dataFile.close()

    for storyNumber, storyContent in enumerate(data["data"]):
        if storyContent["selftext"] == None: continue
        if len(storyContent["selftext"]) < 20: continue

        title = storyContent["title"]
        text = storyContent["selftext"]

        print(title)
        print(text)

        outputAudioDirectory = "Media\\Output_Audio"
        outputVideoDirectory = "Media\\Output_Videos"
        stockVideosDirectory = "Media\\Stock_Videos"

        textToSpeechEngine = TextToSpeechEngine()
        textToSpeechEngine.writeTextFileToAudioFile(f"{title}\n\n{text}", f"{outputAudioDirectory}\\Story{storyNumber}.mp3")

        stockFootageClipMaker = StockFootageClipMaker(f"{stockVideosDirectory}\\Video1-MinecraftParkour.mp4", 
                                                      f"{outputAudioDirectory}\\Story{storyNumber}.mp3", 
                                                      f"{outputVideoDirectory}\\Story{storyNumber}.mp4")
        stockFootageClipMaker.makeVideoClip()

        os.remove(f"{outputAudioDirectory}\\Story{storyNumber}.mp3")



    # url: str = "https://api.dictionaryapi.dev/api/v2/entries/en/programming"

    # response = requests.get(url)
    # responseDict: dict = response.json()

    # print(responseDict)



    # storyFilePath = "Media\\Stories\\Story2.txt"

    # textToSpeechEngine = TextToSpeechEngine()
    # textToSpeechEngine.formatTextFile(storyFilePath)

    # with open(storyFilePath, "r") as file:
    #     story = file.read()
    # file.close()

    # textToSpeechEngine.writeTextFileToAudioFile(story, "Media\\Output_Audio\\Story1.mp3")

    # stockFootageClipMaker = StockFootageClipMaker("Media\\Stock_Videos\\Video1-MinecraftParkour.mp4", "Media\\Output_Audio\\Story1.mp3", "Media\\Output_videos\\test.mp4")
    # stockFootageClipMaker.makeVideoClip()



    # print("Hello, world")

    # url = "https://socialgrep.p.rapidapi.com/search/posts"

    # querystring = {"query":"/r/horrorstories"}

    # headers = {
	  #   "X-RapidAPI-Key": "Check .ENV",
	  #   "X-RapidAPI-Host": "Check .ENV"
    # }

    # response = requests.get(url, headers=headers, params=querystring)

    # print(response.json())


if __name__ == '__main__':
    main()
