# `irc`

Progress on manually sending an IRC message:

    echo -e 'USER bot guest repla-bot repla-bot\nNICK repla-bot\nJOIN #repla-development\nPRIVMSG #repla-development :A test message\nQUIT\n' | nc chat.freenode.net 6697

