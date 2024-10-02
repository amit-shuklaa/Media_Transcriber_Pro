import requests
import json

# An API key is defined here. You'd normally get this from the service you're accessing. It's a form of authentication.
XI_API_KEY = "sk_0cacdf11b9795d3998d61ef44b2a6757e7e5b971792292ba"

# This is the URL for the API endpoint we'll be making a GET request to.
url = "https://api.elevenlabs.io/v1/voices"

# Here, headers for the HTTP request are being set up.
# Headers provide metadata about the request. In this case, we're specifying the content type and including our API key for authentication.
headers = {
"Accept": "application/json",
"xi-api-key": XI_API_KEY,
"Content-Type": "application/json"
}

# A GET request is sent to the API endpoint. The URL and the headers are passed into the request.
response = requests.get(url, headers=headers)

# The JSON response from the API is parsed using the built-in .json() method from the 'requests' library.
# This transforms the JSON data into a Python dictionary for further processing.
data = response.json()

# A loop is created to iterate over each 'voice' in the 'voices' list from the parsed data.
# The 'voices' list consists of dictionaries, each representing a unique voice provided by the API.
for voice in data['voices']:
 print(f"{voice['name']}; {voice['voice_id']}")