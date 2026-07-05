import ast
import pandas as pd
from common import project_root


class ReadUtil:
    '''
    读取excel文件
    '''

    @classmethod
    def read_file(cls, file_path):
        '''
        读取excel文件
        :param file_path: 文件路径
        :return: DataFrame
        '''
        df = pd.read_excel(file_path)
        return df
    
    @classmethod
    def format_auth_ids(cls, auth_ids):
        if isinstance(auth_ids, str):
            try:
                auth_ids = ast.literal_eval(auth_ids)
            except (ValueError, SyntaxError):
                return auth_ids

        if isinstance(auth_ids, (list, tuple, set)):
            return ','.join(map(str, auth_ids))

        return str(auth_ids)


if __name__ == "__main__":

    file_path = project_root.get_project_root() / 'data' / 'data.xlsx'

    read = ReadUtil.read_file(file_path)
    print(read)
