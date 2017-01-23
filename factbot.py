from bs4 import BeautifulSoup
import requests
from lxml import html
# from fact_bot_portal.models import Fact


def scrapeFacts():
    for x in range(0, 5):
        page = requests.get('http://www.randomfunfacts.com/')
        tree = (page.content)
        soup = BeautifulSoup(tree, 'html.parser')
        data = []
        f = soup.find_all("i")[0].string
        # fact = { 'text': f }
        # data.append(fact)
        # fact1 = Fact(text=data.text)
        # fact1.save()
        # return data
        print(f)

# scrapeFacts()
