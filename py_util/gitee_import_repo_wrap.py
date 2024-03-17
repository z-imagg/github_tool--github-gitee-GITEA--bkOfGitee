#!/usr/bin/env python
# -*- coding: <encoding name> -*-

# 【文件作用】 import_githubRepo_to_gitee.sh 包装
from pathlib import Path
from shell import shell

import json

from IdUtil import basicUqIdF


class SimpleRespI:
    url:str
    reqBody:str
    reqHeaders:str
    respStatus:int
    respBody:str
    respHeaders:str
    goal_repoUrl:str

    # def __init__(self,url:str,reqBody:str,reqHeaders:str,respStatus:int,respBody:str,respHeaders:str,goal_repoUrl:str) -> None:
    def __init__(self ) -> None:
        pass

    @staticmethod
    def __fill__(url:str,reqBody:str,reqHeaders:str,respStatus:int,respBody:str,respHeaders:str,goal_repoUrl:str) -> None:
        thiz=SimpleRespI()
        thiz.url:str=url
        thiz.reqBody:str=reqBody
        thiz.reqHeaders:str=reqHeaders
        thiz.respStatus:int=respStatus
        thiz.respBody:str=respBody
        thiz.respHeaders:str=respHeaders
        thiz.goal_repoUrl:str=goal_repoUrl
        return thiz
    def from_dict(d):
        return SimpleRespI.__fill__(d['url'],d['reqBody'],d['reqHeaders'],d['respStatus'],d['respBody'],d['respHeaders'],d['goal_repoUrl'])
        
def gitee_import_repo_wrap_F(prjHmDir:str,fromRepoUrl:str,mirrOrg:str,newRepoName:str)->SimpleRespI:
    resultFP:str=f"/tmp/import_result_{basicUqIdF()}.json"
    cmd_import2gitee=f"{prjHmDir}/gitee_api_fetch_ts/script/import_githubRepo_to_gitee.sh --from_repo {fromRepoUrl}  --goal_org {mirrOrg}  --goal_repoPath {newRepoName} --goal_repoName {newRepoName}  --goal_repoDesc 【镜像】{fromRepoUrl} --write_return {resultFP}"
    shl=shell(cmd_import2gitee)
    assert shl.code == 0, f"断言失败，命令执行返回代码不为0 ，{shl.code}, {cmd_import2gitee}"
    jsonText:str=Path(resultFP).read_text()
    simplRespI:SimpleRespI=json.loads(s=jsonText,object_hook=SimpleRespI.from_dict)
    return simplRespI