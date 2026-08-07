from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

import os
import time

import config


options = Options()


# 保持浏览器不关闭（练习阶段方便观察）
options.add_experimental_option(
    "detach",
    True
)


# Chrome用户目录
# 用来保存登录状态
profile_path = os.path.abspath(
    "data/chrome_profile"
)


options.add_argument(
    f"--user-data-dir={profile_path}"
)



# 指定chromedriver

service = Service(
    executable_path=
    r"chromedriver.exe"
)



driver = webdriver.Chrome(
    service=service,
    options=options
)



driver.maximize_window()



# 打开百度页面
driver.get(
    config.url
)



print("浏览器打开成功")



input(
    "如果需要登录请扫码，完成后按回车继续:"
)



time.sleep(5)