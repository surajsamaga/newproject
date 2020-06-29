import requests
from bs4 import BeautifulSoup


def getdata(url):

    data = requests.get(url)
    soup = BeautifulSoup(data.text, 'html.parser')

    for div in soup.find_all('div', {"class": "image_container"}):
        for a in div.find_all('a'):
            for img in a.find_all('img'):
                print(img['alt'])
