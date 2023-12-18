from Settings.Functions import *
from Settings.DriverSettings import *
import time

from Settings.Locators import *

driver.get(url="http://127.0.0.1:88/")
time.sleep(1)

try:
    LoginPage.type_login()
    LoginPage.type_password()
    LoginPage.sign_in()
    LoginPage.verification()
    Channels.device_tree_click()

    # - начинаем проверку дерева устройств
    Channels.add_channels(ChannelsLocators.add_gprsresursgsm, ChannelsLocators.in_tree_gprsresursgsm, "[GPRS] Ресурс-GSM Интернет")
    Interfaces.add_interfaces(ChannelsLocators.in_tree_gprsresursgsm)
    Counters.add_counters(InterfacesLocators.in_tree_interface_weser_pulsar)
    Counters.add_counters(InterfacesLocators.in_tree_interface_avektra)
    Counters.add_counters(InterfacesLocators.in_tree_interface_puls_st15a)
    Counters.add_counters(InterfacesLocators.in_tree_interface_meter_bus)
    Counters.add_counters(InterfacesLocators.in_tree_interface_mercury200_plc)
    Counters.add_counters(InterfacesLocators.in_tree_interface_mercury230_plc)
    Counters.add_counters(InterfacesLocators.in_tree_interface_vkg2)
    Counters.add_counters(InterfacesLocators.in_tree_interface_vkg7m)
    Counters.add_counters(InterfacesLocators.in_tree_interface_vkt9)
    Counters.add_counters(InterfacesLocators.in_tree_interface_multical)
    Counters.add_counters(InterfacesLocators.in_tree_interface_tcrv_02x)
    Counters.add_counters(InterfacesLocators.in_tree_interface_kyb1)
    Counters.add_counters(InterfacesLocators.in_tree_interface_logica)
    Counters.add_counters(InterfacesLocators.in_tree_interface_tmk)
    Counters.add_counters(InterfacesLocators.in_tree_interface_teross)
    Counters.add_counters(InterfacesLocators.in_tree_interface_tv7)
    Counters.add_counters(InterfacesLocators.in_tree_interface_karat_306)
    Counters.add_counters(InterfacesLocators.in_tree_interface_karat_compact)
    Counters.add_counters(InterfacesLocators.in_tree_interface_abb)
    Counters.add_counters(InterfacesLocators.in_tree_interface_dfm_marine)
    Counters.add_counters(InterfacesLocators.in_tree_interface_danfoss)
    Counters.add_counters(InterfacesLocators.in_tree_interface_pro_expert)
    Counters.add_counters(InterfacesLocators.in_tree_interface_iek_star)
    Counters.add_counters(InterfacesLocators.in_tree_interface_beregun)
    Counters.add_counters(InterfacesLocators.in_tree_interface_betar211)
    Counters.add_counters(InterfacesLocators.in_tree_interface_bolid)
    Counters.add_counters(InterfacesLocators.in_tree_interface_bolid_topaz)
    Counters.add_counters(InterfacesLocators.in_tree_interface_ivk102)
    Counters.add_counters(InterfacesLocators.in_tree_interface_yrcv5xx)
    Counters.add_counters(InterfacesLocators.in_tree_interface_gran_electro)
    Counters.add_counters(InterfacesLocators.in_tree_interface_decast)
    Counters.add_counters(InterfacesLocators.in_tree_interface_integra)
    Counters.add_counters(InterfacesLocators.in_tree_interface_kaskad)
    Counters.add_counters(InterfacesLocators.in_tree_interface_lenelectro)
    Counters.add_counters(InterfacesLocators.in_tree_interface_agat3)
    Counters.add_counters(InterfacesLocators.in_tree_interface_mzep)
    Counters.add_counters(InterfacesLocators.in_tree_interface_agat2)
    Counters.add_counters(InterfacesLocators.in_tree_interface_mzep_old)
    Counters.add_counters(InterfacesLocators.in_tree_interface_mercury200)
    Counters.add_counters(InterfacesLocators.in_tree_interface_mercury230)
    Counters.add_counters(InterfacesLocators.in_tree_interface_milyr)
    Counters.add_counters(InterfacesLocators.in_tree_interface_mirtek)
    Counters.add_counters(InterfacesLocators.in_tree_interface_neva)
    Counters.add_counters(InterfacesLocators.in_tree_interface_seb2a)
    Counters.add_counters(InterfacesLocators.in_tree_interface_psch4tm)
    Counters.add_counters(InterfacesLocators.in_tree_interface_pulsar_sanext)
    Counters.add_counters(InterfacesLocators.in_tree_interface_us800_v1)
    Counters.add_counters(InterfacesLocators.in_tree_interface_us800_v2)
    Counters.add_counters(InterfacesLocators.in_tree_interface_spb_zip)
    Counters.add_counters(InterfacesLocators.in_tree_interface_spodes)
    Counters.add_counters(InterfacesLocators.in_tree_interface_seb1tm)
    Counters.add_counters(InterfacesLocators.in_tree_interface_tbn_km5)
    Counters.add_counters(InterfacesLocators.in_tree_interface_tem104)
    Counters.add_counters(InterfacesLocators.in_tree_interface_vist)
    Counters.add_counters(InterfacesLocators.in_tree_interface_chis_mur)
    Counters.add_counters(InterfacesLocators.in_tree_interface_exo)
    Counters.add_counters(InterfacesLocators.in_tree_interface_pulsar_electro)
    Counters.add_counters(InterfacesLocators.in_tree_interface_energomera_ce102)
    Counters.add_counters(InterfacesLocators.in_tree_interface_energomera_ce30x)
    Counters.add_counters(InterfacesLocators.in_tree_interface_energomera_c)
    Counters.add_counters(InterfacesLocators.in_tree_interface_ey20m)


    # - переходим к проверке дерева абонентов
    # Users.users_tree_click()

    # Users.add_homes(UsersLocators.add_house, UsersLocators.in_tree_house, "Здание_01")
    # Users.add_homes(UsersLocators.add_management_company, UsersLocators.in_tree_management_company, "Управляющая компания_01")


finally:

    driver.close()
    driver.quit()