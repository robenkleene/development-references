# `tmux` Cut and Paste

- `Y`: Paste selection

- `tmux show-buffer`: Show the `tmux` buffer

## Default Mouse

With `set -g mouse on`, by default `tmux` will copy to the `tmux` buffer and then deselect. If `y` has a copy mode override that also copies to the system clipboard, then that key can be hit while holding down the mouse button to copy to the system clipboard.
