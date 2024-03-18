import time

from progress.counter import Countdown

from global_var import GlbVar,getGlbVarInst
#休眠500毫秒，打印一个字符
def sleepVerbose(seconds:int, title:str ):
    total_ms=seconds*1000
    unit_ms:float=200 #200毫秒
    
    description=f"{title}【{seconds}秒】,slpVbs,"
    countDown:Countdown = Countdown(description,max=total_ms) #Countdown没有参数  suffix='%(percent)d%%'，  Bar才有该参数
    for k in range(0, total_ms, unit_ms):
        countDown.next(unit_ms)#自减1个单位
        # print(".",end="")
        time.sleep(unit_ms/1000)
    
    countDown.finish()