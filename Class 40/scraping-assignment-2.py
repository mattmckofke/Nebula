from bs4 import BeautifulSoup
import requests
import pandas as pd

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
response = requests.get('https://www.goodreads.com/list/show/1652.Favorite_picture_books', headers=headers)
html_content = response.text

# Parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')

td_tags = soup.find_all('td')

for idx, td in enumerate(td_tags, start=1):

    star_span = td.find('span', class_='minirating')
    if star_span:
        print(star_span.text)

print(len(td_tags))