import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализируем драйвер
driver = webdriver.Chrome()

try:
    # Открываем страницу
    driver.get("https://stepik.org/lesson/25969/step/12")
    time.sleep(5)  # Даём время на начальную загрузку (можно заменить на WebDriverWait)

    # Ждём, пока поле ввода не станет доступным
    # Новый селектор: textarea или поле с placeholder "Напишите ваш ответ..."
    textarea = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "textarea.ember-text-area"))
    )
    print("Поле ввода найдено!")

    # Вводим текст
    textarea.send_keys("get()")

    # Ждём появление кнопки отправки и кликаем
    submit_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission"))
    )
    submit_button.click()
    print("Ответ отправлен!")

    # Ждём несколько секунд, чтобы увидеть результат
    time.sleep(10)

finally:
    # Закрываем браузер
    driver.quit()