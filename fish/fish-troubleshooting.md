# `fish` Troubleshooting

To solve `TERMINFO` issues, e.g., ""could not set up terminal". run:

    env TERMINFO=/usr/share/terminfo fish

Then:

    brew reinstall ncurses
