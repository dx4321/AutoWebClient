from Settings.Functions import *
from Settings.DriverSettings import *
import time

from Settings.Locators import *

driver.get(url="http://127.0.0.1:88/")
wait_presence_element_id(LoginPageLocators.connection)

try:
    LoginPage.type_login()
    LoginPage.type_password()
    LoginPage.sign_in()
    LoginPage.verification()

    # - начинаем проверку дерева устройств
    Channels.add_channels(ChannelsLocators.add_virtualcomport, ChannelsLocators.in_tree_virtualcomport, "Виртуальный COM-порт")
    # ChangePropertiesChannel.change_properties(ChannelsLocators.in_tree_virtualcomport)
    Interfaces.add_interfaces(ChannelsLocators.in_tree_virtualcomport)
    ChangePropertiesInterface.changing_magic_properties(InterfacesLocators.in_tree_interface_virt_betar)

    # InterfaceAlone.add_interface(ChannelsLocators.in_tree_c2000ethernet)

    # Channels.add_channels(ChannelsLocators.add_comport, ChannelsLocators.in_tree_comport, "COM-порт")
    # ChangePropertiesChannel.change_properties(ChannelsLocators.in_tree_comport)
    # Interfaces.add_interfaces(ChannelsLocators.in_tree_c2000ethernet)
    # Counters.add_counters(InterfacesLocators.in_tree_interface_meter_bus)
    # Dragging.drag_to_tree(UsersLocators.in_tree_apartment, CountersLocators.in_tree_counter_mbus_heatmeter, CountersLocators.in_tree_counter_mbus_heatmeter, UsersLocators.in_tree_single_user)
    # Testing.test_test()

    # - переходим к проверке дерева абонентов
    # Users.users_tree_click()

    # Users.add_homes(UsersLocators.add_house, UsersLocators.in_tree_house, "Здание_01")
    # Users.add_homes(UsersLocators.add_management_company, UsersLocators.in_tree_management_company, "Управляющая компания_01")

finally:

    driver.close()
    driver.quit()