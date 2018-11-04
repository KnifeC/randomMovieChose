# 随机文件及目录选择器
> 主要满足了我自己的随机看片需求

有什么用:从一堆电影中随机选出x个并复制进指定文件夹
* 请安装psutil
```
pip3 install psutil
```
可以切换磁盘了!

现在不知道什么时候复制完成，下一步准备用os.path.getsize(filePath)+threading来完成