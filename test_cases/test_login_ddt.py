import time

import pytest

from page_objects.login_page import LoginPage
from utilities.read_propetries import ReadConfig
from utilities.custom_logger import LogGenerator
from utilities import XLUtils


# test case id
class Test_002_DDT_Login:
    base_url = ReadConfig.get_base_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    path = "./test_data/LoginData.xlsx"
    logger = LogGenerator.log_generator()

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("******************** Test_002_DDT_Login ********************")
        self.logger.info("******************** Verifying Login DDT Test ********************")

        self.driver = setup
        self.driver.get(self.base_url)
        self.login_page = LoginPage(self.driver)
        self.rows = XLUtils.get_row_count(self.path, "Sheet1")

        status_list = []

        for row in range(2, self.rows + 1):
            self.user = XLUtils.read_data(self.path, "Sheet1", row, 1)
            self.password = XLUtils.read_data(self.path, "Sheet1", row, 2)
            self.expected_result = XLUtils.read_data(self.path, "Sheet1", row, 3)

            self.login_page.set_username(self.user)
            self.login_page.set_password(self.password)
            self.login_page.click_login()
            time.sleep(5)

            # self.login_page.set_username(self.username)
            # self.login_page.set_password(self.password)
            # self.login_page.click_login()
            actual_title = self.driver.title
            expected_title = "Dashboard / nopCommerce administration"

            if actual_title == expected_title:
                if self.expected_result == 'Pass':
                    self.logger.info("**** passed ****")
                    self.login_page.click_logout()
                    status_list.append("Pass")
                elif self.expected_result == 'Fail':
                    self.logger.info("**** failed ****")
                    self.login_page.click_logout()
                    status_list.append("Fail")
            elif actual_title != expected_title:
                if self.expected_result == 'Pass':
                    self.logger.info("**** failed ****")
                    # self.login_page.click_logout()
                    status_list.append("Fail")
                elif self.expected_result == 'Fail':
                    self.logger.info("**** passed ****")
                    # self.login_page.click_logout()
                    status_list.append("Pass")
            print(status_list)
        if "Fail" not in status_list:
            self.logger.info("******* DDT Login test passed **********")
            self.driver.close()
            assert True
        else:
            self.logger.error("******* DDT Login test failed **********")
            self.driver.close()
            assert False

        self.logger.info("******* End of Login DDT Test **********")
        self.logger.info("**************** Completed  TC_LoginDDT_002 ************* ");
