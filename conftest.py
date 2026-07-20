import pytest
from api import staff_administrator
from common import read_util, write_util


@pytest.fixture
def data_Change():
    '''
    测试数据准备
    '''
    # 写入Excel数据
    # print("测试数据准备")
    # write_util.WriteUtil.write_file(10)
    
    yield

    print("测试数据清理")
    phones = [
    row[0] for row in read_util.ReadUtil.read_excel_data('data/data.xlsx')
    ]
    admins = staff_administrator.Administrator()
    ids = [] # 管理员id列表
    for phone in phones:
        # 获取新增管理员id
        data = admins.administrator_list(search=phone)
        user_data = data.get('data', {}).get('list', [])
        user_id = user_data[0].get('id') if user_data else None
        ids.append(user_id)
    ids_str = ",".join(map(str, ids))
    # 删除管理员
    admins.administrator_delete(ids=ids_str)
