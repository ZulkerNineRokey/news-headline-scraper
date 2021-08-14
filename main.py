import requests
from bs4 import BeautifulSoup
import json


def print_headlines(response_text):
    soup = BeautifulSoup(response_text, 'lxml')
    headlines = soup.find_all(attrs={"class": "newsHeadline-m__title-link__1puEG"})
    for headline in headlines:
        print(headline.text)

url = 'https://prothomalo.com/'
response = requests.get(url)
print_headlines(response.text)



