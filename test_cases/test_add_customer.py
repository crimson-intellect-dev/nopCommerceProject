import pytest
import time

from selenium.webdriver.common.by import By

from page_objects.login_page import LoginPage
from page_objects.add_customer_page import AddCustomer
from utilities.read_propetries import ReadConfig
from utilities.custom_logger import LogGenerator
import string
import random


class Test_003_AddCustomer:
    base_url = ReadConfig.get_base_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGenerator.log_generator()  # Logger

    @pytest.mark.sanity
    def test_add_customer(self, setup):
        self.logger.info("************* Test_003_AddCustomer **********")
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()
        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting Add Customer Test **********")

        self.add_cust = AddCustomer(self.driver)
        self.add_cust.click_on_customers_menu()
        self.add_cust.click_on_customers_menu_item()

        self.add_cust.click_on_add_new()

        self.logger.info("************* Providing customer info **********")

        self.email = random_generator() + "@gmail.com"
        self.add_cust.set_email(self.email)
        self.add_cust.set_password("test123")
        self.add_cust.set_first_name("Pavan")
        self.add_cust.set_last_name("Kumar")
        self.add_cust.set_gender("Male")
        self.add_cust.set_dob("7/05/1985")  # Format: D / MM / YYY
        self.add_cust.set_company_name("busyQA")
        self.add_cust.set_customer_roles("Guests")
        self.add_cust.set_manager_of_vendor("Vendor 2")

        # self.add_cust.set_company_name("This is for testing.........")
        self.add_cust.click_on_save()

        self.logger.info("************* Saving customer info **********")

        self.logger.info("********* Add customer validation started *****************")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text

        print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True
            self.logger.info("********* Add customer Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            self.logger.error("********* Add customer Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Add customer test **********")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
