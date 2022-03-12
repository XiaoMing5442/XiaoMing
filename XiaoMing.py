# 导包
import os
import shutil
import random

def delete(path) -> str:# 用来删除文件及文件夹
    if os.path.isdir(path):
        shutil.rmtree(path)
    else:
        os.remove(path)

def random_list_select(LiSt,number) -> list|int:# 随机选取LiSt中的number个元素组成一个新列表
    New_LiSt = []
    for i in range(number):
        element = LiSt[random.randint(0,len(LiSt)-1)]
        New_LiSt.append(element)
    return New_LiSt






