#!/usr/bin/env python
# -*- coding: utf8 -*-



# 【术语】 SngltAnnt == SingletonAnnotation == 单例注解

#参考: https://blog.csdn.net/chenyongfa188/article/details/105612341

#Python 装饰器线程安全单例的实现(使用函数装饰器)
import threading
import time
def SngltAnnt(cls):
    instance = {}
    lock = threading.Lock()

    def __single_with_thread_lock(*args,**kwargs):
        print("lock" + str(lock))
        if cls not in instance:
            with lock:
                if cls not in instance:
                    instance[cls] = cls(*args,**kwargs)
        return instance[cls]
    return __single_with_thread_lock

@SngltAnnt
class __C000__():
    def __init__(self):
        time.sleep(2)

def printNewInstance():
    print(__C000__())



#以下是测试单例模式
if __name__=="__main__":
    for i in range(20):
        threading.Thread(target=printNewInstance).start()
    
