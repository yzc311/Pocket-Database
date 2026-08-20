from selenium.webdriver.common.by import By

class AdministratorPage:

    def __init__(self, driver):
        self.driver = driver

    # 点击添加管理员按钮
    def click_import_button(self):
        self.driver.find_element(
            By.CLASS_NAME,
            "right-import"
        ).click()


    # # 输入手机号
    # def input_phone(self, phone):
    #     self.driver.find_element(
    #         By.XPATH,
    #         "//input[@placeholder='请输入登录百度账号的手机号码']"
    #     ).send_keys(phone)

    # 输入手机号
    def input_phone(self):
        elements = self.driver.find_elements(
            By.CLASS_NAME,
            "el-input__inner"
        )
        print(f"共有 {len(elements)} 个输入框")


    # 输入姓名
    def input_name(self, name):
        self.driver.find_element(
            By.XPATH,
            "//input[@placeholder='请输入']"
        ).send_keys(name)