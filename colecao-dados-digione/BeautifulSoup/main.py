import requests
import json
from bs4 import BeautifulSoup

res = requests.get("https://digitalinnovation.one")
res.encoding = "utf-8"

#mostrando o código da requisição
print(res)

#transformar objetos de texto em objetos de HTML
soup = BeautifulSoup(res.text,'html.parser')
#print(soup)

#extraindo dados por meio de class html
cards = soup.find_all(class_="card card-course")
#print(cards)

all_cards = []
for card in cards:
    info = card.find(class_="card-body")
    title = info.find(class_="card-text").text
    legend = info.find(class_="legend").text
    img = info.find('img').attrs['src']
    all_cards.append({
        'title':title,
        'legend':legend,
        'img': img,
    })

#print(all_cards)
with open('cards.json','w') as json_file:
    json.dump(all_cards,json_file, indent=3, ensure_ascii=False)