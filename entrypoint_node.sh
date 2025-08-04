alias ls='ls --color=auto'
alias grep='grep --color=auto'

case $TERM in
        xterm*|rxvt|Eterm|eterm|cygwin)
            PS1='\[\033[30;1m\][clab-node]${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
        ;;
esac