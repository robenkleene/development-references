# `sd`

- `-s` / `--string-mode`: Disable regex
- `-p`: Preview change without executing

The basic strategy is to use `rg` to find matches then do a replace:

- `rg -l --hidden -F "Gottox/irc-message-action@v1" -0 | xargs -0 sd -p -s "Gottox/irc-message-action@v1" "Gottox/irc-message-action@v2"`

Remove `-p` to execute

## Multi-Line

- `-U` / `--multiline`
- `rg -l --hidden -U "runs-on: macos-latest\n    steps" -0 | xargs -0 sd -p 'runs-on: macos-latest\n' 'runs-on: macos-latest\n    timeout-minutes: 20\n'`
