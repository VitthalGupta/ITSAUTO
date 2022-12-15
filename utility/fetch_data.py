from path import path, var_dir
import os
import re

# The data restured by this fuction is a string, for fetching integer values change the type to int
def fetch_var(var):
    os.chdir(var_dir)
    var_file = open("var.txt", "r")
    var_file_data = var_file.read()
    var_file.close()
    var = re.search(var + " : (.*)", var_file_data)
    var = var.group(1)
    os.chdir(path)
    return var