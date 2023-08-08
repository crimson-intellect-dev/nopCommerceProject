import pytest

from page_objects.login_page import LoginPage
from utilities.read_propetries import ReadConfig
from utilities.custom_logger import LogGenerator


# test case id
class Test_001_Login:
    base_url = ReadConfig.get_base_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()

    logger = LogGenerator.log_generator()

    @pytest.mark.regression
    def test_homepage_title(self, setup):
        self.logger.info("******************** Test_001_Login ********************")
        self.logger.info("******************** Verifying Homepage Title ********************")

        self.driver = setup
        self.driver.get(self.base_url)
        actual_title = self.driver.title

        if actual_title == "Your store. Login":
            self.driver.close()
            assert True
            self.logger.info("******************** Homepage Title Test Passed ********************")
        else:
            self.driver.save_screenshot("./screenshots/" + "test_homepage_title.png")
            self.driver.close()
            self.logger.error("******************** Verifying Homepage Failed ********************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("******************** Verifying Login Test ********************")

        self.driver = setup
        self.driver.get(self.base_url)
        self.login_page = LoginPage(self.driver)
        self.login_page.set_username(self.username)
        self.login_page.set_password(self.password)
        self.login_page.click_login()
        actual_title = self.driver.title

        if actual_title == "Dashboard / nopCommerce administration":
            self.driver.close()
            self.logger.info("******************** Verifying Login Test Passed ********************")
            assert True
        else:
            self.driver.save_screenshot("./screenshots/" + "test_login.png")
            self.driver.close()
            self.logger.error("******************** Verifying Login Test Failed ********************")

            assert False



























