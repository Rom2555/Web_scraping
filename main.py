# https://habr.com/ru/articles/

import requests
import bs4
import json


response = requests.get('https://habr.com/ru/articles/')
soup = bs4.BeautifulSoup(response.text, features='lxml')
#print(soup)

articles = soup.select('article.tm-articles-list__item')
print(articles)

# parsed_data = []
# for article in articles_list:
#     if article.select_one('span.post__title-label'):
#         title = article.select_one('span.post__title-text').text.strip()
#         link = article.select_one('a.post__title_link')['href']
#         time = article.select_one('span.post__time').text.strip()
#         text = article.select_one('div.post__text').text.strip()
#
#         parsed_data.append({title, link, time, text,})
#
# print(parsed_data)

#

#articles_block = soup.select('div.tm-articles-list')


#articles_list = articles_block.select_one('tm-articles-list__item')
#print(articles_block)
#
# parsed_data = []
# for article in articles_list:
#     content_title = article.select_one('div.content-title')
#     link = 'https://dtf.ru' + content_title.select_one('a[data-router-link]')['href']
#
#     response = requests.get(link)
#     article_soup = bs4.BeautifulSoup(response.text, features='lxml')
#     title = article_soup.select_one('h1').text.strip()
#     time = article.select_one('time')['datetime']
#     text = article_soup.select_one('article.content__blocks').text.strip()
#
#     parsed_data.append({
#         'title': title,
#         'link': link,
#         'time': time,
#         'text': text,
#     })
#
# with open('articles.json', 'w', encoding='utf-8') as f:
#     json.dump(parsed_data, f, ensure_ascii=False, indent=2)
