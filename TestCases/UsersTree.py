from Settings.Functions import *
from Settings.DriverSettings import *
import time

from Settings.Locators import *

driver.get(url="http://127.0.0.1:88/")
wait_presence_element_id(LoginPageLocators.connection)

try:
    type_login()
    type_password()
    sign_in()
    verification()
    users_tree_click()

    # - начинаем добавление в дерево "Абоненты"
    add_homes(UsersLocators.add_management_company, UsersLocators.in_tree_management_company, "Управляющая компания_01")
    get_element_xpath(UsersLocators.in_tree_management_company).click()
    get_element_xpath(UsersLocators.add_users_tree).click()
    wait_presence_element_xpath(ChannelsLocators.check_modal)
    get_element_xpath(UsersLocators.add_house).click()
    get_element_xpath(ChannelsLocators.add_button_modal).click()
    wait_presence_element_xpath(UsersLocators.in_tree_house)
    get_element_xpath(UsersLocators.in_tree_house).click()

    time.sleep(2)



finally:

    driver.close()
    driver.quit()