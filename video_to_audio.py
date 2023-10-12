from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_audio
import os

# Input video file path
video_file = "video.mp4"

# Output audio file path (MP3)
audio_file = "output_audio.mp3"

# Extract audio from the video and save it as MP3
ffmpeg_extract_audio(video_file, audio_file)

print(f"Audio extracted and saved as {audio_file}")