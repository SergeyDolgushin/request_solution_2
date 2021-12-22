from pprint import pprint
import requests
from ya_disk import YandexDisk
import os


name = "token_ya_disk.txt"


def check_file_exist(name, path = os.getcwd()):
    '''ищем файл в каталогах, если нашли - возвращаем полный путь + имя'''
    for dir in reversed(path.split("\\")):
         path = os.path.normpath(path + os.sep + os.pardir)
         if name in os.listdir(path):           
            print(path)
            return path + '\\' + name
         else:   
            print("Такого файла не существует")
            return -1             

def read_token_from_file(path_name):
    '''читаем токен из файла'''
    with open(path_name, 'rt', encoding = 'utf-8') as text:
        return text.readline()
    



if __name__ == '__main__':
   
    
    ya = YandexDisk(token=read_token_from_file(check_file_exist("token_ya_disk.txt")))
    responce = ya.create_new_folder("test")
    ya.upload_file_to_disk("test/test.txt", check_file_exist("test.txt"))
    

    