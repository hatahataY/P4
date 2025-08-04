alias ls='ls --color=auto'
alias grep='grep --color=auto'

case $TERM in
        xterm*|rxvt|Eterm|eterm|cygwin)
            PS1='\[\033[30;1m\][clab]${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
        ;;
esac


alias clab-start='\
containerlab deploy -t /root/containerlab/topo-clab.yml && \
containerlab destroy -t /root/containerlab/topo-clab.yml'

echo "====================================================="
echo "  Welcome to Containerlab !"
echo "  To start an experiment, run the following command:"
echo ""
echo "  $ clab-start"
echo ""
echo "  To end the experiment and remove containers,"
echo "  press 'Ctrl+C'. "
echo "====================================================="