import pytest
import config
from api import staff_administrator
# from common.api_util import write_util
from common import read_util


@pytest.fixture
def data_change():
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
            config.BASE_DIR / "data" / "data.xlsx"
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
