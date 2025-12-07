# https://habr.com/ru/articles/817555/
# http://jursite.garant.ru/legal-issues/big-data-and-intellectual-property-a-systematic-study-of-scraping-as-part-of-a-common-internet-law-methodology
# https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/python/tests/actions_api/test_wheel.py#L11-L14
# https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk//examples/python/tests/actions_api/test_mouse.py#L24-L27
# https://iqss.github.io/dss-webscrape/filling-in-web-forms.html
# https://stepik.org/course/575/syllabus


# pip install requests
# pip install beautifulsoup4
# pip install lxml
# pip install fake_headers
# pip install selenium
# pip install webdriver-manager




import requests
import bs4

response = requests.get('https://www.iplocation.net/')
# with open('index.html', 'w') as f:
#     f.write(response.text)


soup = bs4.BeautifulSoup(response.text, features='lxml')
ip_span = soup.find('span', attrs={'class': 'table-ip4-home'})
print(ip_span.text.strip())
ip_span = soup.find_all('span', attrs={'class': 'table-ip4-home'})
print(ip_span[0].text.strip())
ip_span = soup.find('span', class_='table-ip4-home')
print(ip_span.text.strip())


span_ip = soup.select_one('span.table-ip4-home')
print(span_ip.text.strip())


#
# from fake_headers import Headers
#
# url = 'https://hh.ru/'
# headers = Headers(browser='chrome', os='mac').generate()
# response = requests.get(url, headers=headers)
# print(response.request.headers)
# with open('index.html', 'w', encoding='utf-8') as f:
#     f.write(response.text)







# ```
# <!DOCTYPE html>
# <html lang="ru">
#   <head>
#     <meta charset="UTF-8">
#     <title>Пример</title>
#   </head>
#   <body>
#     <h1 id="main-title">Заголовок</h1>
#     <p class="intro">Абзац с <a href="/about">ссылкой</a>.</p>
#     <img src="/img/logo.png" alt="Логотип">
#   </body>
# </html>
# ```


