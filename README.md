# 随机文件及目录选择器
> 主要满足了我自己的随机看片需求

有什么用:从一堆电影中随机选出x个并复制进指定文件夹
* 请安装psutil和tqdm
```bash
pip3 install psutil
```
### ver_0.1
可以切换磁盘了!

~~现在不知道什么时候复制完成，下一步准备用os.path.getsize(filePath)+threading来完成~~

### ver_0.2
现在复制完成之后会输出DONE

### ver_0.3
现在支持命令行参数使用

* 一个参数
```bash
python3 randomMovieChose source_path
```
* 两个参数
```bash
python3 randomMovieChose source_path target_path
```

* 三个参数
```bash
python3 randomMovieChose source_path target_path file_num
```