from moviepy.editor import AudioFileClip
from moviepy.editor import VideoFileClip

from random import randint, random


class StockFootageClipMaker:
    ''' StockFootageClipMaker is the class responsible for managing the creation of the short videos.

    Parameters:
    :param videoFilePath: The path to the stock footage video.
    :param audioFilePath: The path to the audio file.
    :param outputVideoPath: The path to location of the output video produced.
    '''
    def __init__(self, videoFilePath: str, audioFilePath: str, outputVideoPath: str):
        self.videoFilePath = videoFilePath
        self.audioFilePath = audioFilePath
        self.outputVideoPath = outputVideoPath

    def makeVideoClip(self):
        ''' Creates a movie clip that is equal length to the audio clip.
        The given movie clip will start at a random interval in the stock footage.
        '''
        videoClip = VideoFileClip(self.videoFilePath)
        audioClip = AudioFileClip(self.audioFilePath)

        videoClipLength = audioClip.duration

        # videoClipStart = (randint(100, (videoClip.duration - videoClipLength) * 100)) * 0.01
        videoClipStart = ((random() * 10) * (videoClip.duration - videoClipLength)) / 10
        videoClipEnd = videoClipStart + videoClipLength

        print(audioClip.duration)
        print(videoClip.duration)

        videoClip = videoClip.cutout(0, videoClipStart)
        videoClip = videoClip.cutout(audioClip.duration, videoClip.duration)

        print(videoClip.duration)

        videoClip = videoClip.set_audio(audioClip)
        # videoClip.write_videofile(self.outputVideoPath)

        try:
            videoClip.write_videofile(self.outputVideoPath)
        except OSError:
            print(f"Error Creating Video")
            print(f"Length: {videoClip.duration}")

        videoClip.close()
        audioClip.close()
    