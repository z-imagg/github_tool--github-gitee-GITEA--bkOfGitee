#!/usr/bin/env bash

#获得 当前脚本所在的目录 的绝对路径，  不依赖于工作目录在哪里
_script='source <(curl -s  http://giteaz:3000/bal/bash-simplify/raw/commit/5bc5e5ee4dffae077f76b1baa177273ce89843a8/dir_util.sh) ; getCurScriptDirByConcat _dir _fn && echo "D=${CurScriptDir}; F=${CurScriptNm}" '
_script="${_script/_dir/$(pwd)}"
_script="${_script/_fn/$0}"
eval "$(bash -c "$_script")"
echo ${D}, ${F}

#####
cd ${D}


VENV_HOME=${D}/.venv
ActivVenv=$VENV_HOME/bin/activate
test -f $ActivVenv || python3 -m venv $VENV_HOME


source $ActivVenv
pip install -r ${D}/requirements.txt