import pyttsx3


class TextToSpeechEngine:
    ''' TextToSpeechEngine is used for converting any text used to audio.
    '''
    def __init__(self):
        self.engine = pyttsx3.init()

    
    def test_speak(self, message: str):
        ''' Converts text prompt into audio played out of speakers of your computer.

        Parameters:
        :param message: The text prompt.
        '''
        self.engine.say(message)
        self.engine.runAndWait()

    def writeMessageToAudioFile(self, message: str, filePath: str):
        ''' Converts text prompt into audio file.

        Parameters:
        :param message: The text prompt.
        :param filePath: The file path of the audio file.
        '''
        self.engine.save_to_file(message, filePath)
        self.engine.runAndWait()

# engine = pyttsx3.init()
# engine.say("I will speak this text")
# engine.runAndWait()