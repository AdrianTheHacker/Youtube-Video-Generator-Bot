# Importing packages required
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.audio.io.AudioFileClip import AudioFileClip

# The sample files used (For testing only)
videoFile: str = "video\\sampleVideo.mp4"
audioFile: str = "audio\\sampleAudio.mp3"

# Creates clips for both audio and video
videoFileClip: VideoFileClip = VideoFileClip(videoFile)
audioFileClip: AudioFileClip = AudioFileClip(audioFile)

# Cuts audio file to match length of video
audioFileClip: AudioFileClip = audioFileClip.set_duration(videoFileClip.duration)

# Creates the new clip and writes it to a new file
newVideoFileClip = videoFileClip.set_audio(audioFileClip)
newVideoFileClip.write_videofile("output_videos\\sampleOutputVideo.mp4")

# Closes all the files opened
videoFileClip.close()
audioFileClip.close()
newVideoFileClip.close()
