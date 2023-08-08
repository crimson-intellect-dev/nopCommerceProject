import time
import pytest
from page_objects.login_page import LoginPage
from page_objects.add_customer_page import AddCustomer
from page_objects.search_curtomer_page import SearchCustomer
from utilities.read_propetries import ReadConfig
from utilities.custom_logger import LogGenerator


class Test_SearchCustomerByEmail_004:
    baseURL = ReadConfig.get_base_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGenerator.log_generator()  # Logger

    @pytest.mark.regression
    def test_search_customer_by_email(self, setup):
        self.logger.info("************* SearchCustomerByEmail_004 **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()
        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting Search Customer By Email **********")

        self.add_cust = AddCustomer(self.driver)
        self.add_cust.click_on_customers_menu()
        self.add_cust.click_on_customers_menu_item()

        self.logger.info("************* searching customer by emailID **********")
        search_cust = SearchCustomer(self.driver)
        search_cust.set_email("victoria_victoria@nopCommerce.com")
        search_cust.click_search()
        time.sleep(5)
        status = search_cust.search_customer_by_email("victoria_victoria@nopCommerce.com")
        self.driver.close()
        assert True == status
        self.logger.info("***************  TC_SearchCustomerByEmail_004 Finished  *********** ")
