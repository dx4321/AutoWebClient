import time
from typing import List

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from Utils.XL import XL
from Utils.logger import logger
from Utils.read_config import read_yaml_config_and_convert_to_app_config, AppConfig


class TeamCity:
    def __init__(self, driver_path: str, app_config: AppConfig, driver_visible=True):

        self.driver: webdriver = self.get_driver(driver_path, visible=driver_visible)
        self.login: str = app_config.team_city.login
        self.password: str = app_config.team_city.password
        self.team_city_config = app_config.team_city
        self.app_config = app_config

        self.for_tests_links_builds: dict = \
            self.team_city_config.for_test_programs_info

        self.builds_counts: int = len(self.for_tests_links_builds.keys())
        self.XL = XL(app_config)

    @classmethod
    def get_driver(cls, _driver_path, visible: bool) -> webdriver:
        """
            Получить веб драйвер
        :param _driver_path: путь к драйверу
        :arg visible - Указать показывать ли браузер, либо нет
        :return driver
        """

        options = Options()
        options.add_argument("--start-maximized")

        if visible is True:
            _driver = webdriver.Chrome(_driver_path, options=options)
        else:
            options.headless = True
            _driver = webdriver.Chrome(_driver_path, options=options)

        return _driver

    def login_for_teamcity(self) -> bool:
        """ Залогиниться в тим сити """

        self.driver.get("http://teamcity.bolid.ru/login.html")

        assert "Log in to" in self.driver.title, "Страница не загрузилась"

        user_name_fild = self.driver.find_element(By.ID, 'username')
        password_fild = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.CLASS_NAME, "buttons")

        user_name_fild.send_keys("login")
        password_fild.send_keys("password")
        login_button.click()
        time.sleep(1)

        return True

    def check_last_bild_if_him_change_and_get_list_programs_for_tests(self) -> List:
        """ Проверить вышла ли последняя сборка
                Если новая сборка вышла, то сохранить ее в excel файл на
                последней строке под названием необходимой программы

            :return - вернуть список программ для которых вышла новая сборка
            (в дальнейшем по ним будут происходить тесты)
        """

        programs_for_new_tests = []

        for prog in self.for_tests_links_builds.keys():
            self.driver.get(self.for_tests_links_builds[prog])
            time.sleep(2)
            logger.debug(self.driver.title)

            build_number = self.driver.find_elements(
                By.XPATH, "//div[@class='col_2eb Build__number--3S']"
            )
            status = self.driver.find_elements(
                By.CLASS_NAME, 'Build__status--26'
            )
            logger.debug(
                f"У {prog} - номер последней сборки -> {build_number[0].text}, "
                f"сборка находится в статусе -> {status[0].text}"
            )

            last_build_in_excel_for_prog = self.XL.get_last_str_for_soft(prog)

            if last_build_in_excel_for_prog != build_number[0].text:
                self.XL.save_to_last_line(prog, build_number[0].text)
                programs_for_new_tests.append(prog)
                # Если есть последняя сборка, то обновить данные
                for testing_po in self.app_config.ranorex.programs_for_tests:
                    if testing_po.name == prog:
                        testing_po.last_bild = build_number[0].text
            else:
                # Если нет, то вернуть None
                for testing_po in self.app_config.ranorex.programs_for_tests:
                    if testing_po.name == prog:
                        testing_po.last_bild = None

                programs_for_new_tests.append(None)

        return programs_for_new_tests


# Tests
if __name__ == '__main__':
    config_app = read_yaml_config_and_convert_to_app_config("C:\\Users\\shapoval\\Documents\\AutoWebClient\\config.yaml")
    tc = TeamCity("C:\\Users\\shapoval\\Documents\\AutoWebClient\\chromedriver\\chromedriver.exe", config_app, driver_visible=True)
    tc.login_for_teamcity()
    list_programs_for_new_tests = tc.check_last_bild_if_him_change_and_get_list_programs_for_tests()
    logger.debug(f"Программы для новых тестов - {list_programs_for_new_tests}")

