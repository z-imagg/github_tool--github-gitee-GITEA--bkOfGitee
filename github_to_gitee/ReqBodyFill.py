#!/usr/bin/env python
# -*- coding: utf8 -*-

from urllib.parse import unquote_plus,quote_plus
from pathlib import Path
from GoalRepo import GoalRpT
import typing
from MyConfig import outHomeDir
from PathUtil import getScriptDir

#获取当前py脚本所在目录，非当前工作目录
_sD=getScriptDir(__file__)
print(f"scriptDir={_sD}")
#scriptDir=/app/wiki/github_tool/github_to_gitee


#术语: Ls == List == 列表 == 数组
#术语: goal == 目标, rp == repository, reqBdy == requestBody == 请求体 == '接口的curl例子.--data-raw'
#术语: kSEPv == keySeperatorValue == key和value之间的分割符, fld == field == 字段, fldSepOnUrl == fieldSeperatorOnUrl == url中字段之间的分割符
#术语: org == organization == 组织 == 仓库名的上一级 
#术语: from_rpUrl == 目标仓库的url, goal_rpOrg == 目标仓库的组织, goal_rpName == 目标仓库的名字, goal_rpDesc == 目标仓库的描述， goal_rpIsPub == 目标仓库是否开源, goal_rpLang == 目标仓库语言
#术语: ReqBodyFillF = 函数ReqBodyFill
#术语: 某_fP == 某_filePath == 某_文件路径, tmpl == template == 模板,  HPRBUD == HttpPostReqBdyUrlEncoded
kSEPv:str="="
fldSepOnUrl:str="&"

def _splitLineByFirstSep(line:str,sep:str):
    arr=line.split(sep)
    return arr[0], sep.join(arr[1:])

def _concatKeyValBySep(keyJ:str,valJ:str,sep:str):
    return f"{keyJ}{sep}{valJ}"

def ReqBodyFillF(goalRp:GoalRpT):
    
    Path(outHomeDir).mkdir(parents=True,exist_ok=True)
    outHPRBUD_dir=f"{outHomeDir}/HttpPostReqBdyUrlEncoded/"
    Path(outHPRBUD_dir).mkdir(parents=True,exist_ok=True)

    from_rpUrl:str=goalRp.from_rpUrl
    goal_rpOrg:str=goalRp.goal_rpOrg
    goal_rpName:str=goalRp.goal_rpName
    goal_rpDesc:str=goalRp.goal_rpDesc
    goal_rpIsPub:bool=goalRp.goal_rpIsPub
    goal_rpLang:int=goalRp.goal_rpLang

    # from_rpUrl:str="https://github.com/pytorch/QNNPACK.git"
    # goal_rpOrg:str="mirrr"
    # goal_rpName:str="pytorch--QNNPACK"
    # goal_rpDesc:str="【来源】https://github.com/pytorch/QNNPACK.git"
    # goal_rpIsPub:bool=True
    # goal_rpLang:int=0

    tmpl_HPRBUD_fN:str="template__HttpPostReqBdyUrlEncoded.txt"
    goal_tmpl_HPRBUD_fP=f"{tmpl_HPRBUD_fN.replace('template__','')}__{goal_rpName}"

    reqBdyUrlEncoded:str=Path(f"{_sD}/{tmpl_HPRBUD_fN}").read_text()#f_1
    # reqBdy:str=unquote_plus(reqBdyUrlEncoded)#f0
    reqBdy:str=reqBdyUrlEncoded # k=v,  v是urlEncoded的，但是不关心模板中的v

    fldLs:typing.List[str]=reqBdy.split(fldSepOnUrl)#f1
    fldDict=dict(_splitLineByFirstSep(lnJ,kSEPv) for lnJ in fldLs)#f2
    #填写 目的仓库 描述
    fldDict["project[import_url]"]=from_rpUrl
    fldDict["project[namespace_path]"]=goal_rpOrg
    fldDict["project[name]"]=goal_rpName
    fldDict["project[path]"]=goal_rpName
    fldDict["project[description]"]=goal_rpDesc
    fldDict["project[public]"]="1" if goal_rpIsPub else "0"
    fldDict["language"]=f"{goal_rpLang}"

    goal_fldUELs:typing.List[str]=[_concatKeyValBySep(quote_plus(keyJ),quote_plus(valJ),kSEPv) for keyJ,valJ in fldDict.items() ]#逆f2
    goal_reqBdyUE:str=fldSepOnUrl.join(goal_fldUELs)#逆f1
    # goal_reqBdyUrlEncoded:str=quote_plus(goal_reqBdy)#逆f0
    # Path(f"{outHomeDir}/dev__{goal_tmpl_HPRBUD_fP}").write_text(goal_reqBdy)#开发调试用
    Path(f"{outHPRBUD_dir}/{goal_rpName}").write_text(goal_reqBdyUE)#逆f_1
    print(f"【正常填写请求体】{goal_tmpl_HPRBUD_fP}")
    return



if __name__ == "__main__":
    print(f"【请注意，您正在运行单元测试】{__file__}")
    goal_rpName:str="pytorch--QNNPACK"
    ReqBodyFillF(
    from_rpUrl="https://github.com/pytorch/QNNPACK.git"
    ,goal_rpOrg="mirrr"
    ,goal_rpName="pytorch--QNNPACK"
    ,goal_rpDesc="【来源】https://github.com/pytorch/QNNPACK.git"
    ,goal_rpIsPub=True
    ,goal_rpLang=0
)
    
end=True