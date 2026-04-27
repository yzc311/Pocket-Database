from tarfile import data_filter

import requests

class Administrator:
    '''
    员工管理-管理员相关接口
    '''
    cookie = {'BDUSS': '0yNjlTbnlqYmFUV1FjMHJVNExwcWdKT2ZvNEtQdVU4THZHVkNCWU9VQWI3UlpxSVFBQUFBJCQAAAAAAQAAAAEAAAC-BCZ70qbWx7OsMDMxMQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABtg72kbYO9pSU', 'BDUSS_BFESS': '0yNjlTbnlqYmFUV1FjMHJVNExwcWdKT2ZvNEtQdVU4THZHVkNCWU9VQWI3UlpxSVFBQUFBJCQAAAAAAQAAAAEAAAC-BCZ70qbWx7OsMDMxMQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABtg72kbYO9pSU'}
    host = 'https://mime-sh.baidu.com/'
    company_id = 781

    def admin_user_list(self):
        # 获取管理员列表
        url = f'{self.host}commer/pocket_user/list'
        response = requests.get(url=url, params={'company_id': self.company_id}, cookies=self.cookie)
        if response.status_code == 200:
            return response.json()
        else:
            return None
        
    def admin_add_user(self, user_data):
        # 添加管理员
        url = f'{self.host}commer/pocket_user/save'
        response = requests.post(url=url, data=user_data, cookies=self.cookie)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    
    def admin_update_user(self, user_data):
        # 更新管理员信息
        url = f'{self.host}commer/pocket_user/save'
        response = requests.post(url=url, data=user_data, cookies=self.cookie)
        if response.status_code == 200:
            return response.json()
        else:
            return None
        
    def admin_delete_user(self, ids):
        # 删除管理员
        url = f'{self.host}commer/pocket_user/del'
        params = {
            'company_id': self.company_id,
            'ids': ids
        }
        response = requests.get(url=url, cookies=self.cookie, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return None
        
class Regular_employee:
    '''
    员工管理-普通员工相关接口
    '''
    cookie = {'BDUSS': '0yNjlTbnlqYmFUV1FjMHJVNExwcWdKT2ZvNEtQdVU4THZHVkNCWU9VQWI3UlpxSVFBQUFBJCQAAAAAAQAAAAEAAAC-BCZ70qbWx7OsMDMxMQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABtg72kbYO9pSU', 'BDUSS_BFESS': '0yNjlTbnlqYmFUV1FjMHJVNExwcWdKT2ZvNEtQdVU4THZHVkNCWU9VQWI3UlpxSVFBQUFBJCQAAAAAAQAAAAEAAAC-BCZ70qbWx7OsMDMxMQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABtg72kbYO9pSU'}
    host = 'https://mime-sh.baidu.com/'
    company_id = 781

    def Ordinary_user_list(self):
        # 获取普通员工列表
        url = f'{self.host}commer/pocket_staff/get_data'
        response = requests.get(url=url, params={'company_id': self.company_id}, cookies=self.cookie)
        if response.status_code == 200:
            return response.json() 
        else:
            return None
        
    def Ordinary_user_add(self, user_data):
        # 添加普通员工
        url = f'{self.host}commer/pocket_staff/save'
        response = requests.post(url=url, data=user_data, cookies=self.cookie)
        if response.status_code == 200:
            return response.json()
        else:
            return None
        
    def Ordinary_user_update(self, user_data):
        # 更新普通员工信息
        url = f'{self.host}commer/pocket_staff/save'
        response = requests.post(url=url, data=user_data, cookies=self.cookie)
        if response.status_code == 200:
            return response.json()
        else:
            return None
        
    def Ordinary_user_delete(self, ids):
        # 删除普通员工
        url = f'{self.host}commer/pocket_staff/del'
        params = {
            'company_id': self.company_id,
            'ids': ids
        }
        response = requests.get(url=url, cookies=self.cookie, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return None




if __name__ == "__main__":
    pass
