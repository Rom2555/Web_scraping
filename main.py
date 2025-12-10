

import requests
import bs4
import json

from fake_headers import Headers

URL = "https://habr.com/ru/articles/"
PART_URL = "https://habr.com/ru"
## Определяем список ключевых слов:
KEYWORDS = ['дизайн', 'фото', 'web', 'python']
headers = Headers(browser='chrome', os='win').generate()

try:
    response = requests.get(URL, headers=headers)
    response.raise_for_status()
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all('article', class_='tm-articles-list__item')
except requests.exceptions.HTTPError as er:
    print(f"Ошибка HTTP: {er}")
    exit(1)
except Exception as e:
    print(f"Ошибка: {e}")
    exit(1)

parsed_data = []
for article in articles:
    try:
        # Название статьи
        title_tag = article.find('h2')
        title = title_tag.get_text(strip=True) if title_tag else "Без названия"

        # Ссылка
        link_tag = article.find('a', class_='tm-title__link')
        link = link_tag['href'] if link_tag else ""
        if link.startswith('/'):
            link = PART_URL + link

        # Время
        time_tag = article.find('time', {'datetime': True})
        time = time_tag['datetime'] if time_tag else ""

        # Текст статьи
        snippet_tag = article.find('div', class_='article-formatted-body')
        # print(snippet_tag)
        #snippet = snippet_tag.get_text(strip=True) if snippet_tag else ""
        p_tags = snippet_tag.find_all('p')
        print(p_tags)
        if p_tags:
            article_text = ' '.join(p.get_text(strip=True).lower() for p in p_tags)

            # Проверяем, есть ли хотя бы одно ключевое слово в тексте
            match_found = any(keyword.lower() in article_text.lower() for keyword in KEYWORDS)
            print(match_found)
            if match_found:
                parsed_data.append({
                    'title': title,
                    'link': link,
                    'time': time
                })
    except Exception as e:
        print(f"Ошибка при парсинге: {e}")

print(f"Найдено {len(parsed_data)} статей с ключевыми словами: {KEYWORDS}")

# Сохранение в JSON
with open('articles.json', 'w', encoding='utf-8') as f:
    json.dump(parsed_data, f, ensure_ascii=False, indent=4)

print("Парсинг завершён. Данные сохранены в articles.json")
