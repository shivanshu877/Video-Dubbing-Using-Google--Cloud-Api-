import requests
import json

def translate_text(contents, target_language, api_key):
    """Translates input text and returns translated text using the Google Cloud Translation API.

    Args:
        contents: The text to translate.
        target_language: The target language code.
        api_key: Your Google Cloud API key.

    Returns:
        A string containing the translated text or None if an error occurs.
    """
    
    endpoint = "https://translate.googleapis.com/language/translate/v2"
    
    # Construct the request payload
    request_data = {
        "q": contents,
        "target": target_language,
        "key": api_key,
    }

    # Send the translation request
    response = requests.post(endpoint, data=request_data)
    
    # Check for successful response
    if response.status_code == 200:
        try:
            translation = response.json()
            translated_text = translation["data"]["translations"][0]["translatedText"]
            return translated_text
        except json.JSONDecodeError as e:
            print(f"Failed to decode JSON response: {e}")
    else:
        print(f"Error: {response.status_code}")
    
    return None

# Replace 'YOUR_API_KEY' with your actual Google Cloud API key
api_key = "AIzaSyBM3YgZB9XHr3mGiIydMLhbE685O8_mFXE"

# Example text to translate
with open("big_audio_file_transcript.txt", "r") as f:
    file_contents = f.read()

# Translate the text to a target language (e.g., "hi" for Hindi)
target_language = "hi"

translation = translate_text(file_contents, target_language, api_key)

# with open("another_lang_conversion.txt", "w") as f:
#     f.write(translation)

# Print the translated text
if translation is not None:
    print(translation)
else:
    print("Translation failed.")


