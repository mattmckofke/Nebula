from bs4 import BeautifulSoup
import requests
import pandas as pd

# Fetch the webpage
response = requests.get("http://books.toscrape.com")
html_content = response.text

# Parse the HTML
soup = BeautifulSoup(html_content, "html.parser")

# Initialize lists to store scraped data
titles = []
prices = []
availability = []

# Loop through each book
for book in soup.find_all("article", class_="product_pod"):
    titles.append(book.find("h3").find("a")["title"])
    price_element = book.find("p", class_="price_color")
    if price_element and price_element.text:
        prices.append(price_element.text.replace('Â', '').strip("£"))  # Remove the pound sign and non-breaking space
    availability_element = book.find("p", class_="instock availability")
    if availability_element and availability_element.text:
        availability.append(availability_element.text.strip())

# Convert prices to floats
prices = [float(price) for price in prices]

# Display scraped data
print(titles)
print(prices)
print(availability)

# Create a DataFrame
data = {"Title": titles, "Price (£)": prices, "Availability": availability}
df = pd.DataFrame(data)

print(df.head())  # Display the first few rows of the DataFrame

# Calculate the average price
average_price = df["Price (£)"].mean()
print(f"Average Price: £{average_price:.2f}")

# Count books under £10
cheap_books = df[df["Price (£)"] < 10]
print(f"Number of books under £10: {len(cheap_books)}")