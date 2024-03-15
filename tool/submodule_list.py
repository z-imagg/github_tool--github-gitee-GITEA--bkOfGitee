#!/usr/bin/env python
# -*- coding: <encoding name> -*-


from pathlib import Path
import git
from git import cmd
import shutil

import sys
# print(sys.argv)
CurScriptNm:str=sys.argv[0]



_BgRp:str="/fridaAnlzAp/pytorch"
BgRp:git.Repo=git.Repo(path=_BgRp)
BgRpRmt:git.Remote=BgRp.remote()
originUrlBgRp:str=BgRpRmt.url
BgRp_:cmd.Git=BgRp.git

# BgRp.submodules

sbmKBg:git.Submodule

for k,sbmKBg in enumerate( BgRp.submodules):
    #bash 关联数组(即字典)
    sbmKBg_bash=f'''declare -A sbmKBg; sbmKBg["name"]="{sbmKBg.name}"; sbmKBg["path"]="{sbmKBg.path}"; sbmKBg["url"]="{sbmKBg.url}"; sbmKBg["hexsha"]="{sbmKBg.hexsha}"; sbmKBg["branch_name"]="{sbmKBg.branch_name}"; sbmKBg["branch_path"]="{sbmKBg.branch_path}";  '''
    # print(f"{sbmKBg.name}, {sbmKBg.path}, {sbmKBg.url}, {sbmKBg.hexsha}, {sbmKBg.branch_name}, {sbmKBg.branch_path}")
    print(sbmKBg_bash)
#此循环输出举例(torch-v0.3.0):
# declare -A sbmKBg; sbmKBg["name"]="torch/lib/gloo"; sbmKBg["path"]="torch/lib/gloo"; sbmKBg["url"]="https://github.com/facebookincubator/gloo"; sbmKBg["hexsha"]="05ad98aeb66fabc7c8126e6068d4a70134d4b80d"; sbmKBg["branch_name"]="master"; sbmKBg["branch_path"]="refs/heads/master";  
# declare -A sbmKBg; sbmKBg["name"]="torch/lib/pybind11"; sbmKBg["path"]="torch/lib/pybind11"; sbmKBg["url"]="https://github.com/pybind/pybind11"; sbmKBg["hexsha"]="9f6a636e547fc70a02fa48436449aad67080698f"; sbmKBg["branch_name"]="master"; sbmKBg["branch_path"]="refs/heads/master";  
# declare -A sbmKBg; sbmKBg["name"]="torch/lib/nanopb"; sbmKBg["path"]="torch/lib/nanopb"; sbmKBg["url"]="https://github.com/nanopb/nanopb.git"; sbmKBg["hexsha"]="14efb1a47a496652ab08b1ebcefb0ea24ae4a5e4"; sbmKBg["branch_name"]="master"; sbmKBg["branch_path"]="refs/heads/master"; 



#bash调用方式:  python /fridaAnlzAp/pytorch-v0.1.x/submodule.py | while IFS= read -r line; do eval  "$line";  echo ${sbmKBg['name']}, ${sbmKBg['path']}, ${sbmKBg['url']}, ${sbmKBg['hexsha']}, ${sbmKBg['branch_name']} , ${sbmKBg['branch_path']} ; done
# torch/lib/gloo, torch/lib/gloo, https://github.com/facebookincubator/gloo, 05ad98aeb66fabc7c8126e6068d4a70134d4b80d, master , refs/heads/master
# torch/lib/pybind11, torch/lib/pybind11, https://github.com/pybind/pybind11, 9f6a636e547fc70a02fa48436449aad67080698f, master , refs/heads/master
# torch/lib/nanopb, torch/lib/nanopb, https://github.com/nanopb/nanopb.git, 14efb1a47a496652ab08b1ebcefb0ea24ae4a5e4, master , refs/heads/master

_end=True