
import httpx
import typing
import traceback

def httpx_post_json(apiUrl:str,reqBodyDct:typing.Dict,timeoutSecs:int=5)->httpx.Response:
  try:
    resp:httpx.Response=httpx.post(url=apiUrl,json=reqBodyDct,verify=False,timeout=timeoutSecs)
    return resp
  except (httpx.ConnectError) as cre:
    print(f"【疑似服务没开启】{apiUrl}")
    traceback.print_exception(cre)
    raise cre
  except (Exception) as exp:
    #开发调试用
    print(f"【其他异常】{apiUrl}")
    traceback.print_exception(exp)
    raise exp