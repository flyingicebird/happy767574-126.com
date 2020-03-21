# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 15:37:58 2020

@author: 以马内利
@describe: 用来在网上下载最新的疫情数据，下载到本地后再处理
"""

#从网络上下载疫情数据

url = 'https://raw.githubusercontent.com/BlankerL/DXY-2019-nCoV-Data/master/csv/DXYArea.csv'
 #保存网络数据文件到本地
import urllib.request
# 下载文件进度展示
def Schedule(blocknum, blocksize, totalsize):
    '''进度函数
    @blocknum: 已经下载的数据块
    @blocksize: 数据块的大小
    @totalsize: 远程文件的大小
    '''
    percent = 100.0 * blocknum * blocksize / totalsize
    if percent > 100:
        percent = 100
        print('完成！')
    print ("%.2f%%"% percent)

# 需要包含请求头，因为有的网站会检查
opener = urllib.request.build_opener()
opener.addheaders = [('User-Agent',
                      'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36')]
urllib.request.install_opener(opener)

# 下面是防止下载中断或者下载进入死循环
import socket
#设置超时时间为30s
socket.setdefaulttimeout(30)
#解决下载不完全问题且避免陷入死循环
try:
    urllib.request.urlretrieve(url,"DXYArea.csv",Schedule)
except socket.timeout:
    count = 1
    while count <= 5:
        try:
            urllib.request.urlretrieve(url,"DXYArea.csv",Schedule)                                              
            break
        except socket.timeout:
            err_info = 'Reloading for %d time'%count if count == 1 else 'Reloading for %d times'%count
            print(err_info)
            count += 1
    if count > 5:
        print("downloading file failed!")