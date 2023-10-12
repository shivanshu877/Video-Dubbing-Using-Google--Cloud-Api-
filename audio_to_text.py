import io
import os

from google.cloud import speech_v1p1beta1 as speech
from google.oauth2 import service_account


def divide_file_into_chunks(file_path, chunk_size=1024 * 1024):
    """Divides a file into chunks of the specified size.

    Args:
        file_path: The path to the file to divide.
        chunk_size: The size of each chunk in bytes.

    Returns:
        A list of chunks, each of which is a byte array.
    """

    chunks = []
    with open(file_path, "rb") as f:
        while True:
            chunk = f.read(chunk_size)
            if chunk:
                chunks.append(chunk)
            else:
                break
    return chunks


def send_chunk_to_speech_to_text(chunk):
    # Create a service account credentials object
    credentials = service_account.Credentials.from_service_account_file("key.json")

    # Create a Speech-to-Text client with the service account credentials
    client = speech.SpeechClient(credentials=credentials)

    # Define the configuration for the speech recognition request
    config = speech.RecognitionConfig()
    config.encoding = speech.RecognitionConfig.AudioEncoding.LINEAR16
    config.sample_rate_hertz = 44100
    config.language_code = "en-US"

    # Define the audio data
    audio = speech.RecognitionAudio(content=chunk)

    # Make the speech recognition request
    response = client.recognize(config=config, audio=audio)

    # Extract the transcripts from the response
    transcripts = []
    for result in response.results:
        for alternative in result.alternatives:
            transcripts.append(alternative.transcript)

    return transcripts


def transcribe_big_audio_file(file_path):
    """Transcribes a big audio file using Google Cloud Speech-to-Text API using service account credentials.

    Args:
        file_path: The path to the audio file to transcribe.

    Returns:
        A list of strings, each of which is a transcript of the audio data.
    """

    # Divide the file into chunks
    chunks = divide_file_into_chunks(file_path)

    # Transcribe each chunk
    transcripts = []
    for chunk in chunks:
        transcripts.extend(send_chunk_to_speech_to_text(chunk))

    return transcripts


# Transcribe the big audio file
transcripts = transcribe_big_audio_file("mono_left.wav")

# Save the transcripts to a file
with open("big_audio_file_transcript.txt", "w") as f:
    for transcript in transcripts:
        f.write(transcript + "\n")
