from dotenv import dotenv_values

import requests
import json
import os

from Tools.StockFootageClipMaker import StockFootageClipMaker
from Tools.TextToSpeechEngine import TextToSpeechEngine


def main():
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


    for storyNumber, storyContent in enumerate(data["data"]):
        if storyContent["selftext"] == None: continue
        if len(storyContent["selftext"]) < 20: continue

        title = storyContent["title"]
        text = storyContent["selftext"]

        outputAudioDirectory = "Media\\Output_Audio"
        outputVideoDirectory = "Media\\Output_Videos"
        stockVideosDirectory = "Media\\Stock_Videos"

        textToSpeechEngine = TextToSpeechEngine()
        textToSpeechEngine.writeTextFileToAudioFile(f"{title}\n\n{text}", f"{outputAudioDirectory}\\Story{storyNumber}_{storyContent[title]}.mp3")

        stockFootageClipMaker = StockFootageClipMaker(f"{stockVideosDirectory}\\Video1-MinecraftParkour.mp4", 
                                                      f"{outputAudioDirectory}\\Story{storyNumber}.mp3", 
                                                      f"{outputVideoDirectory}\\Story{storyNumber}.mp4")
        stockFootageClipMaker.makeVideoClip()

        os.remove(f"{outputAudioDirectory}\\Story{storyNumber}.mp3")


if __name__ == '__main__':
    main()
