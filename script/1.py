from urllib import response

from pytest import fail
import yaml
import config

def read_yaml(path):
    '''
    读取yaml文件
    '''
    with open(path, encoding='utf-8') as file:
        # data = yaml.safe_load(file)
        pass


    return fail


print(read_yaml(config.BASE_DIR / 'data' / 'data.yaml'))
