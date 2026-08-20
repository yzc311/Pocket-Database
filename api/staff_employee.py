import requests
import config


class Employee:
    '''
    员工管理-普通员工相关接口
    '''

    def employee_list(self, page=None, page_size=None, order_by=None, orientation=None, auths=None):
        # 获取普通员工列表
        url = f'{config.host}commer/pocket_staff/get_data'
        params = {
            'company_id': config.company_id,
            'mock_uid': config.mock_uid,
            'mock_uuid': config.mock_uuid,
            'page': page, # 页码，默认值：1
            'page_size': page_size, # 每页数量，默认值：15
            'order_by': order_by, # 排序，默认按照操作时间排序
            'orientation': orientation, # 排序方向，1：升序，0：降序，默认值：0
            'auths': auths # 可阅读内容，权限id，逗号分隔，默认全部
        }
        response = requests.get(url=url, params=params)
        if response.status_code == 200:
            return response.json() 
        else:
            return None
        
    def employee_add(self, phone, name, department_id, auth_ids, id=None, role_id=None):
        # 添加普通员工
        url = f'{config.host}commer/pocket_staff/save'
        params = {
            'mock_uid': config.mock_uid,
            'mock_uuid': config.mock_uuid
        }
        data = {
            'company_id': config.company_id,
            'name': name, # 员工姓名
            'phone': phone, # 员工手机号
            'department_id': department_id, # 部门id，逗号分隔
            'auth_ids': auth_ids, # 可阅读内容，权限id，逗号分隔
            'id': id, # 员工id，更新时必填
            'role_id': role_id # 新版权限系统必填，1 普通员工 2 部门管理员
        }
        response = requests.post(url=url, params=params, data=data)
        if response.status_code == 200:
            return response.json()
        else:
            return None
        
    def employee_update(self, phone, name, department_id, auth_ids, id=None, role_id=None):
        # 更新普通员工信息
        url = f'{config.host}commer/pocket_staff/save'
        params = {
            'mock_uid': config.mock_uid,
            'mock_uuid': config.mock_uuid
        }
        data = {
            'company_id': config.company_id,
            'name': name, # 员工姓名
            'phone': phone, # 员工手机号
            'department_id': department_id, # 部门id，逗号分隔
            'auth_ids': auth_ids, # 可阅读内容，权限id，逗号分隔，默认全部
            'id': id, # 员工id，更新时必填
            'role_id': role_id # 新版权限系统必填，1 普通员工 2 部门管理员
        }
        response = requests.post(url=url, params=params, data=data)
        if response.status_code == 200:
            return response.json()
        else:
            return None
        
    def employee_delete(self, ids):
        # 删除普通员工
        url = f'{config.host}commer/pocket_staff/del'
        params = {
            'mock_uid': config.mock_uid,
            'mock_uuid': config.mock_uuid,
            'company_id': config.company_id,
            'ids': ids
        }
        response = requests.get(url=url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return None
        

if __name__ == "__main__":
    user = Employee()
    print(user.employee_list())
    # print(user.employee_add(phone='18888888888', name='测试员工1', department_id='1', auth_ids='1,2,3', role_id=1))
    # print(user.employee_update(phone='18888888888', name='测试员工1-修改', department_id='1', auth_ids='1,2,3', id=3, role_id=1))
    # print(user.employee_delete(ids='3,4'))