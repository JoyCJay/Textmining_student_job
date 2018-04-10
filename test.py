import os

def file_name(file_dir):
    for root, dirs,files in os.walk(file_dir):
        for i in files:
            print(i) #当前路径下所有非目录子文件
file_name("./Sample")
'''
for files in os.walk("./Sample"):
    for i in files:
        print(i) #当前路径下所有非目录子文件
'''
