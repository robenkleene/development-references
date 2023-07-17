# `xargs`

- `-n 1` (or `-n1`): Only run the command once for each file
- `-o` / `--open-tty`: Make STDIN a terminal (this gets rid of Vim's "Input is not from a terminal" error)

## Examples

- `pbpaste | tr '\n' '\000' | xargs -0 ls`

## Placeholder

    dirname (fd --hidden -p ".github/workflows/.*.yml") | sort | uniq | xargs -I{} echo {}

### Multiple Commands

    dirname (fd --hidden -p ".github/workflows/.*.yml") | sort | uniq | xargs -I{} sh -c "echo; echo {}; git -C {} status"
