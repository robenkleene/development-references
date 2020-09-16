# `irc`

Progress on manually sending an IRC message:

    echo -e 'USER bot guest repla-bot repla-bot\nNICK repla-bot\nJOIN #repla-development\nPRIVMSG #repla-development :A test message\nQUIT\n' | nc chat.freenode.net 6667

Working example:

    (
    echo "NICK repla-bot"
    echo "USER repla-bot 0.0.0.0 repla :Repla Bot"
    sleep 20
    echo "JOIN #repla-development"
    echo "PRIVMSG #repla-development :CI Finished"
    echo "QUIT"
    ) | nc irc.freenode.net 6667
