import json


def json_to_dict(file_name):
    with open(file=file_name, mode="r") as file:
        json_file = json.load(file)
        return json_file
