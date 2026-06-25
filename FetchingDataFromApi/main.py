import requests
import pandas as pd

url = "https://dogapi.dog/api/v2/breeds"

response = requests.get(url)
data = response.json()

# extract only attributes
rows = [item["attributes"] for item in data["data"]]

df = pd.DataFrame(rows)

# print(df)

df.shape

df.to_csv('dog.csv')