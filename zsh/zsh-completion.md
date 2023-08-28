# `zsh` Completion

- `=(<command)`: Complete a path with tempfile that's a result of `<command>` (like `<(<command>)` but allows file to be accessed)
- `=<command>`: Expand to full path of argument (like `which <command>`)

## Substitutions

### Commands

- `!-1` / `!!`: Previous command with parameters
- `!-3`: Third last command with parameters
- `!#`: Current command with parameters
- `!vi`: Complete a previous command that starts with `vi`

### Parameters

#### Current

- `!#:0` / `!#0`: Current command without parameters
- `!#:^` / `!#^`: Insert first parameter in current line
- `!#:$` / `!#$`: Insert previous parameter in current line (same as `M-C--` binding)
- `!#:1` / `!#1`: Insert any previous parameter in current line (`1` maps to the parameter spot)
- `!#:*` / `!#*`: Insert all parameters in current line (`1` maps to the parameter spot)

#### Previous

- `!:0` / `!0`: Previous command
- `!:$` / `!$`: Last argument from previous command (same as `M-.` / `M-_` bindings)
- `!:*` / `!*`: All arguments from previous command
- `!:3-$`: Third to last from previous command
- `!-3:3-$`: Third to last from three commands ago
- `!:1-3`: First through third arguments of previous command
