import requests
import bs4
import json


response = requests.get('https://dtf.ru/games')
soup = bs4.BeautifulSoup(response.text, features='lxml')

articles_block = soup.select_one('div.content-list')
articles_list = articles_block.select('div.content--short')

parsed_data = []
for article in articles_list:
    content_title = article.select_one('div.content-title')
    link = 'https://dtf.ru' + content_title.select_one('a[data-router-link]')['href']

    response = requests.get(link)
    article_soup = bs4.BeautifulSoup(response.text, features='lxml')
    title = article_soup.select_one('h1').text.strip()
    time = article.select_one('time')['datetime']
    text = article_soup.select_one('article.content__blocks').text.strip()

    parsed_data.append({
        'title': title,
        'link': link,
        'time': time,
        'text': text,
    })

with open('articles.json', 'w', encoding='utf-8') as f:
    json.dump(parsed_data, f, ensure_ascii=False, indent=2)
