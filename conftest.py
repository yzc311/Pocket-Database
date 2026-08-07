import pytest
from api import staff_administrator
from common import read_util, write_util
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def data_Change():
    '''
    测试数据准备
    '''

    # 写入excel 数据
    # write_util.WriteUtil.write_file(10)


    yield


    print("测试数据清理")

    phones = [
        row[0]
        for row in read_util.ReadUtil.read_excel_data(
            'data/data.xlsx'
        )
    ]

    admins = staff_administrator.Administrator()

    ids = []


    for phone in phones:

        data = admins.administrator_list(
            search=phone
        )

        user_data = (
            data
            .get('data', {})
            .get('list', [])
        )


        user_id = (
            user_data[0].get('id')
            if user_data
            else None
        )


        ids.append(user_id)


    ids_str = ",".join(
        map(str, ids)
    )


    admins.administrator_delete(
        ids=ids_str
    )



# ============================
# 新增 Selenium fixture
# ============================



@pytest.fixture(scope="session")
def driver():

    options = Options()


    profile_path = os.path.abspath(
        "data/chrome_profile"
    )


    options.add_argument(
        f"--user-data-dir={profile_path}"
    )


    driver = webdriver.Chrome(
        options=options
    )


    driver.maximize_window()


    driver.get(
        "你的百度后台地址"
    )


    input(
        "首次运行请扫码登录，完成后按回车:"
    )


    yield driver


    driver.quit()