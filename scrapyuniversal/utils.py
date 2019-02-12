from os.path import realpath, dirname
import json


def get_config(name):
    path = dirname(realpath(__file__)) + '/configs/' + name + '.json'
    with open(path, 'r', encoding='utf-8') as f:
        return json.loads(f.read())


if __name__ == '__main__':
    print(__file__)
    # print(__file__)
    print(realpath(__file__))
    print(dirname(realpath(__file__)))