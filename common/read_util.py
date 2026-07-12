import ast
import pandas as pd
from config import BASE_DIR



class ReadUtil:
    '''
    读取excel文件
    '''

    @classmethod
    def read_excel_data(cls, file_path):
        '''
        读取excel并格式化数据，用于pytest参数化

        :param file_path: excel文件路径
        :return: list
        '''

        # 1.读取excel
        df = pd.read_excel(file_path)

        # 2.处理permission字段
        if "permission" in df.columns:
            df["permission"] = df["permission"].apply(cls.format_auth_ids)

        # 3.转换成pytest参数化格式
        data = df.values.tolist()

        return data


    @classmethod
    def format_auth_ids(cls, auth_ids):
        '''
        格式化权限id

        :param auth_ids:
        :return:
        '''

        if isinstance(auth_ids, str):
            try:
                auth_ids = ast.literal_eval(auth_ids)
            except (ValueError, SyntaxError):
                return auth_ids

        if isinstance(auth_ids, (list, tuple, set)):
            return ','.join(map(str, auth_ids))

        return str(auth_ids)


if __name__ == "__main__":

    file_path = BASE_DIR / "data" / "data.xlsx"

    read = ReadUtil.read_excel_data(file_path)
    print(read)
