# https://habr.com/ru/articles/
from pprint import pprint
import requests
import bs4
import json

## Определяем список ключевых слов:
KEYWORDS = ['дизайн', 'фото', 'web', 'python']

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.5'
}

response = requests.get('https://habr.com/ru/articles/', headers=headers)
response.raise_for_status()

soup = bs4.BeautifulSoup(response.text, 'html.parser')

articles = soup.find_all('article', class_='tm-articles-list__item')

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
            link = 'https://habr.com' + link

        # ⬇️ Время: ищем тег <time> внутри нужного контейнера
        time_tag = article.find('time', {'datetime': True})
        time = time_tag['datetime'] if time_tag else ""

        p_tags = article.find_all('p')
        article_text = ' '.join(p.get_text(strip=True).lower() for p in p_tags)

        # Проверяем, есть ли хотя бы одно ключевое слово в тексте
        match_found = any(keyword.lower() in article_text for keyword in KEYWORDS)

        if match_found:
            parsed_data.append({
                'title': title,
                'link': link,
                'time': time
            })
            print(f"Найдено: {title} - {link}")

    except Exception as e:
        print(f"Ошибка при парсинге: {e}")

# Сохранение в JSON
with open('articles.json', 'w', encoding='utf-8') as f:
    json.dump(parsed_data, f, ensure_ascii=False, indent=4)

print("Парсинг завершён. Данные сохранены в articles.json")
