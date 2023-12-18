from Settings.Functions import *
from Settings.DriverSettings import *
import time

from Settings.Locators import *

driver.get(url="http://")
wait_presence_element_id(LoginPageLocators.connection)

try:
    type_login()
    type_password()
    sign_in()
    verification()
    device_tree_click()

    # - начинаем добавление в дерево "Устройства"
    add_channels(ChannelsLocators.add_c2000ethernet, ChannelsLocators.in_tree_c2000ethernet, "C2000-Ethernet")
    add_interfaces(ChannelsLocators.in_tree_c2000ethernet)
    add_objects_circle(InterfacesLocators.in_tree_group_interfaces)

    # - переходим к проверке дерева абонентов
    # Users.users_tree_click()

    # Users.add_homes(UsersLocators.add_house, UsersLocators.in_tree_house, "Здание_01")
    # Users.add_homes(UsersLocators.add_management_company, UsersLocators.in_tree_management_company, "Управляющая компания_01")


finally:

    driver.close()
    driver.quit()