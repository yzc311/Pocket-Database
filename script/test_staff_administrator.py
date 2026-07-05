import pytest
from api import staff_administrator


class TestStaffAdministrator:
    '''
    测试管理员
    '''
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

