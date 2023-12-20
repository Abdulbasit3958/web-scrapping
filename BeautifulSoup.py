# Import the necessary libraries
from bs4 import BeautifulSoup 
import requests

# Define the root URL of the website and the specific page for movies starting with 'A'
root = 'https://subslikescript.com'
base_website = f'{root}/movies_letter-A'

# Send a GET request to the website and get the HTML content of the page
result = requests.get(base_website)
content = result.text

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(content, 'lxml')

# Find the pagination section and determine the number of pages
pagination = soup.find('ul', class_='pagination')
pages = pagination.find_all('li', class_='page-item')
last_page = pages[-2].text

# Iterate over the first four pages to collect movie script links
for page in range(1, int(last_page) + 1)[:4]:
    # Construct the URL for each page
    website = f'{base_website}?page={page}'
    result = requests.get(website)
    content = result.text
    soup = BeautifulSoup(content, 'lxml')

    # Find the main content area and initialize a list for links
    box = soup.find('article', class_='main-article')
    page_links = []

    # Extract all the 'href' attributes of 'a' tags within this area
    for link in box.find_all('a', href=True):
        page_links.append(link['href'])

    # For each movie script link, extract and save the script
    for link in page_links: 
        try:
            # Print the link (useful for debugging)
            print(link)
            # Request the content of the movie script page
            result = requests.get(f'{root}/{link}')
            content = result.text
            soup = BeautifulSoup(content, 'lxml')
    
            # Find the title and transcript of the movie script
            box = soup.find('article', class_='main-article')
            title = box.find('h1').get_text() 
            transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')
            
            # Open a file named after the movie title and append the transcript
            with open(f'{title}.txt', 'a', encoding='utf-8') as file:
                file.write(transcript + '\n\n')
        
        # Error handling for broken links or parsing errors
        except: 
            print('--------link not working--------')
            print(link)
