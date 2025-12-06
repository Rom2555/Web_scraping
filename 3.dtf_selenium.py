import json
from time import sleep

from selenium.common import TimeoutException
from selenium.webdriver import Chrome, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

chrome_path = ChromeDriverManager().install()
service = Service(executable_path=chrome_path)
browser = Chrome(service=service)


def wait_element(browser, delay=3, by=By.CSS_SELECTOR, value=None):
    try:
        return WebDriverWait(browser, delay).until(
            expected_conditions.presence_of_element_located((by, value))
        )
    except TimeoutException:
        return None


# response = requests.get('https://dtf.ru/games')
# soup = bs4.BeautifulSoup(response.text, features='lxml')
browser.get('https://dtf.ru/games')
sleep(5)


# # articles_block = soup.select_one('div.content-list')
# articles_block = browser.find_element(by=By.CSS_SELECTOR, value='div.content-list')
#
# # articles_list = articles_block.select('div.content--short')
# articles_list = articles_block.find_elements(by=By.CSS_SELECTOR, value='div.content--short')
#
# links = []
# for article in articles_list:
#     #     content_title = article.select_one('div.content-title')
#     content_title = wait_element(article, value='div.content-title')
#     #     link = 'https://dtf.ru' + content_title.select_one('a[data-router-link]')['href']
#     link = wait_element(content_title, value='a[data-router-link]').get_attribute('href')
#     links.append(link)
#
# parsed_data = []
# for link in links:
# #     response = requests.get(link)
# #     article_soup = bs4.BeautifulSoup(response.text, features='lxml')
#     browser.get(link)
#
# #     title = article_soup.select_one('h1').text.strip()
#     title = wait_element(browser, value='h1').text.strip()
# #     time = article.select_one('time')['datetime']
#     time = wait_element(browser, value='time').get_attribute('datetime')
# #     text = article_soup.select_one('article.content__blocks').text.strip()
#     text = wait_element(browser, value='article.content__blocks').text.strip()
#
#
#     parsed_data.append({
#         'title': title,
#         'link': link,
#         'time': time,
#         'text': text,
#     })
#
# with open('articles2.json', 'w') as f:
#     json.dump(parsed_data, f, ensure_ascii=False, indent=2)




search_button = wait_element(browser, value='button.quick-search-button')
search_button.click()
sleep(3)
search_field = wait_element(browser, value='input.text-input')
search_field.send_keys('World of warcraft')
sleep(3)
search_field.send_keys(Keys.ENTER)
sleep(10)