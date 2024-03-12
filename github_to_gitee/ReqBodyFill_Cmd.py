#!/usr/bin/env python
# -*- coding: utf8 -*-

#【文件作用】 从命令行导入单个github仓库到gitee
#    gitee登录凭据 通过文件 template__HttpPostReq__curl.sh 来表达

import typing
from Const import ConstT
from ReqBodyFill import ReqBodyFillF
from GoalRepo import GoalRpT
from MyConfig import outHomeDir
from pathlib import Path
import sys
import sh
from PathUtil import getScriptDir

#获取当前py脚本所在目录，非当前工作目录
_sD=getScriptDir(__file__)

usage=f"【命令语法】【{__file__} 来源github仓库地址 目标gitee组织 】； \n【举例】【 {__file__} https://github.com/NVlabs/cub.git mirrr 】"
exitCodeErrUsage:int=11
if len(sys.argv)<3:
    print(usage)
    exit(exitCodeErrUsage)

from_rpUrl:str=sys.argv[1]
goal_rpOrg:str=sys.argv[2]

goal_rp:GoalRpT=GoalRpT.build(from_rpUrl,goal_rpOrg)
destGitUrl:str=goal_rp.getDestGitUrl()
ReqBodyFillF(goal_rp)

curlTmpl:str=Path( f"{_sD}/template__HttpPostReq__curl.sh").read_text()

reqBodyDir:str=f"{outHomeDir}/HttpPostReqBdyUrlEncoded/"
reqDir:str=f"{outHomeDir}/HttpPostReq__curl/"
Path(reqBodyDir).mkdir(parents=True,exist_ok=True)
Path(reqDir).mkdir(parents=True,exist_ok=True)
reqBodyFp:str=f"{reqBodyDir}/{goal_rp.goal_rpName}"
reqFp:str=f"{reqDir}/{goal_rp.goal_rpName}"
#sed "s/template__HttpPostReqBdyUrlEncoded.txt/%/g" > $HPR_curl_OutDir/%
# sedCmd:sh.Command=sh.Command("/usr/bin/sed").__call__("s/template__HttpPostReqBdyUrlEncoded.txt/%/g", f"{_sD}/template__HttpPostReq__curl.sh",_out=HPR_curl_fP)

curlScript=curlTmpl.replace("template__HttpPostReqBdyUrlEncoded.txt",reqBodyFp)
Path(reqFp).write_text(curlScript)


curlCmd:sh.Command=sh.Command(reqFp)
#这里命令退出代码不为0，会抛出异常
curlOut:str=curlCmd.__call__()
print("reqFp ",reqFp)
print("curlOut",curlOut)