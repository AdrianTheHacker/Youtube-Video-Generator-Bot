from moviepy.editor import AudioFileClip
from moviepy.editor import VideoFileClip

from random import randint


class StockFootageClipMaker:
    def __init__(self, videoFilePaths: list):
        self.videos = videoFilePaths

    def makeVideoClip(self):
        # For testing purposes clips will be 5 seconds.
        videoClipLength = 0.05 # MoviePy treats this as 5 seconds (min.sec)
        videoIndex = randint(0, len(self.videos) - 1)
        video = self.videos[videoIndex]

        videoLength = VideoFileClip(video).duration
        print(videoLength)
    