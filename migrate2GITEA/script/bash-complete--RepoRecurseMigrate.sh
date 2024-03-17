#!/usr/bin/env bash

#source me.sh

_RepoRecurseMigrate() {
    local pre cur opts

    COMPREPLY=()
    pre=${COMP_WORDS[COMP_CWORD-1]}
    cur=${COMP_WORDS[COMP_CWORD]}
    opts="--from_repo_url  --from_commit_id  --mirror_base_url   --mirror_org_name --sleep_seconds -h --help"
    case "$cur" in
    -* )
        COMPREPLY=( $( compgen -W "$opts" -- $cur ) )
    esac
}
complete -F _RepoRecurseMigrate   RepoRecurseMigrate.py
