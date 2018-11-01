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
        print(os.getcwd())
        print('\n')
        dirList = get_dir_list('.')
        output_the_path(dirList)
        choose = input('''
        please input the number that you want to chose \n 
        input 'n' to make new dir \n 
        input 'y' to choose the dir \n 
        input 'u' to back parent dir \n
        '''
        )
        if choose == 'n':
            make_new_dir()
        elif choose == 'y':
            return os.getcwd()
        elif choose == 'u':
            changePath = os.path.join('.','..')
            os.chdir(changePath)
        else :
            sPath = dirList[int(choose)]
            #print(sPath)
            changePath = os.path.join('.',sPath)
            os.chdir(changePath)

def get_dir_list(Path):
    dir_list = []
    dir_originlist = get_file_and_dir_list(Path)
    for v in dir_originlist:
        if os.path.isdir(os.path.join('.',v)) == True:
            dir_list.append(v)
    return dir_list


def get_file_and_dir_list(Path):
    os.chdir(Path)
    dirandfileList = os.listdir(Path)
    #dirandfileDict = dict(dirandfileList)
    return dirandfileList

def output_the_path(dirList):
    #dirDict_ = {k:dirList[k] for k in len(dirList)}
    for i in range(len(dirList)):
        print('{}  {}'.format(i,dirList[i]))

def make_new_dir():
    os.chdir('.')
    name = input('input the new dir name \n')
    os.mkdir(name,777)

def copy_and_paste(fileList,destinationPath):
    pass

def get_random_file(dirList):
    x = input('你今天想看多少片 \n')
    x = int(x)
    filelist = []
    num = []
    while len(num) <= x:
        ind = random.randint(0,len(dirList))
        if ind in num:
            continue
        elif ind not in num:
            num.append(ind)
            filelist.append(os.path.join(os.getcwd(),dirList[ind]))
    return filelist
  

def main():
    print('get source path \n')
    source_path = get_path()
    dirList = get_file_and_dir_list(source_path)
    output_the_path(dirList)

main()
