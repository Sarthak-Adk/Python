import pandas as pd
import requests
from bs4 import BeautifulSoup

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

headers = {
    'User-Agent': 'Mozilla/5.0'
}

for j in range(2, 10):

    url = f'https://books.toscrape.com/catalogue/page-{j}.html'
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    books = soup.find_all('article', class_='product_pod')



    for i in books:
        # title
        name.append(i.h3.a['title'])

        # price
        price.append(i.find('p', class_='price_color').text.strip())

        # rating
        rating_class = i.find('p', class_='star-rating')['class'][1]
        rating.append(convert[rating_class])

df = pd.DataFrame({
    'name': name,
    'price': price,
    'rating': rating
})


print(df)