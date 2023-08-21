import pyttsx3

import requests

from Tools.StockFootageClipMaker import StockFootageClipMaker
from Tools.TextToSpeechEngine import TextToSpeechEngine


def main():
    storyFilePath = "Media\\Stories\\Story2.txt"

    textToSpeechEngine = TextToSpeechEngine()
    textToSpeechEngine.formatTextFile(storyFilePath)

    with open(storyFilePath, "r") as file:
        story = file.read()
    file.close()

    textToSpeechEngine.writeTextFileToAudioFile(story, "Media\\Output_Audio\\Story1.mp3")

    stockFootageClipMaker = StockFootageClipMaker("Media\\Stock_Videos\\Video1-MinecraftParkour.mp4", "Media\\Output_Audio\\Story1.mp3", "Media\\Output_videos\\test.mp4")
    stockFootageClipMaker.makeVideoClip()

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
