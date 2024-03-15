#!/usr/bin/env bash

#获得 当前脚本所在的目录 的绝对路径，  不依赖于工作目录在哪里
_script='source <(curl -s  giteaz:3000/bal/bash-simplify/raw/commit/2ee8e5286f925e44d0081ac10beee497e0245ded/dir_util.sh) ; getCurScriptDirByConcat _dir _fn && echo "CurSctDir=${CurScriptDir}; CurSctFn=${CurScriptNm}" '
_script="${_script/_dir/$(pwd)}"
_script="${_script/_fn/$0}"
eval "$(bash -c "$_script")"
echo $CurSctDir, $CurSctFn

#####


VENV_HOME=${CurSctDir}/.venv
ActivVenv=$VENV_HOME/bin/activate
test -f $ActivVenv || python3 -m venv $VENV_HOME