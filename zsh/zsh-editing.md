# `zsh` Editing

- `M-_` / `C-X u` / `C-X C-u`: Undo
- `M-C--`: Insert previous parameter
- `M-.` or `M-_`: Insert last parameter of previous command
- `M-h`: Help for current command (runs `man`)
- `C-q` or `^[q`: Push current line (clears the line, execute one command and then return the line)
- `C-y`: Yank (paste in emacs terminology)
- `C-w`: Delete last word (or parameter)

## Autoload

```
autoload -Uz copy-earlier-word
zle -N copy-earlier-word
bindkey -e "^[m" copy-earlier-word
```

`copy-earlier-word`
