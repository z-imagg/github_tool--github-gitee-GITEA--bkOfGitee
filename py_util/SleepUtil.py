import time


#休眠500毫秒，打印一个字符
def sleepVerbose(seconds:int, z:str ):
    unit_ms:float=0.5 #500毫秒
    for k in range(0, int(seconds//unit_ms)):
        print(z,end="")
        time.sleep(seconds)