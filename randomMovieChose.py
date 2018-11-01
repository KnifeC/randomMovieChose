import os
import random
'''
这个python程序会从一堆电影中随机选出x个并复制进指定文件夹
用于片子太多无法选择的情况
将这个文件放在电影目录的上一级目录使用
'''
def get_source_path():
    sPath = input('please input the dir name that have movie you want to chose')
    sourcePath = os.path.join('.','sPath')
    return sourcePath

def get_file_and_dir_dict(Path):
    os.chdir(Path)
    dirList = os.listdir(Path)
    dirDict = dict(dirList)
    return dirDict


def output_the_path(dirDict):
    #dirDict_ = {k:dirList[k] for k in len(dirList)}
    for i in dirDict:
        print(i) 
        print('\n')
    

def make_new_dir():
    name = input('input the new dir name')
    os.mkdir(name)

def copy_and_paste():
    pass

def get_random_index(num):
    x = eval(input('你今天想看多少片'))
    back = []
    i=1
    while len(back) <= x
        ind = random.randint(0,num)
        if ind in back:
            continue
        elif ind not in back:
            back.append(ind)
    return back
            

def main():
    self_path = get_source_path()
    dirDict = get_file_and_dir_dict(self_path)
    output_the_path(dirDict)

main()