import pyttsx3


class TextToSpeechEngine:
    ''' TextToSpeechEngine is used for converting any text used to audio.
    '''
    def __init__(self):
        self.engine = pyttsx3.init()

    def formatTextFile(self, filePath: str):
        ''' Formats text files to remove all instances of â€™ to replace with '.

        Parameters:
        :param filePath: The given text file's file path.
        '''
        with open(filePath, "r") as file:
            text = file.read()
        file.close()

        text = text.replace("â€™", "'")

        with open(filePath, "w") as file:
            file.write(text)
        file.close()

    def testSpeak(self, message: str):
        ''' Converts text prompt into audio played out of speakers of your computer.

        Parameters:
        :param message: The text prompt.
        '''
        self.engine.say(message)
        self.engine.runAndWait()

    def writeTextFileToAudioFile(self, message: str, filePath: str):
        ''' Converts text prompt into audio file.

        Parameters:
        :param message: The text prompt.
        :param filePath: The file path of the audio file.
        '''
        self.engine.save_to_file(message, filePath)
        self.engine.runAndWait()
