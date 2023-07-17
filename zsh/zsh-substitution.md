# `zsh` Substitution

- `vim ${(f)"$(pbpaste)"}`: Each line on clipboard as separate file
    - `(f)` is substitution flag to treat each word as a new line
