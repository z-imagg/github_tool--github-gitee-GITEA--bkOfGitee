#!/usr/bin/env bash

#获得 当前脚本所在的目录 的绝对路径，  不依赖于工作目录在哪里
_script='source <(curl -s  http://giteaz:3000/bal/bash-simplify/raw/commit/51de90716f98be15fe31a75e37513cb4915563ce/dir_util.sh) ; getCurScriptDirByConcat _dir _fn && echo "D=${CurScriptDir}; F=${CurScriptNm}" '
_script="${_script/_dir/$(pwd)}"
_script="${_script/_fn/$0}"
eval "$(bash -c "$_script")"
echo ${D}, ${F}

#####
cd ${D}
Hm="${D}/../" # == /fridaAnlzAp/github-gitee-gitea


VENV_HOME=${Hm}/.venv
ActivVenv=$VENV_HOME/bin/activate
test -f $ActivVenv || python3 -m venv $VENV_HOME


source $ActivVenv
pip install -r ${Hm}/import2gitee/requirements.txt


source $ActivVenv
pip install -r ${Hm}/localGitea_as_github/requirements.txt