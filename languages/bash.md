# Bash

- `$(command)`: Command substitution, the result of the command replaces the  `cat $(ls)` command.
- `( list )` and `{ list; }` are used to group commands, e.g., `(ls *.js; ls *.css) | grep test`. The difference is that `()` creates a sub-shell and `{}` does not. (Note that the `;` is required only with `{}`.)