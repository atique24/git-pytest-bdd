import json


def json_to_list(file_name):
    with open(file=file_name,mode="r") as file:
        json_file = json.load(file)
        new_list = []
        for i in range(0, len(json_file)):
            new_list.append(list(json_file[i].values()))

    return new_list

