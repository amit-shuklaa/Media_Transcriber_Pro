import requests

# Replace with your Deepgram API key
DEEPGRAM_API_KEY = 'f0b317d5bd1b670d58b6e8c268f7c909de129913'
DEEPGRAM_API_URL = 'https://api.deepgram.com/v1/listen'

# Path to your audio file
audio_file_path = 'C:\\Users\\ammy0\\Desktop\\Code For Python\\Internship\\extracted_audio.mp3'  # Update this path

headers = {
    'Authorization': f'Token {DEEPGRAM_API_KEY}',
    'Content-Type': 'audio/mpeg',  # Change if your audio format is different
}

# Read the audio file
with open(audio_file_path, 'rb') as audio_file:
    response = requests.post(DEEPGRAM_API_URL, headers=headers, data=audio_file)

if response.status_code == 200:
    response_json = response.json()
    print("Response JSON:", response_json)  # Debugging line
    if 'channel' in response_json:
        transcript = response_json['channel']['alternatives'][0]['transcript']
        print("Transcript:", transcript)
    else:
        print("Error: 'channel' key not found in the response.")
        print("Full response:", response_json)
else:
    print("Error:", response.status_code, response.text)
