import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


class DriverUtil:


    @classmethod
    def get_driver(cls):

        options = Options()


        # 调试阶段保留
        options.add_experimental_option(
            "detach",
            True
        )


        # Chrome用户目录
        profile_path = os.path.abspath(
            "data/chrome_profile"
        )


        options.add_argument(
            f"--user-data-dir={profile_path}"
        )


        service = Service(
            executable_path=os.path.abspath(
                "chromedriver.exe"
            )
        )


        driver = webdriver.Chrome(
            service=service,
            options=options
        )


        # driver.maximize_window()


        return driver