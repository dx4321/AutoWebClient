import condition as condition

from Settings.AuthData import *
from Settings.InputMask import *
from Settings.Locators import *
from Settings.DriverSettings import *

import time


# - функция ввода логина
def type_login():
    get_element_id(LoginPageLocators.login).clear()
    get_element_id(LoginPageLocators.login).send_keys(login_default)


# - функция ввода пароля
def type_password():
    get_element_id(LoginPageLocators.password).clear()
    get_element_id(LoginPageLocators.password).send_keys(password_default)


# - вход
def sign_in():
    get_element_id(LoginPageLocators.sing_in).click()


# - проверка корректной авторизации оператора "Администратор"
def verification():
    wait_presence_element_xpath(LoginPageLocators.role)
    user_role = get_element_xpath(LoginPageLocators.role).text

    if user_role == "Администратор":
        pass

    else:
        print(Exception("Провал тест-кейса на проверке оператора."))


# - функция нажатия на корень "Устройства"
def device_tree_click():
    get_element_xpath(SelectLocators.select_device_tree).click()


# - ЗАПАСНОЙ ВАРИАНТ. Функция нажатия на кнопку "Добавить" в дереве устройств.
def device_tree_button_add():
    get_element_xpath(ChannelsLocators.add_device_tree).click()
    time.sleep(1)
    get_element_xpath(ChannelsLocators.check_modal)
    time.sleep(1)


# - кликаем по любому элементу
def click_element(element):
    get_element_xpath(element).click()


# - функция, которая нажимает на кнопку "Добавить" и добавляем каналы связи
def add_channels(channel, confirm, label_channel: str):
    get_element_xpath(SelectLocators.select_device_tree).click()
    get_element_xpath(ChannelsLocators.add_device_tree).click()
    wait_presence_element_xpath(ChannelsLocators.check_modal)
    get_element_xpath(channel).click()
    get_element_xpath(ChannelsLocators.add_button_modal).click()
    wait_presence_element_xpath(confirm)
    confirm = get_element_xpath(confirm).text

    if confirm == label_channel:
        print("Канал успешно создан")

    else:
        Exception("Провал тест-кейса на добавлении канала связи")


# - функция нажатия на канал связи и добавления к нему ОДНОГО интерфейса
def add_interface(channel):
    get_element_xpath(channel).click()
    get_element_xpath(ChannelsLocators.add_device_tree).click()
    wait_presence_element_xpath(ChannelsLocators.check_modal)
    get_element_xpath(ChannelsLocators.add_button_modal).click()


# - функция нажатия на канал связи и добавления к нему всех интерфейсов
def add_interfaces(channel):
    i = 1
    get_element_xpath(channel).click()
    get_element_xpath(ChannelsLocators.add_device_tree).click()
    wait_presence_element_xpath(ChannelsLocators.check_modal)
    select_list = select_element_id(InterfacesLocators.add_list)
    get_list = get_element_id(InterfacesLocators.add_list).text
    format_list = get_list.split("\n")
    interfaces = len(format_list)
    get_element_xpath(ChannelsLocators.add_button_modal).click()

    # - цикл добавления интерфейсов на канал связи по списку
    while i < interfaces:
        time.sleep(1)
        get_element_xpath(channel).click()
        get_element_xpath(ChannelsLocators.add_device_tree).click()
        wait_presence_element_xpath(ChannelsLocators.check_modal)
        select_list.select_by_index(i)
        get_element_xpath(ChannelsLocators.add_button_modal).click()
        wait_invisible_element_xpath(ChannelsLocators.check_modal)
        i = i + 1
    return

    # - функция нажатия на интерфейс и добавления к нему всех счётчиков


# - функция нажатия на интерфейс и добавления к нему всех доступных счётчиков
def add_counters(interface):
    i = 1
    time.sleep(0.5)
    get_element_xpath(interface).click()
    get_element_xpath(ChannelsLocators.add_device_tree).click()
    wait_presence_element_xpath(ChannelsLocators.check_modal)
    select_list = select_element_id(InterfacesLocators.add_list)
    get_list = get_element_id(InterfacesLocators.add_list).text
    format_list = get_list.split("\n")
    counters = len(format_list)
    get_element_xpath(ChannelsLocators.add_button_modal).click()
    time.sleep(1)

    # - цикл добавления всех счётчиков на интерфейс по списку
    while i < counters:
        time.sleep(0.5)
        get_element_xpath(interface).click()
        get_element_xpath(ChannelsLocators.add_device_tree).click()
        wait_presence_element_xpath(ChannelsLocators.check_modal)
        select_list.select_by_index(i)
        get_element_xpath(ChannelsLocators.add_button_modal).click()
        wait_invisible_element_xpath(ChannelsLocators.check_modal)
        i = i + 1
    return


# - легендарная функция, которая добавляет все интерфейсы и счётчики на них
def add_objects_circle(interface_group):
    time.sleep(1)
    get_list = get_element_xpath(interface_group).text
    format_list_interfaces = get_list.split("\n")
    time.sleep(1)

    for interface in format_list_interfaces:
        time.sleep(1)
        xpath_interface = "//a[contains(text(),'" + interface + "')]"
        time.sleep(0.5)
        click_element(xpath_interface)
        time.sleep(0.5)
        get_element_xpath(ChannelsLocators.add_device_tree).click()
        wait_presence_element_xpath(ChannelsLocators.check_modal)
        select_list_devices = select_element_id(InterfacesLocators.add_list)
        get_list_devices = get_element_id(InterfacesLocators.add_list).text
        format_list_devices = get_list_devices.split("\n")
        counters = len(format_list_devices)
        get_element_xpath(ChannelsLocators.add_button_modal).click()
        time.sleep(1)
        check_window = wait_invisible_element_xpath(ChannelsLocators.check_modal_attention)
        start_count = True
        if check_window == start_count:
            count = 1
            while count < counters:
                time.sleep(0.5)
                get_element_xpath(ChannelsLocators.add_device_tree).click()
                wait_presence_element_xpath(ChannelsLocators.check_modal)
                select_list_devices.select_by_index(count)
                get_element_xpath(ChannelsLocators.add_button_modal).click()
                wait_invisible_element_xpath(ChannelsLocators.check_modal)
                count += 1
        else:
            time.sleep(0.5)
            get_element_id(ChannelsLocators.modal_ok).click()


# - функция выбора корня дерева "Абоненты"
def users_tree_click():
    get_element_xpath(SelectLocators.select_users_tree).click()
    time.sleep(1)


# - ЗАПАСНОЙ ВАРИАНТ. Функция нажатия на кнопку "Добавить" в дереве абонентов.
def users_tree_button_add():
    get_element_xpath(UsersLocators.add_users_tree).click()
    time.sleep(1)
    get_element_xpath(ChannelsLocators.check_modal)

    # - функция добавления дома/УК


def add_homes(homes, confirm, label_homes: str):
    get_element_xpath(UsersLocators.add_users_tree).click()
    time.sleep(1)
    get_element_xpath(ChannelsLocators.check_modal)
    get_element_xpath(homes).click()
    get_element_xpath(ChannelsLocators.add_button_modal).click()
    wait_presence_element_xpath(confirm)
    confirm = get_element_xpath(confirm).text

    if confirm == label_homes:
        print("Здание/УК успешно создано")

    else:
        Exception("Провал тест-кейса на добавлении абонентов")

    # - универсальная функция перетаскивания объектов в деревьях


def drag_to_tree(first_tree, second_tree, dragging_element, target_element):
    get_element_xpath(first_tree).click()
    time.sleep(1)
    get_element_xpath(second_tree).click()
    time.sleep(1)
    start = get_element_xpath(dragging_element)
    finish = get_element_xpath(target_element)
    time.sleep(1)
    DriverSettings.action_element(start, finish)
    time.sleep(1)


def change_properties(channel):
    get_element_xpath(channel).click()
    time.sleep(1)
    name_channel = get_element_xpath(channel).text
    name_property = get_element_xpath(PropertiesLocators.load_property).text
    if name_channel == name_property:
        pass

    else:
        Exception("Провал тест-кейса проверке имени канала связи и свойств")

    get_element_xpath(PropertiesLocators.activity_yes).click()
    get_element_id(PropertiesLocators.property_2).clear()
    get_element_id(PropertiesLocators.property_2).send_keys("с2000-Эзернет")
    get_element_id(PropertiesLocators.property_5).clear()
    get_element_id(PropertiesLocators.property_5).send_keys("999999")
    get_element_xpath(PropertiesLocators.working_mode_safe).click()
    get_element_id(PropertiesLocators.property_7).clear()
    get_element_id(PropertiesLocators.property_7).send_keys("1")
    get_element_id(PropertiesLocators.property_14).send_keys("Проверка комментария/Check comment/123456@#$$^&")
    get_element_id(PropertiesLocators.save).click()
    time.sleep(2)


def property_cycling(properties):
    property_list = get_element_id(properties).text
    select_property = select_element_id(properties)
    format_list = property_list.split("\n")
    property_name = len(format_list)

    index = 0
    while index < property_name:
        time.sleep(0.1)
        select_property.select_by_index(index)
        get_element_id(PropertiesLocators.save).click()
        wait_presence_element_xpath(CheckingToastMessage.toast_success_update)
        index += 1


def changing_magic_properties(interface):
    time.sleep(1)
    get_element_xpath(interface).click()
    time.sleep(1)
    name_interface = get_element_xpath(interface).text
    name_property = get_element_xpath(PropertiesLocators.load_property).text

    if name_interface == name_property:
        pass

    else:
        Exception("Провал тест-кейса проверке имени канала связи и свойств")

    get_element_xpath(PropertiesLocators.activity_yes).click()

    def property_cycl(properties):
        property_list = get_element_xpath(properties).text
        select_property = select_element_xpath(properties)
        format_list = property_list.split("\n")
        property_name = len(format_list)

        index = 0
        while index < property_name:
            time.sleep(0.1)
            select_property.select_by_index(index)
            get_element_id(PropertiesLocators.save).click()
            wait_presence_element_xpath(CheckingToastMessage.toast_success_update)
            index += 1

    property_cycl(PropertiesLocators.port_speed_list)
    property_cycl(PropertiesLocators.pause_commands_list)
    property_cycl(PropertiesLocators.timeout_magic_list)
    property_cycl(PropertiesLocators.delay_devices_list)
