# Emacs Consult

## `rg`

- Flags after `#TODO -- -g *.el` (`fd` probably doesn't support this because it's a custom command, not a built in?)
- A second `#` to add Vertico searches after `rg` filtering, e.g., `#TODO#!today` will return for all matches for `TODO` from `rg` and then filter those in Vertico to remove lines that match `today`.
