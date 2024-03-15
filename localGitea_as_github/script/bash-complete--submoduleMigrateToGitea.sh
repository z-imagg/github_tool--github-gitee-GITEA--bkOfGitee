#!/usr/bin/env bash

#source me.sh

_submoduleMigrateToGitea() {
    local pre cur opts

    COMPREPLY=()
    pre=${COMP_WORDS[COMP_CWORD-1]}
    cur=${COMP_WORDS[COMP_CWORD]}
    opts="--from_parent_repo_dir   --mirror_base_url   --mirror_org_name -h --help"
    case "$cur" in
    -* )
        COMPREPLY=( $( compgen -W "$opts" -- $cur ) )
    esac
}
complete -F _submoduleMigrateToGitea   submoduleMigrateToGitea.py
