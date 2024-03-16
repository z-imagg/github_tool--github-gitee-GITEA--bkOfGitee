#!/usr/bin/env python
# -*- coding: <encoding name> -*-

# 【文件作用】 import_githubRepo_to_gitee.sh 包装
from pathlib import Path
from shell import shell

import json

from IdUtil import basicUqIdF


class SimpleRespI:
    def __init__(self,url:str,reqBody:str,reqHeaders:str,respStatus:int,respBody:str,respHeaders:str,goal_repoUrl:str) -> None:
        self.url:str=url
        self.reqBody:str=reqBody
        self.reqHeaders:str=reqHeaders
        self.respStatus:int=respStatus
        self.respBody:str=respBody
        self.respHeaders:str=respHeaders
        self.goal_repoUrl:str=goal_repoUrl

def gitee_import_repo_wrap_F(fromRepoUrl:str,mirrOrg:str,newRepoName:str)->SimpleRespI:
    resultFP:str=f"/tmp/import_result_{basicUqIdF()}.json"
    cmd_import2gitee=f"import_githubRepo_to_gitee.sh --from_repo {fromRepoUrl}  --goal_org {mirrOrg}  --goal_repoPath {newRepoName} --goal_repoName {newRepoName}  --goal_repoDesc 【镜像】{fromRepoUrl} --write_return {resultFP}"
    shl=shell(cmd_import2gitee)
    assert shl.code == 0, f"断言失败，命令执行返回代码不为0 ，{shl.code}, {cmd_import2gitee}"
    jsonText:str=Path(resultFP).read_text()
    simplRespI:SimpleRespI=json.loads(s=jsonText,cls=SimpleRespI)
    return simplRespI