# import pytest
# from api import staff_administrator


# class a:
#     '''
#     测试管理员
#     '''
#     def b(self):
#         '''
#         测试获取管理员列表
#         '''
#         administrator = staff_administrator.Administrator()
#         administrator_list = administrator.administrator_list()
#         # assert administrator_list is not None
#         # assert len(administrator_list) > 0
#         # assert administrator_list.get('ecode') == 0
#         return administrator_list

# if __name__ == '__main__':
#     a = a()
#     b = a.b()
#     print(b.get('emsg'))
    

# str1 = "abcdefg"

# m = len(str1) - 1

# while m >= 0:
#     print(str1[m])
#     m -= 1

from common import read_util


read = read_util.ReadUtil.read_file('data/data.xlsx')
print(read)