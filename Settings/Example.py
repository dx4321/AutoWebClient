from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from AuthData import login_default, password_default

import time
import random
import pickle

# options позволяет задать настройки для браузера с которым мы работаем
options = webdriver.ChromeOptions()

"""
#различные варианты для проверки  UserAgent
options.add_argument("user-agent=HelloWorld") - пример 1. можно самому присвоить свой юзер агент
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36")
options.add_argument(f"user-agent={useragent.random}") - пример 3. Юзерагент будет абсолютно рандомным и будет браться из библиотеки fake_useragent. Хороший пример, брать его для проверки.
"""

# отключение WebDriver mode для ChromeDriver после 79.0.3945
# options.add_argument("--disable-blink-features=AutomationControlled")   # - позволяет отключить обнаружение автоматизированного управления браузера, для работы необходима 12 и 24 строчки кода

# headless позволяет работать без визуального отображения браузера, что значительно экономит ресурсы ПК. Для визуального отображения необходимо отключить опцию
# options.add_argument("--headless")    # - пример скрытия браузера №1
##options.headless = True              # - пример скрытия браузера №2

driver: WebDriver = webdriver.Chrome(
    executable_path="C:\\AutoTests\\ResursWeb\\chromedriver\\chromedriver.exe")  # - для применения options необходимо дописать ", options=options)"

try:
    driver.get(url="http://127.0.0.1:88/")  # - говорим драйверу открыть указанную страницу
    # driver.get(url="https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")
    time.sleep(2)  # - засыпаем на 2 сек

    # ввод логина
    # username_input.send_keys("Администратор") - самый простой вариант. Зашиваем по жёсткому данные авторизации
    print("Проходим ввод логина...")
    username_input = driver.find_element(By.ID, "username")                                                                 # - находим элемент поля по ID
    username_input.clear()                                                                                                  # - очищаем его
    time.sleep(1)                                                                                                           # - засыпаем на 1 сек
    username_input.send_keys(login_default)                                                                             # - send_keys берёт переменную авторизации логина из модуля auth_data
    time.sleep(1)

    # ввод пароля
    # password_input.send_keys("123456") - самый простой вариант. Зашиваем по жёсткому данные авторизации
    print("Проходим ввод пароля...")
    password_input = driver.find_element(By.ID, "password")                                                                 # - находим элемент поля по ID
    password_input.clear()                                                                                                  # - очищаем его
    time.sleep(1)                                                                                                           # - засыпаем на 1 сек
    password_input.send_keys(password_default)                                                                            # - send_keys берёт переменную авторизации пароля из модуля auth_data
    time.sleep(1)

    # авторизация
    # password_input.send_keys(Keys.ENTER)   # - вариант авторизации по нажатию кнопки на клавиатуре Enter, можно использовать когда нет IDшника кнопки входа
    print("Входим в web-клиент...")
    login_button = driver.find_element(By.ID, "signIn")                                                                     # - находим кнопку входа по ID
    login_button.click()                                                                                                    # - нажимаем на неё
    time.sleep(3)                                                                                                           # - засыпаем на 5 сек
    print("Завершаем тест-кейс...")

    # проверка на корректность авторизации
    check_auth = driver.find_element(By.XPATH, "//span[@class='label label-default ng-binding']").text
    print("Найден оператор " + check_auth)

    if check_auth == "admin":
        print("Тест-кейс выполнен успешно.")

    else:
        print(Exception("Провал тест-кейса на проверке оператора."))

    # работа с куки
    # pickle.dump(driver.get_cookies(), open(f"{admin_default_log}_cookies", "wb"))   # - создаёт файл с именем, которое присваивается переменной admin_default_log в модуле auth_data
    # for cookie in pickle.load(open(f"{admin_default_log}_cookies", "rb")):   # - цикл for приказывает загрузить файл куки. В наших реалиях у меня не получилось выполнить.
    #     driver.add_cookie(cookie)

    # try:   # - метод проверки работы веб-драйвера. Для работы необходима настройка options (читать выше)
    #     driver.get(url="https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")  # - говорим драйверу открыть указанную страницу
    #     time.sleep(5)   # - засыпаем на 2 сек

except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()
