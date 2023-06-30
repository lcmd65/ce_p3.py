import json

def jsonConst():
    with open("backend/const.json") as const:
        json_const_dict = json.load(const)
    return json_const_dict

def jsonChange( key_data, data ):
    with open("backend/const.json", "r+") as const:
        json_const_dict = json.load(const)
        json_const_dict[key_data] = data
        const.seek(0)  # rewind
        json.dump(json_const_dict, const)
        const.truncate()