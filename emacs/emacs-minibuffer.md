# `emacs` Minibuffer

- `M-p` & `M-n`: Previous command
- `C-g`: Cancel minibuffer

## Stuck Minibuffer

If the minibuffer becomes stuck with a partial command, the solution is to focus it, either with the mouse or `C-x o`, then hit `C-g`. (Note that performing another minibuffer command, e.g., `M-x C-g` will not fix it.)

This probably happens when the minibuffer has an active command and then focus is lost (e.g., when clicking into the popup from a `<partial-command>-<tab>`.
