# `nnn`

- `␣`: Tag file
- `^G`: Quit cd
- `1` / `2` / `3` / `4`: Switch to tab
- `␣` / `+`: Toggle selection

## Filter

- `/`: Filter
- `⎋`: Exit prompt (e.g., a filter)
- `^L`: Toggle last filter
- `^N`: Type to nav
- `.`: Toggle show hidden files

## Help

- `?`: Show shortcuts (dumped to terminal so you can see them on quit)

## Operations

- `E`: Edit file (e.g., an empty file that can't be edited with return)
- `X` / `^X`: Delete file
- `^R`: Rename file
- `P`: Copy to new location
- `V`: Move to new location
- `N`: Create new
    - `D`: Directory
    - `F`: File
- `!` / `^]`: Spawn new shell on top of `nnn` (use `exit` to get back to `nnn`, `echo $NNNLVL` will show the current level)
- `]`: Open native shell prompt to enter shell commands

## Plugins

- `;`: Run a plugin (followed by assigned key) or `↩` to select a plugin to run
- `⌥<key>`: Can also be used to run a plugin
