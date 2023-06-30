import os
##_________Running 2+ funtion in event
def sequence(*functions):
    def func(*args, **kwargs):
        return_value = None
        for function in functions:
            return_value = function(*args, **kwargs)
        return return_value
    return func

def stopAllProcesingToFile(file_path):
    for link in os.listdir(os.path.dirname(file_path)):
        if link.startswith(file_path + "-"):
            os.system("fuser -k " + link)
