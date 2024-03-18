import time

from progress.counter import Countdown

from global_var import GlbVar,getGlbVarInst
#休眠500毫秒，打印一个字符
def sleepVerbose(seconds:int, title:str ):
    oneUnit_ms:float=0.2 #200毫秒
    unitCnt=int(seconds//oneUnit_ms)

    
    description=f"{title}【{seconds}秒】,slpVbs,"
    countDown:Countdown = Countdown(description,max=unitCnt)
    for k in range(0, unitCnt):
        countDown.next(1)#自减1
        # print(".",end="")
        time.sleep(oneUnit_ms)