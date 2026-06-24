import requests
import pandas as pd
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0'
}

response = requests.get('https://books.toscrape.com/', headers=headers).text
soup = BeautifulSoup(response, 'html.parser')

books = soup.find_all('article', class_='product_pod')

name = []
price = []
rating = []

convert = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

for i in books:

    # title
    name.append(i.h3.a['title'])

    # price
    price.append(i.find('p', class_='price_color').text.strip())

    # rating (extract class)
    rating_class = i.find('p', class_='star-rating')['class'][1]

    # convert to number
    rating.append(convert[rating_class])

df = pd.DataFrame({
    'name': name,
    'price': price,
    'rating': rating
})

print(df)

df.to_csv('book.csv')