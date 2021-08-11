# `xargs`

- `-n 1`: Only run the command once for each file
- `-o` / `--open-tty`: Make STDIN a terminal (this gets rid of Vim's "Input is not from a terminal" error)

## Placeholder

    dirname (fd --hidden -p ".github/workflows/.*.yml") | sort | uniq | xargs -I{} echo {}
