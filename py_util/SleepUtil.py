import time



from global_var import GlbVar,getGlbVarInst
#休眠500毫秒，打印一个字符
def sleepVerbose(seconds:int, title:str ):
    oneUnit_ms:float=0.5 #500毫秒
    unitCnt=int(seconds//oneUnit_ms)
    
    for k in getGlbVarInst().richPrgrs.track(sequence= range(0, unitCnt),description=f"{title}【{seconds}秒】" ):
        # print(z,end="")
        time.sleep(oneUnit_ms)