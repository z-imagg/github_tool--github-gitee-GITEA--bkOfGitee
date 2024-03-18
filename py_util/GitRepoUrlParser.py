#!/usr/bin/env python
# -*- coding: <encoding name> -*-

# 【文件作用】 工具类 解析形如 https://github.com/NVlabs/stylegan.git 具有两层路径 的git仓库地址 

_GIT=".git"

class GitRepoUrlC:
    def __init__(self,baseUrl:str,orgName:str,repoName:str) -> None:
        self.baseUrl:str=baseUrl #TODO host--> baseUrl
        self.orgName:str=orgName
        self.repoName:str=repoName
    
    def url_str(self):
        return f"{self.baseUrl}/{self.orgName}/{self.repoName}.git"
    
    def to_mirror_url(self,mirrorBaseUrl:str,mirrorOrg:str):
        that=GitRepoUrlC(None,None,None)
        that.baseUrl=mirrorBaseUrl
        that.orgName=mirrorOrg
        that.repoName=f"{self.orgName}--{self.repoName}"
        return that


import re
#                           //host/org /repo
GitRepoUrlReExpr=r"(http[s]?://.+)/(.+)/(.+)\.git"

def gitRepoUrlParseF(repoUrl:str) -> GitRepoUrlC:
    # print(f"{repoK.name}, {repoK.path}, {repoK.url}, {repoK.hexsha}, {repoK.branch_name}, {repoK.branch_path}")
    repoUrl=repoUrl if repoUrl.endswith(_GIT) else f"{repoUrl}{_GIT}"
    urlMatch=re.match(pattern=GitRepoUrlReExpr,string=repoUrl)
    assert urlMatch is not None,f"断言失败，【{repoUrl}】不匹配正则表达式【{GitRepoUrlReExpr}】【忽略末尾.git】"
    urlFieldLs=urlMatch.groups()
    assert urlFieldLs is not None and len(urlFieldLs) == 3 ,f"断言失败，【{repoUrl}】不匹配正则表达式【{GitRepoUrlReExpr}】【忽略末尾.git】，字段个数不为3，实际字段个数【{len(urlFieldLs)}】"
    baseUrl=urlFieldLs[0]
    org=urlFieldLs[1]
    repo=urlFieldLs[2]
    return GitRepoUrlC(baseUrl,org,repo)


class GitMirrorRepoUrlC:
    def __init__(self,host:str,mirrorOrgName:str,orgName:str,repoName:str) -> None:
        self.baseUrl:str=host
        self.mirrorOrgName:str=mirrorOrgName
        self.orgName:str=orgName
        self.repoName:str=repoName


#                                 //host/mrrOrg/org--repo
GitMirrorRepoUrlReExpr=r"(http[s]?://.+)/(.+)/(.+)--(.+)\.git"
def gitMirrorRepoUrlParseF(repoUrl:str)->GitMirrorRepoUrlC:
  repoUrl=repoUrl if repoUrl.endswith(_GIT) else f"{repoUrl}{_GIT}"
  urlMatch=re.match(pattern=GitMirrorRepoUrlReExpr,string=repoUrl)
  assert urlMatch is not None,f"断言失败，【{repoUrl}】不匹配正则表达式【{GitMirrorRepoUrlReExpr}】【忽略末尾.git】"
  urlFieldLs=urlMatch.groups()
  assert urlFieldLs is not None and len(urlFieldLs) == 4 ,f"断言失败，【{repoUrl}】不匹配正则表达式【{GitMirrorRepoUrlReExpr}】【忽略末尾.git】，字段个数不为4，实际字段个数【{len(urlFieldLs)}】"
  baseUrl=urlFieldLs[0]
  _mirrorOrg=urlFieldLs[1]
  org=urlFieldLs[2]
  repo=urlFieldLs[3]
  return GitMirrorRepoUrlC(baseUrl,_mirrorOrg,org,repo)