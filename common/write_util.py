import pandas as pd
import random
import project_root


class WriteUtil:
    '''
    制造测试数据并写入excel文件
    '''
    @classmethod
    def write_file(cls,num):
        '''
        生成随机数据并写入excel文件
        '''
        nums = random.sample(range(100000000, 1000000000), num)
        phones = ["18" + str(n) for n in nums]
        '''
        生成随机手机号
        '''

        names = [
            ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=3))
            for _ in range(num)
            ]
        '''
        生成随机姓名
        '''

        department = [
            random.randint(291, 299)
            for _ in range(num)
        ]
        '''
        生成随机部门编号
        '''

        permission = [
            random.sample(range(1, 8), k=random.randint(1, 7))
            for _ in range(num)
        ]
        '''
        生成随机权限编号
        '''
        df = pd.DataFrame({'phones': phones, 'names': names, 'department': department, 'permission': permission})
        path = project_root.get_project_root() / 'data' / 'data.xlsx'
        df.to_excel(path, index=False)
        return df

if __name__ == "__main__":

    names_list = WriteUtil.write_file(10)
    print(names_list)