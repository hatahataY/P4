alias ls='ls --color=auto'
alias grep='grep --color=auto'

case $TERM in
        xterm*|rxvt|Eterm|eterm|cygwin)
            PS1='\[\033[30;1m\][clab]${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
        ;;
esac

echo "====================================================="
echo "  Welcome to Containerlab!"
echo "  'clab' is a wrapper to simplify your workflow."
echo "  -------------------------------------------------"
echo "  Available Commands:"
echo "  - clab start <topology_file> : Deploys the specified lab topology."
echo "  - clab stop <topology_file>  : Destroys the specified lab topology."
echo "  - clab build                 : Builds the containerlab image."
echo "  - clab clean                 : Removes the containerlab image."
echo "====================================================="