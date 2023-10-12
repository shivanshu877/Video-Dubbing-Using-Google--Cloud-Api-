from pydub import AudioSegment
import os

# Specify the folder containing the WAV files
folder_path = "audio_chunks"  # Replace with the path to your folder

# Get a list of all WAV files in the folder
wav_files = [file for file in os.listdir(folder_path) if file.endswith(".wav")]

# Check if there are WAV files in the folder
if not wav_files:
    print("No WAV files found in the folder.")
    exit()

# Sort the WAV files in the correct order based on their names
wav_files.sort(key=lambda x: int(x.split("_")[1].split(".")[0]))

# Initialize an empty AudioSegment to store the combined audio
combined_audio = AudioSegment.empty()

# Combine all WAV files in sequential order
for wav_file in wav_files:
    audio = AudioSegment.from_file(os.path.join(folder_path, wav_file), format="wav")
    combined_audio += audio

# Specify the output file name and path
output_file = "combined_output.wav"

# Export the combined audio to a single WAV file
combined_audio.export(output_file, format="wav")

print(f"Combined audio saved to {output_file}")
