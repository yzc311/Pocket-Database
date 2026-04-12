from http.cookiejar import Cookie
import requests

def user_list():
    url = 'https://mime.baidu.com/commer/pocket_user/list'
    params = {
        'company_id': 3177
    }
    cookie = {
        'BDUSS': 'jZYM3hDY1NwU1I1VnlyZkxxeUlndWRFeHNGY0tOMTBoNEI1cjZZbWpCYVRaQUpxSVFBQUFBJCQAAAAAAQAAAAEAAAC-BCZ70qbWx7OsMDMxMQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJPX2mmT19ppY; BDUSS_BFESS=jZYM3hDY1NwU1I1VnlyZkxxeUlndWRFeHNGY0tOMTBoNEI1cjZZbWpCYVRaQUpxSVFBQUFBJCQAAAAAAQAAAAEAAAC-BCZ70qbWx7OsMDMxMQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJPX2mmT19ppY',
        # Add other necessary cookies if required
    }
    response = requests.get(url, params=params, cookies=cookie)
    if response.status_code == 200:
        return response.json()
    else:
        return None
    

if __name__ == "__main__":
    users = user_list()
    if users:
        print(users)
    else:
        print("Failed to retrieve user list.")