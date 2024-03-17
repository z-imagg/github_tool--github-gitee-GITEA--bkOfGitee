#!/usr/bin/env python
# -*- coding: utf8 -*-


import typing
import git
from GitPyCloneProgress import GitPyCloneProgressC
from IdUtil import basicUqIdF
from DirUtil import dirIsEmptyExcludeHidden
import traceback

#gitpython获取给定commitId上的tag们（对所有tag进行过滤）
def tagNameLsByCmtId(repo:git.Repo,cmtId:str )->typing.Tuple[str,typing.List[git.Tag]]:
    tagLs:typing.List[git.Tag]=list(filter(lambda tag:tag.commit.hexsha == cmtId,repo.tags))
    tagNmLs:typing.List[str]=[tagK.name  for tagK in tagLs]
    tagNmLsTxt:str= ",".join(tagNmLs)
    return (tagNmLsTxt,tagLs)


#  检查gitee镜像仓库是否能正常克隆
def checkRepoByClone(repoUrl:str,title:str)->git.Repo:
    try:
        dir=f"/tmp/{title}_{basicUqIdF()}"
        repo:git.Repo=git.Repo.clone_from(url=repoUrl,to_path=dir,  progress=GitPyCloneProgressC())
        assert not dirIsEmptyExcludeHidden(dir) , f"断言失败，克隆到的不应该是空仓库. repoUrl=【{repoUrl}】,dir=【{dir}】"
        return repo
    except git.GitCommandError as e:
        print(f"克隆仓库报错. repoUrl=【{repoUrl}】,dir=【{dir}】")
        traceback.print_exception(e)
        raise e
