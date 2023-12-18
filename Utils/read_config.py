from typing import List, Dict, Optional

import yaml
from pydantic import BaseModel, Field

from Utils.logger import logger


class VmAuth(BaseModel):
    """ Для авторизационных данных виртуальных машин """

    login: str
    password: str


class VSphere(BaseModel):
    """ Для конфигурации VSphere """

    host: str
    user: str
    password: str

    data_store: str
    vms: Dict[str, VmAuth]
    vm_for_bloc2: str
    snapshot_name: str

    usb_info: Dict = Field(alias="UsbInfo")

    network_card_name: str
    static_ip_address_pool: List
    gateway: str
    dns: str


class TeamCityConfig(BaseModel):
    """ Для авторизационных данных тим сити """

    login: str
    password: str
    for_test_programs_info: dict
    history_file_path: str = Field(alias="HistoryFilePath")


class Programs(BaseModel):
    """ Дата класс тестируемых программ """

    name: str
    last_bild: str
    licenses_for_max_tests: int
    bloc1: str
    bloc2: dict  # либо ничего, либо список с именем стенда и значением -
    # путем со скомпилированным тестом


class Ranorex(BaseModel):
    """ Информация об артефактах Ranorex """

    all_licenses: int
    dir_to_logs: str
    path_to_pdf_converter: str
    programs_for_tests: List[Programs] = Field(alias="ProgramsForTests")


class Email(BaseModel):
    """ Информация о настройках почты и получателях отчетов (в зависимости от софта) """

    server: str
    port: int
    send_from: str
    login: str
    password: str
    soft: dict
    network_folder: str


class AppConfig(BaseModel):
    """ Описание основного модуля управления приложением """

    email: Email = Field(alias="Email")
    esxi: VSphere = Field(alias="VSphere")
    team_city: TeamCityConfig = Field(alias="TeamCity")
    time_for_test_activate: str = Field(alias="TimeForTestActivate")
    ranorex: Ranorex = Field(alias="Ranorex")


def read_yaml_config_and_convert_to_app_config(path: str) -> AppConfig:
    """ Прочесть yaml config и вернуть структуру данных """

    with open(path, "r", encoding="utf-8") as yaml_file:
        data = yaml.load(yaml_file, Loader=yaml.FullLoader)
        logger.debug("Read config successful")

    return AppConfig(**data)


# Tests
if __name__ == '__main__':
    app_config = read_yaml_config_and_convert_to_app_config("C:\\Users\\shapoval\\Documents\\AutoWebClient\\config.yaml")
    logger.debug(app_config.esxi.vms)
