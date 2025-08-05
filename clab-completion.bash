_clab_completion() {
    local cur prev opts
    COMPREPLY=()
    cur="${COMP_WORDS[COMP_CWORD]}"
    prev="${COMP_WORDS[COMP_CWORD-1]}"
    opts="start stop build clean"

    if [[ ${prev} == "start" || ${prev} == "stop" ]]; then
        COMPREPLY=( $(compgen -f -X '!*.yml' -- "${cur}") )
        return 0
    fi

    COMPREPLY=( $(compgen -W "${opts}" -- "${cur}") )
    return 0
}
complete -F _clab_completion clab