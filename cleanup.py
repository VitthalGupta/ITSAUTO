import os
from path import  var_dir, cred_dir
def clean_all():
    os.system("rm -rf " + var_dir)
    os.system("rm -rf " + cred_dir)

def clean_cred():
    os.system("rm -rf " + cred_dir)

def clean_var():
    os.system("rm -rf " + var_dir)

clean_all()