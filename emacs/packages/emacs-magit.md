# `magit`

* `s`: `git add`

## Status

* `<M-tab>`: Cycle diff collapsed

## Commit

1. `c c`: Start commit (don't use `C`, that's what inserts an entry for the current file)
2. `C-c C-c`: Finish commit
3. `P p`: Git push

* `C-c C-k`: Cancel commit

## Basic

* `F p`: `git pull`

## Branches

* `b c`: Change branch

## Diff

* `d r <branch>`: Diff vs. a branch

## Log

* `l`: Brings up the log popup
* `l=g`: Perform a git log search, e.g., `git log -G <string>`

When viewing a commit, `<space>` scrolls forward in the commit and `<backspace>` scrolls backward.

## Movement

- `N-p` / `N-n`: Next/previous section
- `p` / `n`: Next/previous subsection

## Advanced

- To checkout an older version of a file, even if it has been deleted,even if it has been deleted, use `magit-file-checkout`. If the point is on a path to that file, the default path will be that path. Use `HEAD^` for a recently deleted file.
