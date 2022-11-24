import os
from cryptography.fernet import Fernet
import platform

# Get the current working directory
from path import path

# Class defination for credentials
class Credentials():
    def __init__(self):
        self.__username = ""
        self.__key = ""
        self.__password = ""
        self.__key_file = 'key.key'
        self.__time_of_exp = -1

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__key = Fernet.generate_key()
        f = Fernet(self.__key)
        self.__password = f.encrypt(password.encode()).decode()
        del f

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username):
        while (username == ''):
            username = input(
                'Enter a proper User name, blank is not accepted:')
        self.__username = username

    def create_cred(self):
        os.chdir(path)
        cred_file = "cred"
        if os.path.exists(cred_file):
            print("Credentials file already exists")
        else:
            os.mkdir(cred_file)
            os.chdir(cred_file)
            cred_filename = 'CredFile.ini'
            with open(cred_filename, 'w') as file_in:
                file_in.write("#Credential file:\nUsername={}\nPassword={}\n"
                              .format(self.__username, self.__password))
                file_in.write("++"*20)
        #If there exists an older key file, This will remove it.
        if (os.path.exists(self.__key_file)):
            os.remove(self.__key_file)
        #Open the Key.key file and place the key in it.
        #The key file is hidden.
        try:
            os_name = platform.system()
            # creating the key file
            with open(self.__key_file, 'w') as key_in:
                key_in.write(self.__key.decode())
            # Hiding the key file
            if (os_name == "Windows"):
                os.system("attrib +h key.key")
            elif (os_name == "Linux"):
                os.system("mv key.key .key.key")
            elif (os_name == "Darwin"):
                os.system("setfile -a V key.key")

        except PermissionError as e:
            print("Permission denied to hide the key file")
            print("Please run the program as an administrator")

        self.__username = ""
        self.__password = ""
        self.__key = ""
        self.__key_file
