from bs4 import BeautifulSoup
import requests

url = "https://example.com"

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html.parser")

print(soup.prettify())

title = soup.find("title")

print(title.text)

paragraphs = soup.find_all("p")
for paragraph in paragraphs:
    print(paragraph.text)
    
highlights = soup.find_all("p", class_="highlight")
for highlight in highlights:
    print(highlight.text)
    
links = soup.find_all("a")
for link in links:
    print(link["href"])