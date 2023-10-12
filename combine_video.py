from moviepy.editor import VideoFileClip, AudioFileClip, clips_array

# Load the video file and audio file
video_path = "video.mp4"  # Replace with the path to your video file
audio_path = "combined_output.wav"  ## Replace with the path to your audio file

video_clip = VideoFileClip(video_path)
audio_clip = AudioFileClip(audio_path)

# Get the duration of the video and audio
video_duration = video_clip.duration
audio_duration = audio_clip.duration

# Check if the audio duration is longer than the video duration
if audio_duration > video_duration:
    # Calculate the audio speed adjustment factor
    speed_factor = audio_duration / video_duration
    
    # Set the audio speed to match the video duration
    audio_clip = audio_clip.speedx(speed_factor)

# Set the audio of the video to the adjusted audio
video_clip = video_clip.set_audio(audio_clip)

# Export the combined video with adjusted audio
output_path = "combined_video.mp4"  # Specify the output video file path
video_clip.write_videofile(output_path, codec="libx264")

print(f"Combined video saved to {output_path}")
