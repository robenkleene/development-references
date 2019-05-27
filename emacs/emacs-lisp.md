# `emacs` Lisp

* `nil` and the empty list `()` are the same.
* `'` means don't evaluate this instead make it a reference to this.
* `-p` at the end of a function name is for predicate

## Language

- `boundp`: Test if a variable is nil
- `bound-and-true-p`: Test if a variable is not nil and true

## Comments

Lisp has hierarchical comments (e.g., `;` vs `;;` are indented differently). To insert a specific level of comment, use: `M-2 M-;` where `2` is the number of semicolons to use.

