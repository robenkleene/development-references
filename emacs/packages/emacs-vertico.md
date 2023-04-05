# Emacs Vertico

To accept a match that doesn't exist, use `M-RET` (`vertico-exit-input`), or use `<up>` to highlight the prompt line itself.

## `rg`

- Flags after `#TODO -- -g *.el`
- A second `#` to add Vertico searches after `rg` filtering, e.g., `#TODO#!today` will return for all matches for `TODO` from `rg` and then filter those in Vertico to remove lines that match `today`.
