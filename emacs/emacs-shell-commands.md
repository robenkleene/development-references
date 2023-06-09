# `emacs` Shell Commands

- `C-u M-!`: Insert the result of a shell command in the minibuffer (e.g., for a filename). Requires `(setq enable-recursive-minibuffers t)`.
- `M-!` / `shell-command`: Run a shell command
- `M-|` / `shell-command-on-region`: Run a shell command on the region (output is printed to the minibuffer)
- `C-u M-|`: Run a shell command on the region, replacing region
