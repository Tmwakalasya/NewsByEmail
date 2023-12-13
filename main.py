import requests
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("API_KEY")
url = f"https://newsapi.org/v2/everything?q=tesla&from=2023-11-13&sortBy=publishedAt&apiKey={api_key}"
request = requests.get(url)
content = request.json()
# print(len(content["articles"]))
for article in content["articles"]:
    print(article["title"])
