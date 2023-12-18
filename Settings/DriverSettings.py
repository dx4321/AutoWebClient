#pip install --proxy http://login:password@proxy.bolid.ru:3128   - использовать для установки библиотек

from selenium import webdriver
from allure import step
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException


"""
настройки драйвера
"""

# options позволяет задать настройки для браузера с которым мы работаем
options = webdriver.ChromeOptions()
# options.headless = True  # - пример скрытия браузера №2

options.add_argument("--start-maximized")

driver: WebDriver = webdriver.Chrome(
    executable_path="\\chromedriver\\chromedriver.exe", options=options)

"""
функции ЯВНОГО ожидания появления элемента в DOM
"""


def wait_presence_element_xpath(locator):
    try:
        WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, locator)))
    except TimeoutException:
        return False
    return True


def wait_presence_element_id(locator):
    try:
        WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, locator)))
    except TimeoutException:
        return False
    return True


def wait_visible_element_xpath(locator):
    try:
        WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, locator)))
    except TimeoutException:
        return False
    return True


def wait_visible_element_id(locator):
    try:
        WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.ID, locator)))
    except TimeoutException:
        return False
    return True


def wait_invisible_element_xpath(locator):
    try:
        WebDriverWait(driver, 2).until(EC.invisibility_of_element_located((By.XPATH, locator)))
    except TimeoutException:
        return False
    return True


def wait_invisible_element_id(locator):
    try:
        WebDriverWait(driver, 2).until(EC.invisibility_of_element_located((By.ID, locator)))
    except TimeoutException:
        return False
    return True


"""
функция перетаскивания элементов с паузой (без паузы закомментировано)
"""


def action_element(source, target):
    return ActionChains(driver).click_and_hold(source).move_to_element(target).pause(2).release(target).perform()


# action.drag_and_drop(source, target).perform()   -  альтернативный вариант использования, если нужно перетащить без паузы


"""
функция открытия контекстного меню у web элементов
"""


def right_click(element):
    return ActionChains(driver).context_click(element).perform()


"""
функция выбора элемента
"""


def select_element_xpath(locator: str):
    return Select(driver.find_element(By.XPATH, locator))


def select_element_id(locator: str):
    return Select(driver.find_element(By.ID, locator))


"""
функции получения элементов из DOM-дерева по ID и xpath
"""


# функция get_element_xpath тоже самое, что и driver.find_element(By.XPATH, "ваш_xpath"), только короче. Актуально для других локаторов ниже
def get_element_xpath(locator: str):
    return driver.find_element(By.XPATH, locator)


def get_element_id(locator: str):
    return driver.find_element(By.ID, locator)


def get_element_link_text(locator):
    return driver.find_element(By.LINK_TEXT, locator)


def get_element_partial_link_text(locator):
    return driver.find_element(By.PARTIAL_LINK_TEXT, locator)


"""
функции получения нескольких элементов из DOM-дерева по разным локаторам
"""


# получение нескольких элементов по разным локаторам
def get_elements_xpath(locator: str):
    return driver.find_elements(By.XPATH, locator)


def get_elements_id(locator: str):
    return driver.find_elements(By.ID, locator)


def get_elements_name(locator: str):
    return driver.find_elements(By.NAME, locator)


def get_elements_class_name(locator: str):
    return driver.find_elements(By.CLASS_NAME, locator)


def get_elements_tag_name(locator: str):
    return driver.find_elements(By.TAG_NAME, locator)


def get_elements_link_text(locator: str):
    return driver.find_elements(By.LINK_TEXT, locator)