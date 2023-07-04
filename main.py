import requests
api_key = "0615f778dcd74240a6bc51ea815ce976"
# Endpoint is the actual url
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-05-11&sortBy=publishedAt&apiKey=0615f778dcd74240a6bc51ea815ce976"
# Make a request
requests = requests.get(url)
# Get a dictionary with the data
content = requests.json()
# Access the article titles and description
for article in content['articles']:
    print(article['title'])
    print(article['description'])