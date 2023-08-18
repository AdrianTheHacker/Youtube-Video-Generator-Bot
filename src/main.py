import pyttsx3

from Tools.StockFootageClipMaker import StockFootageClipMaker
from Tools.TextToSpeechEngine import TextToSpeechEngine

def main():
    storyFilePath = "Media\\Stories\\Story1.txt"

    textToSpeechEngine = TextToSpeechEngine()
    textToSpeechEngine.formatTextFile(storyFilePath)

    with open(storyFilePath, "r") as file:
        story = file.read()
    file.close()

    textToSpeechEngine.writeMessageToAudioFile(story, "Media\\Output_Audio\\Story1.mp3")

    stockFootageClipMaker = StockFootageClipMaker("Media\\Stock_Videos\\Video1-MinecraftParkour.mp4", "Media\\Output_Audio\\Story1.mp3")
    stockFootageClipMaker.makeVideoClip()


if __name__ == '__main__':
    main()
