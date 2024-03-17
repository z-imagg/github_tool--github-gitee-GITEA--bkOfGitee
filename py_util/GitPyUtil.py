#!/usr/bin/env python
# -*- coding: utf8 -*-


import git
import typing

#gitpython获取给定commitId上的tag们（对所有tag进行过滤）
def tagNameLsByCmtId(repo:git.Repo,cmtId:str )->typing.Tuple[str,typing.List[git.Tag]]:
    tagLs:typing.List[git.Tag]=list(filter(lambda tag:tag.commit.hexsha == cmtId,repo.tags))
    tagNmLs:typing.List[str]=[tagK.tag.tag  for tagK in tagLs]
    tagNmLsTxt:str= ",".join(tagLs)
    return (tagNmLsTxt,tagLs)