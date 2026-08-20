import pytest
import allure
from api import staff_administrator
from common.api_util import read_util


class TestStaffAdministrator:
    '''
    测试管理员
    '''
    @allure.epic('口袋资料库')
    @allure.feature("员工管理")
    @allure.story("管理员")
    @allure.title('获取管理员列表')
    @pytest.mark.smoke
    def test_get_administrator_list(self):
        '''
        测试获取管理员列表
        '''
        administrator = staff_administrator.Administrator()
        administrator_list = administrator.administrator_list()
        assert administrator_list is not None
        assert len(administrator_list) > 0
        assert administrator_list.get('ecode') == 0
        assert administrator_list.get('emsg') == 'OK'

    @allure.epic('口袋资料库')
    @allure.feature("员工管理")
    @allure.story("管理员")
    @allure.title('添加管理员')
    @pytest.mark.usefixtures("data_Change")
    @pytest.mark.parametrize("phones, names, department, permission", read_util.ReadUtil.read_excel_data('data/data.xlsx'))
    def test_add_administrator(self, phones, names, department, permission):
        '''
        测试添加管理员
        '''

        administrator = staff_administrator.Administrator()

        resp = administrator.administrator_add(
            name=names,
            phone=str(phones),
            auth_ids=permission,
            department_id=department
        )

        assert resp is not None

        assert resp.get('ecode') == 0
        assert resp.get('emsg') == 'OK'

