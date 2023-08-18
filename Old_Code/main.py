# # Importing packages required
# # from moviepy.video.io.VideoFileClip import VideoFileClip
# # from moviepy.audio.io.AudioFileClip import AudioFileClip
# from moviepy.editor import VideoFileClip, AudioFileClip, CompositeAudioClip

# # The sample files used (For testing only)
# videoFile: str = "video\\sampleVideo3.mp4"
# audioFile: str = "audio\\sampleAudio.mp3"
# audioFile2: str = "audio\\sampleAudio2.mp3"
# outputFile: str = "output_videos\\sampleOutputVideo.mp4"

# # Creates clips for both audio and video
# videoFileClip: VideoFileClip = VideoFileClip(videoFile)
# audioFileClip: AudioFileClip = AudioFileClip(audioFile)
# audioFileClip2: AudioFileClip = AudioFileClip(audioFile2)

# final_audio = CompositeAudioClip([audioFileClip, audioFileClip2])
# final_audio.set_duration(videoFileClip.duration)

# # Creates the new clip and writes it to a new file
# newVideoFileClip = videoFileClip.set_audio(final_audio)
# newVideoFileClip.write_videofile("output_videos\\sampleOutputVideo.mp4")

# # Closes all the files opened
# videoFileClip.close()
# audioFileClip.close()
# newVideoFileClip.close()
# final_audio.close()
