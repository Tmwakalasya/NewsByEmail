import requests
import os
from dotenv import load_dotenv
from send_email import send_email

load_dotenv()
email_user = os.getenv("EMAIL")
email_password = os.getenv("PASSWORD")
email_receiver = os.getenv("RECEIVER")
api_key = os.getenv("API_KEY")

# The q parameter stands for the topic
url = (f"https://newsapi.org/v2/everything?"
       f"q=tesla&"
       f"sortBy=publishedAt&"
       f"apiKey={api_key}")

request = requests.get(url)

# Get a dictionary with data:
content = request.json()
message = ""

for article in content.get("articles", [])[:20]:
    title = article.get("title")
    description = article.get("description")
    url = article.get("url")

    if title is not None:
        message += ("Subject: Today's news" + "\n"
                    + (title + "\n"
                       + description + url + 2 * "\n"))
message = message.encode("utf-8")
send_email(message=message)
