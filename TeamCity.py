import time

from Settings.DriverSettings import *
from Settings.Locators import *


class TeamCity:
    def __init__(self, driver_path: str, driver_visible=True):

        self.driver: webdriver = self.get_driver(driver_path, visible=driver_visible)
        self.login: str = "fishzon"
        self.password: str = "fishzon"
        self.team_city = "http://teamcity.bolid.ru/buildConfiguration/ArmResurs_ArmResursInstall10_Work?branch=%3Cdefault%3E&buildTypeTab=overview"
        self.prog = "ArmResurs"

    @classmethod
    def get_driver(cls, _driver_path, visible: bool) -> webdriver:

        options = Options()
        options.add_argument("--start-maximized")
        PATH = r"C:\Users\fishzon\Downloads"
        p = {"download.default_directory": PATH, "safebrowsing.enabled": "false"}
        options.add_experimental_option("prefs", p)

        if visible is True:
            _driver = webdriver.Chrome(_driver_path, options=options)
        else:
            options.headless = True
            _driver = webdriver.Chrome(_driver_path, options=options)

        return _driver

    def login_for_teamcity(self) -> bool:
        """ Залогиниться в TeamCity """

        self.driver.get("http://teamcity.bolid.ru/login.html")

        assert "Log in to" in self.driver.title, "Страница не загрузилась"

        user_name_fild = self.driver.find_element(By.ID, 'username')
        password_fild = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.CLASS_NAME, "buttons")

        user_name_fild.send_keys(self.login)
        password_fild.send_keys(self.password)
        login_button.click()
        time.sleep(2)

        return True

    def download_last_bild(self):
        """ Cкачать последную сборку"""

        self.driver.get(self.team_city)
        time.sleep(2)
        print(self.driver.title)

        build_number = self.driver.find_elements(By.XPATH,
                                                 "//div[@class='BuildDetails__build--3a']//span[contains (@title, 'Build')]")
        status = self.driver.find_elements(By.CLASS_NAME, 'Build__status--26')
        print(
            f"У {self.prog} - номер последней сборки -> {build_number[0].text}, "f"сборка находится в статусе -> {status[0].text}")
        build_number[0].click()
        time.sleep(2)
        self.driver.find_element(By.ID, "artifacts_Tab").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, TeamCityLocators.ArmResursExe).click()

        input()


# Точка входа
if __name__ == '__main__':
    tc = TeamCity("C:\\Users\\fishzon\\Documents\\AutoWebClient\\chromedriver\\chromedriver.exe", driver_visible=True)
    tc.login_for_teamcity()
    tc.download_last_bild()
