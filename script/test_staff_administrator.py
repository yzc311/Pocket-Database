import pytest
from api import staff_administrator
from common import write_util
from common import read_util


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
    

    # def test_add_administrator(self):
    #     '''
    #     测试添加管理员
    #     '''
    #     write_util.WriteUtil.write_file(10)
    #     read = read_util.ReadUtil.read_file('data/data.xlsx')
    #     administrator = staff_administrator.Administrator()

    #     for _, row in read.iterrows():
    #         resp = administrator.administrator_add(
    #             name=row.get('names'),
    #             phone=str(row.get('phones')),
    #             auth_ids=read_util.ReadUtil.format_auth_ids(row.get('permission')),
    #             department_id=row.get('department')
    #         )
    #         assert resp is not None
    #         if resp.get('ecode') == 1003 and resp.get('emsg') == 'phone error':
    #             continue
    #         assert resp.get('ecode') == 0
    #         assert resp.get('emsg') == 'OK'


    # @pytest.mark.parametrize("phones, names, department, permission", read_util.ReadUtil.read_excel_data('data/data.xlsx'))
    # def test_add_administrator(self, phones, names, department, permission):
    #     '''
    #     测试添加管理员
    #     '''
    #     write_util.WriteUtil.write_file(10)
    #     read = read_util.ReadUtil.read_excel_data('data/data.xlsx')
    #     administrator = staff_administrator.Administrator()

    #     for _, row in read.iterrows():
    #         resp = administrator.administrator_add(
    #             name=row.get('names'),
    #             phone=str(row.get('phones')),
    #             auth_ids=read_util.ReadUtil.format_auth_ids(row.get('permission')),
    #             department_id=row.get('department')
    #         )
    #         assert resp is not None
    #         if resp.get('ecode') == 1003 and resp.get('emsg') == 'phone error':
    #             continue
    #         assert resp.get('ecode') == 0
    #         assert resp.get('emsg') == 'OK'


    @pytest.mark.parametrize(
    "phones, names, department, permission",
    read_util.ReadUtil.read_excel_data('data/data.xlsx')
)
    def test_add_administrator(
        self,
        phones,
        names,
        department,
        permission
):
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

pytest.main()