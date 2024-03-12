#!/usr/bin/env python
# -*- coding: utf8 -*-




import os
from pathlib import Path

def getScriptDir(scriptFullPath:str)->str:
    #获取当前py脚本所在目录，非当前工作目录
    scriptFullPath:str = os.path.realpath(__file__)
    scriptDir:str=Path(scriptFullPath).parent
    # print(f"scriptFUllPath {scriptFullPath}, _curScriptDir {scriptDir}")
    return scriptDir


if __name__ == "__main__":
    print(f"【请注意，您正在运行单元测试】{__file__}")
    scriptDir=getScriptDir(__file__)
    print(f"scriptDir={scriptDir}")
    