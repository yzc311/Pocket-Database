from tarfile import data_filter

import requests

class Administrator:
    cookie = {'BDUSS': '0yNjlTbnlqYmFUV1FjMHJVNExwcWdKT2ZvNEtQdVU4THZHVkNCWU9VQWI3UlpxSVFBQUFBJCQAAAAAAQAAAAEAAAC-BCZ70qbWx7OsMDMxMQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABtg72kbYO9pSU', 'BDUSS_BFESS': '0yNjlTbnlqYmFUV1FjMHJVNExwcWdKT2ZvNEtQdVU4THZHVkNCWU9VQWI3UlpxSVFBQUFBJCQAAAAAAQAAAAEAAAC-BCZ70qbWx7OsMDMxMQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABtg72kbYO9pSU'}
    host = 'https://mime-sh.baidu.com/'
    company_id = 781

    def admin_user_list(self):
        url = f'{self.host}commer/pocket_user/list'
        response = requests.get(url=url, params={'company_id': self.company_id}, cookies=self.cookie)
        if response.status_code == 200:
            return response.json()
        else:
            return None
        
    def admin_add_user(self, user_data):
        url = f'{self.host}commer/pocket_user/save'
        response = requests.post(url=url, data=user_data, cookies=self.cookie)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    
    def admin_update_user(self, user_data):
        url = f'{self.host}commer/pocket_user/save'
        response = requests.post(url=url, data=user_data, cookies=self.cookie)
        if response.status_code == 200:
            return response.json()
        else:
            return None
        
    def admin_delete_user(self, ids):
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
    cookie = {'BDUSS': '0yNjlTbnlqYmFUV1FjMHJVNExwcWdKT2ZvNEtQdVU4THZHVkNCWU9VQWI3UlpxSVFBQUFBJCQAAAAAAQAAAAEAAAC-BCZ70qbWx7OsMDMxMQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABtg72kbYO9pSU', 'BDUSS_BFESS': '0yNjlTbnlqYmFUV1FjMHJVNExwcWdKT2ZvNEtQdVU4THZHVkNCWU9VQWI3UlpxSVFBQUFBJCQAAAAAAQAAAAEAAAC-BCZ70qbWx7OsMDMxMQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABtg72kbYO9pSU'}
    host = 'https://mime-sh.baidu.com/'
    company_id = 781

    def Ordinary_user_list(self):
        url = f'{self.host}commer/pocket_staff/get_data'
        response = requests.get(url=url, params={'company_id': self.company_id}, cookies=self.cookie)
        if response.status_code == 200:
            return response.json() 
        else:
            return None
        
    def Ordinary_user_add(self, user_data):
        url = f'{self.host}commer/pocket_staff/save'
        response = requests.post(url=url, data=user_data, cookies=self.cookie)
        if response.status_code == 200:
            return response.json()
        else:
            return None
        
    def Ordinary_user_update(self, user_data):
        url = f'{self.host}commer/pocket_staff/save'
        response = requests.post(url=url, data=user_data, cookies=self.cookie)
        if response.status_code == 200:
            return response.json()
        else:
            return None
        
    def Ordinary_user_delete(self, ids):
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
    data = {
        "company_id": 781,
        "department_id": 302,
        "name": "1234",
        "phone": "13800000000",
        "auth_ids": [1, 2, 3, 4],
        "id": 2054
    }
    ordinary_employee = Regular_employee()
    result = ordinary_employee.Ordinary_user_update(data)
    print(result)