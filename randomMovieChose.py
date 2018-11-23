import os
import random
import shutil
import psutil
import threading
import time

'''
这个python程序会从一堆电影中随机选出x个并复制进指定文件夹
用于片子太多无法选择的情况
'''


def pocessStatus(source_path,file,target_path):
    sourceFile = os.path.join(source_path,file)
    targetFile = os.path.join(target_path,file)
    sourceSize = os.path.getsize(sourceFile)
    targetSize = os.path.getsize(targetFile)
    t = time.clock()
    percent = 0.0
    if sourceSize == 0:
        print("{} Done\n".format(file))
        return
    while percent != 100:
        percent = (targetSize/sourceSize) * 100
        percent = int(percent)
        scale = percent//5
        a = '*' * scale
        b = '.' * (20 - scale)
        c = percent
        t -= time.clock()
        print("\r{}{:^3.0f}%[{}->{}]{:.2f}s".format(file,c,a,b,-t),end='\n')
        time.sleep(0.05)

    # pbar = tqdm(desc = file,total = 100)
    # percent = 0
    # if(sourceSize == 0):
    #     pbar.update(100)
    #     pbar.close()
    #     return True
    # while(percent != 1):
    #     time.sleep(0.02)
    #     percent = targetSize/sourceSize
    #     int(percent)
    #     pbar.update = (percent*100)
    #     sourceSize = os.path.getsize(sourceFile)
    #     targetSize = os.path.getsize(targetFile)
    # pbar.close()

def copy_and_paste_single_file(source_path,file,target_path):
    if os.path.isfile(os.path.join(source_path,file)) == True:
        sourceFile = os.path.join(source_path,  file)
        targetFile = os.path.join(target_path,  file)
        shutil.copy(sourceFile,targetFile)
    elif os.path.isdir(os.path.join(source_path,file)) == True:
        sourceFile = os.path.join(source_path,  file)
        targetFile = os.path.join(target_path,  file)
        shutil.copytree(sourceFile,targetFile)

def copy_and_paste(source_path,fileList,target_path):
    for file in fileList:
        if os.path.isfile(os.path.join(source_path,file)) == True:
            sourceFile = os.path.join(source_path,  file)
            targetFile = os.path.join(target_path,  file)
            shutil.copy(sourceFile,targetFile)
        elif os.path.isdir(os.path.join(source_path,file)) == True:
            sourceFile = os.path.join(source_path,  file)
            targetFile = os.path.join(target_path,  file)
            shutil.copytree(sourceFile,targetFile)


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
        input 'd' to change disk dir \n
        '''
        )
        if choose == 'n':
            make_new_dir()
        elif choose == 'y':
            return os.getcwd()
        elif choose == 'u':
            changePath = os.path.join('.','..')
            os.chdir(changePath)
        elif choose == 'd':
            change_disk()
        else :
            sPath = dirList[int(choose)]
            #print(sPath)
            changePath = os.path.join('.',sPath)
            os.chdir(changePath)

def change_disk():
    disk_list = psutil.disk_partitions()
    num = len(disk_list)
    for i in range(num):
        print("{} {}".format(i,disk_list[i].mountpoint))
    change = input('please input the num \n')
    change = eval(change)
    os.chdir(disk_list[change].mountpoint)


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

def get_random_file(dirList):
    x = input('你今天想看多少片 \n')
    x = int(x)
    filelist = []
    num = []
    while len(num) < x:
        ind = random.randint(0,len(dirList)-1)
        if ind in num:
            continue
        elif ind not in num:
            num.append(ind)
            filelist.append(dirList[ind])
    print(filelist)
    return filelist

def main():
    print('choose source path ')
    source_path = get_path()
    dirList = get_file_and_dir_list(source_path)
    output_the_path(dirList)
    fileList = get_random_file(dirList)
    print('choose target path ')
    target_path = get_path()
    for file in fileList:
        t_copy = threading.Thread(copy_and_paste_single_file(source_path,file,target_path))
        t_status = threading.Thread(pocessStatus(source_path,file,target_path))
        t_status.start()
        t_copy.start()
        
if __name__ == '__main__':
    main()
