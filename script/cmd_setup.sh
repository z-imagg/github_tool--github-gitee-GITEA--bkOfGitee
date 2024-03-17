#!/usr/bin/env bash


f=$0 ; { [[ "$f" == /* ]] || f="$(pwd)/$f" ;} ; d=$(dirname $f)
#d==/fridaAnlzAp/github-gitee-gitea/script/

hm=$(realpath -s ${d}/../)
#hm=/fridaAnlzAp/github-gitee-gitea/
ImportHm=$hm/import2gitee
MigrateHm=$hm/migrate2GITEA
export PATH=$ImportHm/:$MigrateHm:$PATH
source $ImportHm/script/bash-complete--RepoRecurseImport.sh
source $MigrateHm/script/bash-complete--RepoRecurseMigrate.sh
chmod +x $ImportHm/RepoRecurseImport.py
chmod +x $MigrateHm/RepoRecurseMigrate.py

bash $hm/script/env_prepare.sh
source $hm/.venv/bin/activate

#正常可用：RepoRecurseImport.py --help 及其 bash自动完成
#正常可用：RepoRecurseMigrate.py --help 及其 bash自动完成