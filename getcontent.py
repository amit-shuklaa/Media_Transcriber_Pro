import requests
from bs4 import BeautifulSoup

# Define the URL of the website to scrape
url = "https://techcrunch.com/2024/04/30/sams-clubs-ai-powered-exit-tech-reaches-20-of-stores/"  # Replace with the target website

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract desired content (e.g., all paragraphs)
    paragraphs = soup.find_all('p')  # Modify this to target specific content

    # Print the extracted content
    for para in paragraphs:
        print(para.text)
else:
    print(f"Failed to retrieve content: {response.status_code}")