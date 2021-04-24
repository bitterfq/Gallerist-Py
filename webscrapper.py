import requests
from bs4 import BeautifulSoup
import imagehandler

class Message:
    def __init__(self, title, metadata, url):
        self.title = title
        self.metadata = metadata
        self.url = url 


def scrape():
    URL = "https://www.slam.org/explore-the-collection/object-of-the-day/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    page = requests.get(URL, headers= headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    titles = soup.find_all(
        "section", "component component--media component--reduced-spacing")
 
    meta = soup.find_all("section", "component component--text")

    emb_msg = Message("", "", "")

    for title in titles:
        _title = title.find('h2')
        img = title.find('img')
        print(_title.text)
        print()
        print(img['data-src'])
        emb_msg.title = _title.text
        emb_msg.url = img['data-src']
        break

    for data in meta:
        mt_data = data.find("p")
        print(mt_data.text)
        emb_msg.metadata = mt_data.text
        break

    imagehandler.download(emb_msg.url, emb_msg.title)

    return emb_msg

