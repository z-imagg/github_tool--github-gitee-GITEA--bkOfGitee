import httpx
import typing

def httpx_post_json(apiUrl:str,reqBodyDct:typing.Dict,timeoutSecs:int=5)->httpx.Response:
  try:
    resp:httpx.Response=httpx.post(url=apiUrl,json=reqBodyDct,verify=False,timeout=timeoutSecs)
    return resp
  except ConnectionRefusedError as cre:
    print(f"【疑似服务没开启】{apiUrl}")
    raise cre