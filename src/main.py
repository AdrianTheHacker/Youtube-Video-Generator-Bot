import pyttsx3
from Tools.TextToSpeechEngine import TextToSpeechEngine

def main():
    textToSpeechEngine = TextToSpeechEngine()
    textToSpeechEngine.writeMessageToAudioFile("Hello, World!", "Audio\\HelloWorld.mp3")


if __name__ == '__main__':
    main()
