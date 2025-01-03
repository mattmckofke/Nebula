from bs4 import BeautifulSoup
import requests
import pandas as pd
import nltk
from nltk.corpus import stopwords

#nltk.download("stopwords")
stop_words = stopwords.words("english")
print(stop_words)
def remove_stopwords(text):
    filtered = []
    for w in text.split():
        if str(w).lower not in stop_words:
            filtered.append(w)
    
    print(filtered)
    return " ".join(filtered)

quotes = []
authors = []
tags = []

for i in range(1, 11):
    # Fetch the webpage
    response = requests.get(f"http://quotes.toscrape.com/page/{i}/")
    html_content = response.text

    # Parse the HTML
    soup = BeautifulSoup(html_content, "html.parser")
    
    for quote in soup.find_all("div", class_="quote"):
        authors.append(quote.find("small", class_="author").text)
        quotes.append(quote.find("span", class_="text").text)
        tags.append([tag.text for tag in quote.find_all("a", class_="tag")])
        
data = {"Author": authors, "Quotes": quotes, "Tags": tags}
df = pd.DataFrame(data)

example = remove_stopwords(quotes[0])
print(example)
# Need to remove start and end quotes from quotes
# 