import time



from global_var import GlbVar,getGlbVarInst
#休眠500毫秒，打印一个字符
def sleepVerbose(seconds:int, title:str ):
    oneUnit_ms:float=0.5 #500毫秒
    unitCnt=int(seconds//oneUnit_ms)
    
    description=f"{title}【{seconds}秒】"
    for k in range(0, unitCnt):
        print(".",end="")
        time.sleep(oneUnit_ms)