import os
import random
import shutil
'''
这个python程序会从一堆电影中随机选出x个并复制进指定文件夹
用于片子太多无法选择的情况
'''
def get_path():
    choose = True
    while choose != 'y':
        print(os.getcwd)
        print('\n')
        dirDict = get_file_and_dir_dict('.')
        output_the_path(dirDict)
        choose = input('''
        please input the number that you want to chose \n 
        input '-1' to make new dir \n 
        input 'y' to choose the dir \n 
        input 'u' to back parent dir \n
        '''
        )
        if choose == '-1':
            make_new_dir()
        elif choose == 'y':
            sPath = dirDict[int(choose)]
            changePath = os.path.join('.','sPath')
            os.chdir(changePath)
            return changePath
        elif choose == 'u':
            changePath = os.path.join('.','..')
            os.chdir(changePath)
        else :
            sPath = dirDict[int(choose)]
            changePath = os.path.join('.','sPath')
            os.chdir(changePath)

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
    os.chdir('.')
    name = input('input the new dir name \n')
    os.mkdir(name,777)

def copy_and_paste(fileList,destinationPath):
    pass

def get_random_index(num):
    x = input('你今天想看多少片 \n')
    x = int(x)
    back = []
    while len(back) <= x:
        ind = random.randint(0,num)
        if ind in back:
            continue
        elif ind not in back:
            back.append(ind)
    return back
            

def main():
    print('get source path \n')
    source_path = get_path()
    dirDict = get_file_and_dir_dict(source_path)
    output_the_path(dirDict)

main()
