import os
import re
from path import path, var_dir

# function to update the variable file
def update_var(var_name, var_value):
    os.chdir(var_dir)
    var_file = open("var.txt", "r")
    var_file_data = var_file.read()
    var_file.close()
    var_file_data = re.sub(var_name, var_value, var_file_data)
    var_file = open("var.txt", "w")
    var_file.write(var_file_data)
    var_file.close()
    os.chdir(path)