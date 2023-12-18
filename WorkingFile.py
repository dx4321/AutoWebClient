from Settings.Functions import *
from Settings.DriverSettings import *
import time

from Settings.Locators import *

driver.get(url="http://127.0.0.1:88/")
wait_presence_element_id(LoginPageLocators.connection)


def main():
    try:
        type_login()
        type_password()
        sign_in()
        verification()

        # click_channel(ChannelsLocators.in_tree_c2000ethernet)
        #add_objects_circle(InterfacesLocators.in_tree_group_interfaces)
        time.sleep(10)
        change_properties(ChannelsLocators.in_tree_c2000ethernet)
        time.sleep(1)
        get_element_xpath(InterfacesLocators.in_tree_interface_meter_bus).click()
        name_interface = get_element_xpath(InterfacesLocators.in_tree_interface_meter_bus).text
        name_property = get_element_xpath(PropertiesLocators.load_property).text

        if name_interface == name_property:
            pass
        else:
            Exception("Провал тест-кейса проверке имени канала связи и свойств")

        get_element_xpath(PropertiesLocators.activity_yes).click()
        number = 3
        id_properties = "field_" + str(number)
        property_cycling(id_properties)
        number = 5
        id_properties = "field_" + str(number)
        property_cycling(id_properties)
        number = 6
        id_properties = "field_" + str(number)
        property_cycling(id_properties)
        number = 7
        id_properties = "field_" + str(number)
        property_cycling(id_properties)



        # add_channels(ChannelsLocators.add_c2000ethernet, ChannelsLocators.in_tree_c2000ethernet, "C2000-Ethernet")
        # add_interfaces(ChannelsLocators.in_tree_c2000ethernet)
    # InterfaceAlone.add_interface(ChannelsLocators.in_tree_c2000ethernet)
    # ChangePropertiesInterface.changing_native_properties(InterfacesLocators.in_tree_interface_meter_bus)
    # ChangePropertiesInterface.changing_magic_properties(InterfacesLocators.in_tree_interface_mercury200_plc)
    # ChangePropertiesInterface.changing_magic_properties(InterfacesLocators.in_tree_interface_mercury230_plc)
    # ChangePropertiesInterface.changing_magic_properties(InterfacesLocators.in_tree_interface_vkt9)
    # ChangePropertiesInterface.changing_magic_properties(InterfacesLocators.in_tree_interface_multical)
    # ChangePropertiesInterface.changing_magic_properties(InterfacesLocators.in_tree_interface_tmk)
    # ChangePropertiesInterface.changing_magic_properties(InterfacesLocators.in_tree_interface_teross)
    # ChangePropertiesInterface.changing_magic_properties(InterfacesLocators.in_tree_interface_karat_306)
    # ChangePropertiesInterface.changing_magic_properties(InterfacesLocators.in_tree_interface_karat_compact)
    # ChangePropertiesInterface.changing_magic_properties(InterfacesLocators.in_tree_interface_abb)
    # ChangePropertiesInterface.changing_magic_properties(InterfacesLocators.in_tree_interface_dfm_marine)
    # ChangePropertiesInterface.changing_magic_properties(InterfacesLocators.in_tree_interface_danfoss)
    # ChangePropertiesInterface.changing_magic_properties(InterfacesLocators.in_tree_interface_pro_expert)
    # ChangePropertiesInterface.changing_magic_properties(InterfacesLocators.in_tree_interface_iek_star)
    # ChangePropertiesInterface.changing_magic_properties(InterfacesLocators.in_tree_interface_beregun)
    # ChangePropertiesInterface.changing_magic_properties(InterfacesLocators.in_tree_interface_betar211)
    # # ChangePropertiesInterface.changing_magic_properties(InterfacesLocators.in_tree_interface_bolid)
    # ChangePropertiesInterface.changing_magic_properties(InterfacesLocators.in_tree_interface_bolid_topaz)
    # # ChangePropertiesInterface.changing_magic_properties(InterfacesLocators.in_tree_interface_ivk102)
    # # ChangePropertiesInterface.changing_magic_properties(InterfacesLocators.in_tree_interface_yrcv5xx)
    # ChangePropertiesInterface.changing_magic_properties(InterfacesLocators.in_tree_interface_gran_electro)
    # ChangePropertiesInterface.changing_magic_properties(InterfacesLocators.in_tree_interface_decast)
    # ChangePropertiesInterface.changing_magic_properties(InterfacesLocators.in_tree_interface_integra)
    # ChangePropertiesInterface.changing_magic_properties(InterfacesLocators.in_tree_interface_kaskad)
    # ChangePropertiesInterface.changing_magic_properties(InterfacesLocators.in_tree_interface_lenelectro)
    # ChangePropertiesInterface.changing_magic_properties(InterfacesLocators.in_tree_interface_agat3)
    # ChangePropertiesInterface.changing_magic_properties(InterfacesLocators.in_tree_interface_mzep)
    # ChangePropertiesInterface.changing_magic_properties(InterfacesLocators.in_tree_interface_agat2)
    # ChangePropertiesInterface.changing_magic_properties(InterfacesLocators.in_tree_interface_mercury200)
    # ChangePropertiesInterface.changing_magic_properties(InterfacesLocators.in_tree_interface_mercury230)
    # ChangePropertiesInterface.changing_magic_properties(InterfacesLocators.in_tree_interface_milyr)
    # ChangePropertiesInterface.changing_magic_properties(InterfacesLocators.in_tree_interface_mirtek)
    # ChangePropertiesInterface.changing_magic_properties(InterfacesLocators.in_tree_interface_neva)
    # ChangePropertiesInterface.changing_magic_properties(InterfacesLocators.in_tree_interface_seb2a)
    # ChangePropertiesInterface.changing_magic_properties(InterfacesLocators.in_tree_interface_psch4tm)
    # # ChangePropertiesInterface.changing_magic_properties(InterfacesLocators.in_tree_interface_pulsar_sanext)
    # ChangePropertiesInterface.changing_magic_properties(InterfacesLocators.in_tree_interface_us800_v1)
    # ChangePropertiesInterface.changing_magic_properties(InterfacesLocators.in_tree_interface_us800_v2)
    # ChangePropertiesInterface.changing_magic_properties(InterfacesLocators.in_tree_interface_spb_zip)
    # # ChangePropertiesInterface.changing_magic_properties(InterfacesLocators.in_tree_interface_spodes)
    # ChangePropertiesInterface.changing_magic_properties(InterfacesLocators.in_tree_interface_seb1tm)
    # ChangePropertiesInterface.changing_magic_properties(InterfacesLocators.in_tree_interface_tbn_km5)
    # ChangePropertiesInterface.changing_magic_properties(InterfacesLocators.in_tree_interface_vist)
    # ChangePropertiesInterface.changing_magic_properties(InterfacesLocators.in_tree_interface_chis_mur)
    # # ChangePropertiesInterface.changing_magic_properties(InterfacesLocators.in_tree_interface_exo)
    # ChangePropertiesInterface.changing_magic_properties(InterfacesLocators.in_tree_interface_pulsar_electro)
    # ChangePropertiesInterface.changing_magic_properties(InterfacesLocators.in_tree_interface_energomera_ce102)
    # ChangePropertiesInterface.changing_magic_properties(InterfacesLocators.in_tree_interface_energomera_ce30x)
    # ChangePropertiesInterface.changing_magic_properties(InterfacesLocators.in_tree_interface_energomera_c)
    # ChangePropertiesInterface.changing_magic_properties(InterfacesLocators.in_tree_interface_ey20m)

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


if __name__ == '__main__':
    main()
