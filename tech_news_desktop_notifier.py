import requests
import notify2
import time
import datetime
import os
from dotenv import load_dotenv

# get api key from .env file
load_dotenv()
API_KEY = os.getenv("NEWS_API_KEY")


def main():
    response = requests.get(
        f"https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey={API_KEY}")
    data = response.json()
    articles = data["articles"]

    notify2.init("Tech news notification app")

    item_num = 1
    for article in articles:
        title = article['title']
        description = article["description"]

        if title == None:
            title = "Empty title"
        elif description == None:
            description = "Empty description"

        # show every titles in articles for every 8 seconds
        notification = notify2.Notification(
            f"{item_num}. {title}", description)
        notification.show()
        time.sleep(8)

        # after showing news notification add it to a txt file
        news = f"{item_num}. {title} {description}"
        today = datetime.date.today()

        with open(f"Tech news {today}.txt", "a") as file:
            file.write(news + "\n\n")

        item_num += 1

    notification.close()


main()
