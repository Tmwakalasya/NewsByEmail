import requests
import os
from dotenv import load_dotenv
from send_email import send_email
load_dotenv()
email_user = os.getenv("EMAIL")
email_password = os.getenv("PASSWORD")
email_receiver = os.getenv("RECEIVER")
api_key = os.getenv("API_KEY")
url = f"https://newsapi.org/v2/everything?q=tesla&from=2023-11-13&sortBy=publishedAt&apiKey={api_key}"
request = requests.get(url)
content = request.json()
message = ""
print(content)
for article in content["articles"]:
    if article["title"] is not None:
        message += message + article["title"] + "\n" + article["description"] + 2 * "\n"
send_email(message=message,user=email_user,password=email_password,receiver=email_receiver)

