import config
from common.apiclient_util import ApiClient


class Administrator:
    '''
    员工管理-管理员相关接口
    '''

    def __init__(self):
        # 初始化ApiClient实例
        self.api_client = ApiClient()

    def administrator_list(self, search=None, page=None, page_size=None, order_by=None, orientation=None):
        # 获取管理员列表
        url = f'{config.host}commer/pocket_user/list'
        params = {
            'company_id': config.company_id,
            'search': search, # 搜索 （支持标题、内容、操作人）
            'page': page, # 页数，默认1
            'page_size': page_size, # 每页显示数量，默认15
            'order_by': order_by, # 排序，默认按照操作时间排序
            'orientation': orientation # 排序方向，1代表升序，0代表降序。默认0
        }
        response = self.api_client.request(method='GET', url=url, params=params)
        return response.json()


    def administrator_save(self, name, phone, auth_ids, department_id=None, id=None):
        # 添加管理员 & 更新管理员信息
        url = f'{config.host}commer/pocket_user/save'
        data = {
            'company_id': config.company_id,
            'name': name, # 备注姓名，最长6个汉字
            'phone': phone, # 手机号码，也是账号
            'auth_ids': auth_ids, # 权限id，逗号分隔；1话术权限，2资料库权限，3企业通知权限，4人员管理权限
            'department_id': department_id, # 部门id
            'id': id # 管理员id，更新时必填，添加时不填
        }
        response = self.api_client.request(method='POST', url=url, data=data)
        return response.json()


    def administrator_delete(self, ids):
        # 删除管理员
        url = f'{config.host}commer/pocket_user/del'
        params = {
            'company_id': config.company_id,
            'ids': ids
        }
        response = self.api_client.request(method='GET', url=url, params=params)
        return response.json()

if __name__ == "__main__":
    admin = Administrator()
    # print(admin.administrator_list(search=187))
    # print(admin.administrator_save(name='测试管理员1', phone='18180873861', auth_ids='1,2,3,4', department_id=1))
    # print(admin.administrator_save(name='测试管理员1-修改', phone='18888888888', auth_ids='1,2,3,4', department_id=1, id=3))
    # print(admin.administrator_delete(ids='3,4'))