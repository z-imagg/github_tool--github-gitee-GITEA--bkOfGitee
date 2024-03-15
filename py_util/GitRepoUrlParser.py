#!/usr/bin/env python
# -*- coding: <encoding name> -*-

# 【文件作用】 工具类 解析形如 https://github.com/NVlabs/stylegan.git 具有两层路径 的git仓库地址 


class GitRepoUrlC:
    def __init__(self,host:str,orgName:str,repoName:str) -> None:
        self.host:str=host #TODO host--> baseUrl
        self.orgName:str=orgName
        self.repoName:str=repoName
    
    def url_str(self):
        return f"https://{self.host}/{self.orgName}/{self.repoName}.git"


import re
#                           //host/org /repo
GitRepoUrlReExpr=r"http[s]?://(.+)/(.+)/(.+)\.git"

def gitRepoUrlParseF(repoUrl:str) -> GitRepoUrlC:
    _GIT=".git"
    # print(f"{repoK.name}, {repoK.path}, {repoK.url}, {repoK.hexsha}, {repoK.branch_name}, {repoK.branch_path}")
    repoUrl=repoUrl if repoUrl.endswith(_GIT) else f"{repoUrl}{_GIT}"
    urlMatch=re.match(pattern=GitRepoUrlReExpr,string=repoUrl)
    assert urlMatch is not None,f"断言失败，【{repoUrl}】不匹配正则表达式【{GitRepoUrlReExpr}】【忽略末尾.git】"
    urlFieldLs=urlMatch.groups()
    assert urlFieldLs is not None and len(urlFieldLs) == 3 ,f"断言失败，【{repoUrl}】不匹配正则表达式【{GitRepoUrlReExpr}】【忽略末尾.git】，字段个数不为3，实际字段个数【{len(urlFieldLs)}】"
    host=urlFieldLs[0]
    orgName=urlFieldLs[1]
    repoName=urlFieldLs[2]
    return GitRepoUrlC(host,orgName,repoName)


class GitMirrorRepoUrlC:
    def __init__(self,host:str,mirrorOrgName:str,orgName:str,repoName:str) -> None:
        self.host:str=host
        self.mirrorOrgName:str=mirrorOrgName
        self.orgName:str=orgName
        self.repoName:str=repoName


#                                 //host/mrrOrg/org--repo
GitMirrorRepoUrlReExpr=r"http[s]?://(.+)/(.+)/(.+)--(.+)\.git"
def gitMirrorRepoUrlParseF(repoUrl:str)->GitMirrorRepoUrlC:
  _GIT=".git"
  repoUrl=repoUrl if repoUrl.endswith(_GIT) else f"{repoUrl}{_GIT}"
  urlMatch=re.match(pattern=GitMirrorRepoUrlReExpr,string=repoUrl)
  assert urlMatch is not None,f"断言失败，【{repoUrl}】不匹配正则表达式【{GitMirrorRepoUrlReExpr}】【忽略末尾.git】"
  urlFieldLs=urlMatch.groups()
  assert urlFieldLs is not None and len(urlFieldLs) == 4 ,f"断言失败，【{repoUrl}】不匹配正则表达式【{GitMirrorRepoUrlReExpr}】【忽略末尾.git】，字段个数不为4，实际字段个数【{len(urlFieldLs)}】"
  giteaHost=urlFieldLs[0]
  _mirrorOrgName=urlFieldLs[1]
  orgName=urlFieldLs[2]
  repoName=urlFieldLs[3]
  return GitMirrorRepoUrlC(giteaHost,_mirrorOrgName,orgName,repoName)