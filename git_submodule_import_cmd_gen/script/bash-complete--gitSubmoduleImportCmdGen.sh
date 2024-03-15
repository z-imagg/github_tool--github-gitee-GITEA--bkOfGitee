#!/usr/bin/env bash

#source me.sh

_gitSubmoduleImportCmdGen() {
    local pre cur opts

    COMPREPLY=()
    pre=${COMP_WORDS[COMP_CWORD-1]}
    cur=${COMP_WORDS[COMP_CWORD]}
    opts="--parent_repo_dir   --goal_org   --sleep_seconds --sleep_seconds_delta -h --help"
    case "$cur" in
    -* )
        COMPREPLY=( $( compgen -W "$opts" -- $cur ) )
    esac
}
complete -F _gitSubmoduleImportCmdGen   gitSubmoduleImportCmdGen.py
