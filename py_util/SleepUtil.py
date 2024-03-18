import time

from rich.progress import track

from rich import print

from global_var import GlbVar
#休眠500毫秒，打印一个字符
def sleepVerbose(seconds:int, z:str ):
    oneUnit_ms:float=0.5 #500毫秒
    unitCnt=int(seconds//oneUnit_ms)
    
    # 全局只能有一个 rich.progress.Progress的实例，
    # 所以  这里必须要写 richPrgrs.track, 而直接写track, 否则会报错  " rich.errors.LiveError: Only one live display may be active at once ", 
    for k in GlbVar.getInst().richPrgrs.track(sequence= range(0, unitCnt),description="休眠中" ):
        # print(z,end="")
        time.sleep(oneUnit_ms)