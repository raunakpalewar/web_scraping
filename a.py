import requests
from bs4 import BeautifulSoup

def scrape_web_content(topic):
    # Make a GET request to the URL to fetch the HTML content
    url=f'https://timesofindia.indiatimes.com/topic/{topic}'
    response = requests.get(url)

    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the content you want (for example, extracting all paragraphs)
        all_paragraphs = soup.find_all('p')

        # Join all paragraphs to create a single string of content
        content_text = '\n'.join([p.get_text() for p in all_paragraphs])

        return content_text
    else:
        print("Failed to fetch the content")
        return None

def save_to_file(content, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"Scraped content saved to '{filename}'")

# URL of the website you want to scrape
topic = input('Enter the news topic : ')

# File name for the text file to save the content
file_name = f"scraped_content {topic}.txt"  # File name for the saved content

# Call the function to scrape the web content
scraped_content = scrape_web_content(topic)

if scraped_content:
    save_to_file(scraped_content, file_name)
