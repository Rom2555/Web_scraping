from datetime import datetime

import requests
import bs4
import json
from fake_headers import Headers

# URL главной страницы:
URL = "https://habr.com/ru/articles/"
# URL части сайта:
PART_URL = "https://habr.com"
# Определяем список ключевых слов:
KEYWORDS = ["дизайн", "фото", "web", "python"]


def get_page_html(url):
    """Получает HTML-содержимое страницы."""
    headers = Headers(browser="chrome", os="win").generate()
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.text
    except requests.exceptions.HTTPError as e:
        print(f"Ошибка HTTP при запросе {url}: {e}")
    except Exception as e:
        print(f"Ошибка подключения к {url}: {e}")
    return None


def parse_articles(html):
    """Парсит статьи с главной страницы."""
    soup = bs4.BeautifulSoup(html, "html.parser")
    return soup.find_all("article", class_="tm-articles-list__item")


def extract_text_from_snippet(snippet_tag):
    """Извлекает и объединяет текст из тегов <p> или всего блока."""
    if not snippet_tag:
        return ""

    p_tags = snippet_tag.find_all("p")
    if p_tags:
        return " ".join(p.get_text(strip=True).lower() for p in p_tags)
    return snippet_tag.get_text(strip=True).lower()


def format_datetime(iso_time):
    """Преобразует ISO-строку времени в удобочитаемый формат."""
    try:
        dt = datetime.fromisoformat(iso_time.replace("Z", "+00:00"))
        return dt.strftime("%d.%m.%Y %H:%M")
    except Exception as e:
        print(f"Ошибка при форматировании даты-времени: {e}")
        return iso_time


def parse_article(article):
    """Обрабатывает одну статью и возвращает данные, если найдено ключевое слово."""
    try:
        # Название статьи
        title_tag = article.find("h2")
        title = title_tag.get_text(strip=True) if title_tag else "Без названия"

        # Ссылка
        link_tag = article.find("a", class_="tm-title__link")
        link = link_tag["href"] if link_tag else ""
        if link.startswith("/"):
            link = PART_URL + link

        # Время
        time_tag = article.find("time", {"datetime": True})
        iso_time = time_tag["datetime"] if time_tag else ""
        human_time = format_datetime(iso_time)

        # Текст статьи
        snippet_tag = article.find("div", class_="article-formatted-body")
        article_text = extract_text_from_snippet(snippet_tag)
        all_text = title.lower() + " " + article_text
        # Проверяем, есть ли хотя бы одно ключевое слово в тексте
        if any(keyword.lower() in all_text for keyword in KEYWORDS):
            return {"title": title, "link": link, "date_time": human_time}
    except Exception as e:
        print(f"Ошибка при парсинге статьи: {e}")
    return None


def save_to_json(data, filename="articles.json"):
    """Сохраняет данные в JSON-файл."""
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"Данные сохранены в {filename}")
    except Exception as e:
        print(f"Ошибка при записи в файл: {e}")


def main():
    """Основная функция."""
    html = get_page_html(URL)
    if not html:
        print("Не удалось получить страницу.")
        return

    articles = parse_articles(html)
    parsed_data = []

    for article in articles:
        result = parse_article(article)
        if result:
            parsed_data.append(result)

    print(f"Найдено {len(parsed_data)} статей с ключевыми словами: {KEYWORDS}")
    save_to_json(parsed_data)


if __name__ == "__main__":
    main()
