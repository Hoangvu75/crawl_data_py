import requests
from bs4 import BeautifulSoup

# Set the base URL for the website
base_url = 'https://phongtro123.com/tinh-thanh/ho-chi-minh?page='

# Set the number of pages you want to crawl
num_pages = 5

# Crawl data from each page
for page in range(1, num_pages + 1):
    # Send an HTTP GET request to the website
    website = f"{base_url}{page}"
    response = requests.get(website)

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the elements containing movie information
    objects = soup.find_all('h3', class_='post-title')

    for object in objects:
        soup = BeautifulSoup(str(object), 'html.parser')
        text = soup.get_text()
        print(text)


