from selenium.webdriver.common.by import By
from common.ui_util.selenium_driver_util import DriverUtil
import time
import config


driver = DriverUtil.get_driver()
driver.get(config.url)
driver.implicitly_wait(10)
driver.find_element(By.CLASS_NAME,
            "right-import"
        ).click()
elements = driver.find_elements(By.CLASS_NAME, "el-input__inner")
print(f"共有{len(elements)}个输入框:{elements}")
# time.sleep(3)