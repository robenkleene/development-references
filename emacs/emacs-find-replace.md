# `emacs` Find & Replace

- `M-s .` (`isearch-forward-symbol-at-point`): Search for symbol at point
    - These searches go to a different ring than regular searches, to get a previous symbol search, start the search with `M-s _`

## Search

- `C-s`: Incremental search
- `C-s`: Forward
- `C-r`: Backward
- `C-g`: Cancel

## Incremental Search

- `M-e`: Edit the current incremental search

## Replace

- `M-%`: Find & replace
- `C-M-%`: Regular Expression Find & replace

### Active Replace

- `!`: Replace to the end of the file
- `␣` or `Y`: One replacement
- `q` or `↩`: Exit

## Compilation Errors & `grep`

- `C-x <backtick>` or `M-g n` / `M-g p`: Next/previous Error
- You can clear the current grep search by `kill-this-buffer` on the `*grep*` buffer

## Special

- `highlight-regex`: Highlight regular expression
- `highlight-phrase`: Highlight case-insensitive with spaces
