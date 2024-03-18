#!/usr/bin/env python
# -*- coding: utf8 -*-


import typing
import git
from GitPyCloneProgress import GitPyCloneProgressC
from IdUtil import basicUqIdF
from DirUtil import dirIsEmptyExcludeHidden
import traceback

from urllib.parse import urlparse
from rich.progress import Progress

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
        repo:git.Repo=git.Repo.clone_from(url=repoUrl,to_path=dir,  progress=GitPyCloneProgressC(progressTitle,getGlbVarInst().richPrgrs))
        assert not dirIsEmptyExcludeHidden(dir) , f"{title},断言失败，克隆到的不应该是空仓库. repoUrl=【{repoUrl}】,dir=【{dir}】"
        return repo
    except git.GitCommandError as e:
        print(f"{title},克隆仓库报错,请检查该仓库是否存在. repoUrl=【{repoUrl}】,dir=【{dir}】")
        traceback.print_exception(e)
        raise e
