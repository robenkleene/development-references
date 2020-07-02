# `zsh` Editing

`^]` is meta.

- `^_` or `^Xu` or `^X^U`: Undo
- `^[^-`: Insert previous parameter
- `^[.` or `^[_`: Insert last parameter of previous command
- `^[h`: Help for current command (runs `man`)
- `^q` or `^[q`: Push current line (clears the line, execute one command and then return the line)
- `^y`: Yank (paste in emacs terminology)
- `^w`: Delete last word (or parameter)