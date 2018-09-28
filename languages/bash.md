# Bash

- `$(command)`: Command substitution, the result of the command replaces the  `cat $(ls)` command.
- `( list )` and `{ list; }` are used to group commands, e.g., `(ls *.js; ls *.css) | grep test`. The difference is that `()` creates a sub-shell and `{}` does not. (Note that the `;` is required only with `{}`.)

## `getopts`

In `while getopts ":a:bh" option`, the first `:` runs `getopts` in "silent error checking mode", e.g., if you want to handle error messages yourself. In `a:`, it means the `a` flag can have arguments.
