class LoginPageLocators:
    login: str = "username"
    password: str = "password"
    sing_in: str = "signIn"
    connection: str = "connection-successful"
    role: str = "//span[@class='label label-default ng-binding']"


class SelectLocators:
    select_device_tree: str = "//a[@class='jstree-anchor']"  # - кликаем по корню "Устройства" дерева устройств
    select_users_tree: str = "/html/body/div[2]/div/div/div/div[2]/div[3]/resurs-tree/div/div[2]/div/ul/li/a"


class CheckingToastMessage:
    toast_wait: str = "//div[contains(@class, 'toast-wait')]"

    toast_success: str = "//div[contains(@class, 'toast-success')]"
    toast_success_loading: str = "//div[contains(@class, 'toast-success')]//div[text() = 'Загрузка данных завершена']"
    toast_success_update: str = "//div[contains(@class, 'toast-success')]//div[text() = 'Данные обновлены']"

    toast_error: str = "//div[contains(@class, 'toast-error')]"

    toast_info_common: str = "//div[contains(@class, 'toast-info')]"
    toast_info_close_connection: str = "//div[contains(@class, 'toast-info')]//div[text() = 'Соединение закрыто']"


class ChannelsLocators:
    add_device_tree: str = "//resurs-tree[@tree='device']//button[@title='Добавить']"  # - нажимаем на кнопку "Добавить" в дереве устройств
    check_modal: str = "//div[@class='modal fade in']//div[@class='modal-header']//h4[contains(@class, 'modal-title')]"  # - проверка на открытие модального окна "Добавить устройство" и "Добавить абонента"
    check_modal_attention: str = "//div[contains(@class, 'col-lg-12 white-space-pre-line ng-binding') and text() = 'Устройства могут быть добавлены только через поиск!']"
    add_button_modal: str = "//div[@id='page-wrapper']//div[@class='modal-footer']//button[@class='btn btn-primary']"  # - нажимаем на кнопку "ОК" в модальном окне "Добавить устройство" и "Добавить абонента"
    add_c2000ethernet: str = "//option[@value='TC2000EthernetChannel']"  # - выбираем в модальном окне канал связи "С2000-Ethernet"
    add_comport: str = "//option[@value='TCOMChannel']"  # - выбираем в модальном окне канал связи "СОМ-порт"
    add_csdresursgsm: str = "//option[@value='TTelemetriy_CSD_Channel']"  # - выбираем в модальном окне канал связи "CSD Ресурс-GSM"
    add_gprsresursgsm: str = "//option[@value='TTelemetriy_GPRS_Channel']"  # - выбираем в модальном окне канал связи "GPRS Ресурс-GSM"
    add_soketclient: str = "//option[@value='TSocketClientChannel']"  # - выбираем в модальном окне канал связи "Soket Client"
    add_soketserver: str = "//option[@value='TSocketServerChannel']"  # - выбираем в модальном окне канал связи "Soket Server"
    add_techem: str = "//option[@value='TTechemChannel']"  # - выбираем в модальном окне канал связи "Techem"
    add_virtualcomport: str = "//option[@value='TVirtualCOMChannel']"  # - выбираем в модальном окне канал связи "Виртуальный СОМ-порт"
    in_tree_c2000ethernet: str = "/html/body/div[2]/div/div/div/div[2]/div[1]/resurs-tree/div/div[2]/div/ul/li/ul/li/a"  # - проверяем в дереве устройств добавление канала связи
    in_tree_comport: str = "//resurs-tree[@tree='device']//li[contains(@class, 'jstree-node')]//a[contains(@class, 'jstree-anchor') and text() = 'COM-порт']"  # - проверяем в дереве устройств добавление канала связи
    in_tree_csdresursgsm: str = "//resurs-tree[@tree='device']//li[contains(@class, 'jstree-node')]//a[contains(@class, 'jstree-anchor') and text() = '[CSD] Ресурс-GSM Модем']"  # - проверяем в дереве устройств добавление канала связи
    in_tree_gprsresursgsm: str = "//resurs-tree[@tree='device']//li[contains(@class, 'jstree-node')]//a[contains(@class, 'jstree-anchor') and text() = '[GPRS] Ресурс-GSM Интернет']"  # - проверяем в дереве устройств добавление канала связи
    in_tree_soketclient: str = "//resurs-tree[@tree='device']//li[contains(@class, 'jstree-node')]//a[contains(@class, 'jstree-anchor') and text() = '[Ethernet] Socket Client']"  # - проверяем в дереве устройств добавление канала связи
    in_tree_soketserver: str = "//resurs-tree[@tree='device']//li[contains(@class, 'jstree-node')]//a[contains(@class, 'jstree-anchor') and text() = '[Ethernet] Socket Server (TELEOFIS)']"  # - проверяем в дереве устройств добавление канала связи
    in_tree_techem: str = "//resurs-tree[@tree='device']//li[contains(@class, 'jstree-node')]//a[contains(@class, 'jstree-anchor') and text() = '[Internet] Techem']"  # - проверяем в дереве устройств добавление канала связи
    in_tree_virtualcomport: str = "//resurs-tree[@tree='device']//li[contains(@class, 'jstree-node')]//a[contains(@class, 'jstree-anchor') and text() = 'Виртуальный COM-порт']"  # - проверяем в дереве устройств добавление канала связи
    modal_ok: str = "OK"


# noinspection SpellCheckingInspection
class InterfacesLocators:
    add_list: str = "create-modal-select-list"  # - путь к выпадающему списку в модальном окне
    in_tree_group_interfaces: str = "/html/body/div[2]/div/div/div/div[2]/div[1]/resurs-tree/div/div[2]/div/ul/li/ul/li/ul"  # - xpath к группе объектов в дереве Устройств
    in_tree_interface_meter_bus: str = "//a[contains(text(),'[MBus] Счётчики Meter-Bus')]"  # - путь к интерфейсу в дереве (оставил для примера)


class UsersLocators:
    add_users_tree: str = "/html/body/div[2]/div/div/div/div[2]/div[3]/resurs-tree/div/div[1]/resurs-tree-panel/button[2]"
    add_house: str = "/html/body/div[2]/div/resurs-create-modal/div/div/div/div[2]/ng-include/div/div/div/div/form/select/option[1]"
    add_management_company: str = "/html/body/div[2]/div/resurs-create-modal/div/div/div/div[2]/ng-include/div/div/div/div/form/select/option[2]"
    add_apartment: str = "/html/body/div[2]/div/resurs-create-modal/div/div/div/div[2]/ng-include/div/div/div/div/form/select/option[1]"
    add_entrance: str = "/html/body/div[2]/div/resurs-create-modal/div/div/div/div[2]/ng-include/div/div/div/div/form/select/option[2]"
    add_single_user: str = "/html/body/div[2]/div/resurs-create-modal/div/div/div/div[2]/ng-include/div/div/div/div/form/select/option[1]"
    add_multi_user: str = "/html/body/div[2]/div/resurs-create-modal/div/div/div/div[2]/ng-include/div/div/div/div/form/select/option[2]"
    add_multi_account: str = "/html/body/div[2]/div/resurs-create-modal/div/div/div/div[2]/ng-include/div/div/div/div/form/select/option"
    in_tree_management_company: str = "/html/body/div[2]/div/div/div/div[2]/div[3]/resurs-tree/div/div[2]/div/ul/li/ul/li/a"
    in_tree_house: str = "/html/body/div[2]/div/div/div/div[2]/div[3]/resurs-tree/div/div[2]/div/ul/li/ul/li/ul/li/a"
    in_tree_apartment: str = "/html/body/div[2]/div/div/div/div[2]/div[3]/resurs-tree/div/div[2]/div/ul/li/ul/li[1]/ul/li/a"
    in_tree_entrance: str = "/html/body/div[2]/div/div/div/div[2]/div[3]/resurs-tree/div/div[2]/div/ul/li/ul/li[1]/ul/li[2]/a"
    in_tree_single_user: str = "/html/body/div[2]/div/div/div/div[2]/div[3]/resurs-tree/div/div[2]/div/ul/li/ul/li[1]/ul/li/ul/li[1]/a"
    in_tree_multi_user: str = "/html/body/div[2]/div/div/div/div[2]/div[3]/resurs-tree/div/div[2]/div/ul/li/ul/li[1]/ul/li[1]/ul/li[2]/a"
    in_tree_multi_account: str = "/html/body/div[2]/div/div/div/div[2]/div[3]/resurs-tree/div/div[2]/div/ul/li/ul/li[1]/ul/li[1]/ul/li[2]/ul/li/a"


class PropertiesLocators:
    property_manager: str = "//div[@class='panel-body panel-scroll form-props']"
    load_property: str = "//span[@class='title ng-binding' and text()]"
    identification: str = "field_Идентификатор"
    save: str = "property-manager-save-button"
    save_v2: str = "//button[contains(@id, 'property-manager-save-button') and text() = ' Сохранить']"
    property_1: str = "field_1"
    property_2: str = "field_2"
    property_3: str = "field_3"
    property_4: str = "field_4"
    property_5: str = "field_5"
    property_6: str = "field_6"
    property_7: str = "field_7"
    property_8: str = "field_8"
    property_9: str = "field_9"
    property_10: str = "field_10"
    property_11: str = "field_11"
    property_12: str = "field_12"
    property_13: str = "field_13"
    property_14: str = "field_14"
    compatibility_yes: str = "//resurs-props//div[contains(@class, 'panel-resurs-props')]//label[text() = 'Совместимость с Карат-911']/following-sibling::select//option[@value='boolean:true']"
    compatibility_no: str = "//resurs-props//div[contains(@class, 'panel-resurs-props')]//label[text() = 'Совместимость с Карат-911']/following-sibling::select//option[@value='boolean:false']"
    control_parity_list: str = "//resurs-props//div[contains(@class, 'panel-resurs-props')]//label[text() = 'Контроль чётности']/following-sibling::select"
    activity_yes: str = "//resurs-props//div[contains(@class, 'panel-resurs-props')]//label[text() = 'Активность']/following-sibling::select//option[@value='boolean:true']"
    activity_no: str = "//resurs-props//div[contains(@class, 'panel-resurs-props')]//label[text() = 'Активность']/following-sibling::select//option[@value='boolean:false']"
    working_mode_fast: str = "//resurs-props//div[contains(@class, 'panel-resurs-props')]//label[text() = 'Режим работы']/following-sibling::select//option[@value='string:Быстрый']"
    working_mode_safe: str = "//resurs-props//div[contains(@class, 'panel-resurs-props')]//label[text() = 'Режим работы']/following-sibling::select//option[@value='string:Надёжный']"
    port_speed_list: str = "//resurs-props//div[contains(@class, 'panel-resurs-props')]//label[text() = 'Скорость порта']/following-sibling::select"
    port_speed_300: str = "//resurs-props//div[contains(@class, 'panel-resurs-props')]//label[text() = 'Скорость порта']/following-sibling::select//option[@value='string:300']"
    timeout_list: str = "//resurs-props//div[contains(@class, 'panel-resurs-props')]//label[text() = 'Таймаут, мсек']/following-sibling::select"
    delay_commands_list: str = "//resurs-props//div[contains(@class, 'panel-resurs-props')]//label[text() = 'Задержка между командами, мсек']/following-sibling::select"
    pause_commands_list: str = "//resurs-props//div[contains(@class, 'panel-resurs-props')]//label[text() = 'Пауза между командами, мсек']/following-sibling::select"
    timeout_magic_list: str = "//resurs-props//div[contains(@class, 'panel-resurs-props')]//label[text() = 'Тайм-аут чтения, мсек']/following-sibling::select"
    delay_devices_list: str = "//resurs-props//div[contains(@class, 'panel-resurs-props')]//label[text() = 'Задержка между счётчиками, мсек']/following-sibling::select"


class TeamCityLocators:
    ArmResurs: str = '/html/body/div[1]/div[6]/div/div/div/div[1]/div[1]/div/div[2]/div/div[1]/div/div/div[7]/div/div/a/span/div/span[2]'
    ArmResursInstall10: str = '/html/body/div[1]/div[6]/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/div[6]/div[1]/div/div/div/div/span/a/span[2]'
    Work: str = '/html/body/div[1]/div[6]/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div[1]/h3/div[1]/a/span[2]'
    branch_master: str = '/html/body/div[1]/div[6]/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/div[3]/div/div/div[1]/div/div[1]/a/span/span/span[1]'
    LastBuild: str = "//div[@class='BuildDetails__build--3a']"
    Artifacts: str = "//div[@class='refreshable']//a[contains(@title, 'View Artifacts')]"
    ArmResursExe: str = '/html/body/div[1]/div[6]/div/div[3]/div/div/div/div/div/ul/li[1]/a'