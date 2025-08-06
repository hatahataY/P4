alias ls='ls --color=auto'
alias ll='ls --color=auto -l'
alias l='ls --color=auto -lA'
alias grep='grep --color=auto'

case $TERM in
        xterm*|rxvt|Eterm|eterm|cygwin)
            PS1='\[\033[30;1m\][clab]${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
        ;;
esac

if [ -f /etc/bash_completion ] && ! shopt -oq posix; then
    . /etc/bash_completion;
fi
eval "$(docker completion bash)"
eval "$(containerlab completion bash)"
eval "$(register-python-argcomplete clab)"

echo "====================================================="
echo "  Welcome to Containerlab!"
echo "  'clab' is a wrapper to simplify your workflow."
echo "====================================================="