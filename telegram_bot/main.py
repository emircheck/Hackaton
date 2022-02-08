import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time


def get_first_news():
    header = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    }
    url ="https://kaktus.media/"
    r = requests.get(url=url, headers=header)

    soup = BeautifulSoup(r.text, "lxml")
    articles_cards = soup.find_all("div", class_="Tag--article")

    for article in articles_cards:
        article_title = article.find("a", class_="ArticleItem--name").text.strip()
        article_url = f'https://kaktus.media{article.get}'
        article_date_time = article.find("div", class_="ArticleItem--time").get("date")

        date_from_iso = datetime.fromisoformat(article_date_time)
        date_time = datetime.strftime(date_from_iso, "%Y-%m-%d %H:%M:%S")
        article_date_timestamp = time.mktime(datetime.strftime(date_time,"%Y-%m-%d %H:%M:%S").timetuple())

        print(f"{article_title} | {article_url} | {article_date_timestamp}")
    

get_first_news()
