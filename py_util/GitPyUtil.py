#!/usr/bin/env python
# -*- coding: utf8 -*-


import typing
import git
from CntUtil import Counter
from GitPyCloneProgress import GitPyCloneProgressC
from IdUtil import basicUqIdF
from DirUtil import dirIsEmptyExcludeHidden
import traceback

from urllib.parse import urlparse

from MiscUtil import firstLine
from global_var import GlbVar,getGlbVarInst

#gitpython获取给定commitId上的tag们（对所有tag进行过滤）
def tagNameLsByCmtId(repo:git.Repo,cmtId:str )->typing.Tuple[str,typing.List[git.Tag]]:
    tagLs:typing.List[git.Tag]=list(filter(lambda tag:tag.commit.hexsha == cmtId,repo.tags))
    tagNmLs:typing.List[str]=[tagK.name  for tagK in tagLs]
    tagNmLsTxt:str= ",".join(tagNmLs)
    return (tagNmLsTxt,tagLs)

#问题，当gitee某url仓库不存在时，若克隆其，则要求输入用户名密码，此时程序被卡住了。
#  解决办法是 在url上 添加 站位用户名、站位密码， 当仓库不存在时，直接报错，不会卡住。
# 利用urlparse给仓库url 添加 站位用户名、站位密码
def repoUrlAddUserPass(repoUrl:str)->str:
    usr="usr"
    pwd="123"
    uo=urlparse(url=repoUrl)
    newUrl=f"{uo.scheme}://{usr}:{pwd}@{uo.netloc}{uo.path}"
    return newUrl

#  检查gitee镜像仓库是否能正常克隆
def checkRepoByClone(_repoUrl:str,title:str)->git.Repo:
    #给仓库url添加 站位用户名、站位密码，防止当仓库不存在时本程序被gitpython要求输入用户名密码而卡住
    repoUrl=repoUrlAddUserPass(_repoUrl)
    
    try:
        progressTitle=f"{title}:{repoUrl}"
        dir=f"/tmp/{title}_{basicUqIdF()}"
        repo:git.Repo=git.Repo.clone_from(url=repoUrl,to_path=dir,  progress=GitPyCloneProgressC(progressTitle))
        assert not dirIsEmptyExcludeHidden(dir) , f"{title},断言失败，克隆到的不应该是空仓库. repoUrl=【{repoUrl}】,dir=【{dir}】"
        return repo
    except git.GitCommandError as e:
        print(f"{title},克隆仓库报错,请检查该仓库是否存在?忘记执行RepoRecurseImport.py导入了?. repoUrl=【{repoUrl}】,dir=【{dir}】")
        traceback.print_exception(e)
        raise e




def printFrmRepoMsg(from_repo_url:str, from_commit_id:str, repo:git.Repo,cntr:Counter)->str:
    
    idxMsg=f"第{cntr.inc()}个仓库 "

    cmtIdMsg=f"提交id【{from_commit_id}】"

    subNmLs=", ".join([son.url for son in repo.submodules])
    subRpLsTxt=f"有子仓库{len(repo.submodules)}个=【{subNmLs}】" if len(repo.submodules)>0 else "无子仓库"
    
    tagNmLsTxt,tagLnLs=tagNameLsByCmtId(repo,from_commit_id)
    tagTxt:str=f"tag们【{tagNmLsTxt}】" if len(tagLnLs)>0 else "无tag"

    cmtMsg=firstLine(repo.commit(from_commit_id).message)
    cmtMsgDisplay=f"提交消息【{cmtMsg}】"
    
    print(f"{idxMsg}【{from_repo_url}】，{cmtIdMsg}，  {tagTxt}，  {subRpLsTxt}  ，{cmtMsgDisplay}")
    