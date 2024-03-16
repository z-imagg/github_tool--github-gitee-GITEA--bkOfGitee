
#无with测试 https://github.com/rsalmei/alive-progress  正常 

#with参考:  https://blog.csdn.net/Shiroh_ms08/article/details/53859475
from alive_progress import alive_bar
bar=alive_bar(100, manual=True)
bar.__enter__()
bar(20)
bar(40)
bar.__exit__(None,None,None)