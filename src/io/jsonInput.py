import json


def readJSON(json_file_path):
    json_file = open(json_file_path, 'r')
    return json.load(json_file)


if __name__ == '__main__':
    print readJSON('../../data/gen_hierarchies/SexGH.json')