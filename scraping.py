from bs4 import BeautifulSoup
import requests

source = requests.get(HistoryOfFight.html).text

soup = BeautifulSoup(source, 'html.parser')

hey = soup.find('article')

headline  = hey.td.text

print(headline.prettify())

