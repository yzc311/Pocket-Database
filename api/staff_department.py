import config
from common.apiclient_util import ApiClient


class Department:
    '''
    员工管理-部门相关接口
    '''

    def __init__(self):
        # 初始化ApiClient实例
        self.api_client = ApiClient()


    def department_list(self):
        # 获取部门列表
        url = f'{config.host}commer/pocket_staff/get_department_data'
        params = {
            'company_id': config.company_id
        }
        response = self.api_client.request(method='GET', url=url, params=params)
        return response.json()


    def department_get_list(self, page=None, page_size=None):
        # 部门管理-获取列表
        url = f'{config.host}commer/pocket_department/get_list'
        params = {
            'company_id': config.company_id,
            'page': page, # 页码，第一页传1，第二页传2，以此类推，不传默认为1
            'page_size': page_size # 每页条数，不传默认为15
        }
        response = self.api_client.request(method='GET', url=url, params=params)
        return response.json()


    def department_user_list(self, department_id):
        # 获取部门员工列表
        url = f'{config.host}commer/pocket_staff/department_staff'
        params = {
            'company_id': config.company_id,
            'department_id': department_id
        }
        response = self.api_client.request(method='GET', url=url, params=params)
        return response.json()


    def department_save(self, name, id=None, parent_dep_id=None):
        # 添加部门 & 更新部门信息
        url = f'{config.host}commer/pocket_department/save'
        data = {
            'company_id': config.company_id,
            'name': name,
            'id': id, # 更新部门时需要传递部门id，添加部门时不需要传递id
            'parent_dep_id': parent_dep_id # 上级部门id，一级部门传0或者不传递，新权限系统必传
        }
        response = self.api_client.request(method='POST', url=url, data=data)
        return response.json()
        

    def department_user_save(self, department_id, staff_ids):
        # 部门管理-部门员工保存
        url = f'{config.host}commer/pocket_department/save_staff'
        data = {
            'company_id': config.company_id,
            'department_id': department_id,
            'staff_ids': staff_ids
        }
        response = self.api_client.request(method='POST', url=url, data=data)
        return response.json()

    def department_delete(self, ids):
        # 删除部门
        url = f'{config.host}commer/pocket_department/del'
        params = {
            'company_id': config.company_id,
            'ids': ids
        }
        response = self.api_client.request(method='GET', url=url, params=params)
        return response.json()

    def department_user_delete(self, department_id, staff_ids):
        # 部门管理-部门员工删除
        url = f'{config.host}commer/pocket_department/delete_staff'
        data = {
            'company_id': config.company_id,
            'department_id': department_id,
            'staff_ids': staff_ids
        }
        response = self.api_client.request(method='POST', url=url, data=data)
        return response.json()

if __name__ == "__main__":
    department = Department()
    # print(department.department_list())
    # print(department.department_get_list())
    # print(department.department_user_list(department_id=1))
    # print(department.department_save(name='测试部门1', parent_dep_id=0))
    # print(department.department_save(name='测试部门1-修改', id=2, parent_dep_id=0))
    # print(department.department_user_save(department_id=2, staff_ids=[3,4]))
    # print(department.department_user_delete(department_id=2, staff_ids=[3]))
    # print(department.department_delete(ids=[2]))