#!/usr/bin/env python
# -*- coding: utf8 -*-

import typing
from Const import ConstT
import re
#                                    word1         / word2 /*
_rePtn_githubRpUrl=r'https://github\.com/([\w\d\._\-]+)/([\w\d\._\-]+)\.git'
# word1/word2 即 org组织/repo仓库名  ，添加 中划线 到 此 正则表达式

def _fetch_goal_rpName(githubRpUrl:str):
# goal_rpUrl:str="https://github.com/pytorch/QNNPACK.git"
    matches = re.match(pattern=_rePtn_githubRpUrl, string=githubRpUrl)
    assert matches is not None and len(matches.groups()) == 2, f"【错误】【断言失败】【正则不匹配】【{_rePtn_githubRpUrl}】【{githubRpUrl}】"
    word1:str = matches.group(1)
    word2:str = matches.group(2)
    goal_rpName=f"{word1}{ConstT.OrgSepRepo}{word2}"
    return goal_rpName


class GoalRpT:

    def __init__(self):
        pass

    def __fill__(self,
    goal_rpUrl:str,
    goal_rpOrg:str,
    goal_rpName:str,
    goal_rpDesc:str,
    goal_rpIsPub:bool,
    goal_rpLang:int) -> None:
        self.goal_rpUrl:str=goal_rpUrl
        self.goal_rpOrg:str=goal_rpOrg
        self.goal_rpName:str=goal_rpName
        self.goal_rpDesc:str=goal_rpDesc
        self.goal_rpIsPub:bool=goal_rpIsPub
        self.goal_rpLang:int=goal_rpLang

    @staticmethod
    def build(goal_rpUrl:str,goal_rpOrg:str):
#举例:
# goal_rpUrl:str="https://github.com/pytorch/QNNPACK.git"
# goal_rpOrg:str="mirrr"
# goal_rpName:str="pytorch--QNNPACK"
# goal_rpDesc:str="【来源】https://github.com/pytorch/QNNPACK.git"
# goal_rpIsPub:bool=True
# goal_rpLang:int=0
        thiz:GoalRpT=GoalRpT()
        thiz.goal_rpUrl=goal_rpUrl
        thiz.goal_rpOrg=goal_rpOrg
        thiz.goal_rpName=_fetch_goal_rpName(goal_rpUrl)
        thiz.goal_rpDesc=f"【来源】{goal_rpUrl}"
        thiz.goal_rpIsPub=True
        thiz.goal_rpLang=0
        return thiz






