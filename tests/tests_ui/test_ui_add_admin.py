import pytest
import config
from page.administrator_page import AdministratorPage

class TestAdmin:
    def test_add_admin(self,driver):
        driver.get(config.url)
        driver.implicitly_wait(10)
        admin_page = AdministratorPage(driver)
        admin_page.click_import_button()
        admin_page.input_phone("18112637212")
        admin_page.input_name("test")