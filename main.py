import requests, random

url = "https://type.fit/api/quotes"
quotes = requests.get(url).json()

random_quote = random.choice(quotes)
print(f"{random_quote['text']}\n  author: {random_quote['author']}")
