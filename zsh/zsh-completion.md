# `zsh` Completion

## Substitutions

### Commands

- `!-1` / `!!`: Previous command
- `!#`: Current command

### Parameters

#### Current

- `!#:0` / `!#0`: Current command
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
