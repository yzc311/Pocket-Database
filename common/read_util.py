import pandas as pd
import project_root


class ReadUtil:

    @classmethod
    def read_file(cls, file_path):
        df = pd.read_excel(file_path)
        return df


if __name__ == "__main__":

    file_path = project_root.get_project_root() / 'data' / 'data.xlsx'

    read = ReadUtil.read_file(file_path)
    print(read)