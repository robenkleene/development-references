# `fish` Variables

## Universal Variables

- Stored in `~/.config/fish_variables` and preserved across restarts (`abbr` are also stored in this file)
- `set -Ux`: Save universal variable (that will also be exported with `-x`, which is probably what's wanted)
- `set -e`: Remove a universal variable
- `set --names -U`: List all universal variables
- `set --names -U | grep -v "^_*fish"`: Can seems like it gets all variables that have been set manually
