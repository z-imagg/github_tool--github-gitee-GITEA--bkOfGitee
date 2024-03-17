import httpx
import typing

def httpx_post_json(apiUrl:str,reqBodyDct:typing.Dict,timeoutSecs:int=5)->httpx.Response:
  try:
    resp:httpx.Response=httpx.post(url=apiUrl,json=reqBodyDct,verify=False,timeout=timeoutSecs)
    return resp
  except (httpx.ConnectError) as cre:
    print(f"【疑似服务没开启】{apiUrl}")
    raise cre
  except (Exception) as exp:
    #开发调试用
    print(f"【其他异常】{apiUrl}")
    import traceback
    traceback.print_exception(exp)
    raise exp