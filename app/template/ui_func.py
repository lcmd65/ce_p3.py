import os
import gc
import meta.external_var
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

def collectGarbage():
    if meta.external_var.root != None:
        meta.external_var.root.after(10000, sequence(gc.collect()))