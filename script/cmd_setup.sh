#!/usr/bin/env bash

#source me.sh 或 bash me.sh 均能获取当前脚本完整路径的写法
declare -r f=$(readlink -f ${BASH_SOURCE[0]}) 2>/dev/null
d=$(dirname $f)
#d==/fridaAnlzAp/github-gitee-GITEA/script/

hm=$(realpath -s ${d}/../)
#hm=/fridaAnlzAp/github-gitee-GITEA/
ImportHm=$hm/import2gitee
MigrateHm=$hm/migrate2GITEA
export PATH=$ImportHm/:$MigrateHm:$PATH
source $ImportHm/script/bash-complete--RepoRecurseImport.sh
source $MigrateHm/script/bash-complete--RepoRecurseMigrate.sh
chmod +x $ImportHm/RepoRecurseImport.py
chmod +x $MigrateHm/RepoRecurseMigrate.py

bash $hm/script/env_prepare.sh >/dev/null
source $hm/.venv/bin/activate

#正常可用：RepoRecurseImport.py --help 及其 bash自动完成
#正常可用：RepoRecurseMigrate.py --help 及其 bash自动完成