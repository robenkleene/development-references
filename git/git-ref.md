# `git` Ref

## Special Refs

- `HEAD`: Current commit
- `ORIG_HEAD`: Head before a drastic change

## Relative Refs

- `HEAD~2`: Two commits back from `HEAD` (or grandparent)
- `HEAD^2`:

## Reflog

The reflog is a chronological list of changes in `git`.

- `git reflog`: List the reflog
- `HEAD@{1}`: Reference the previous commit in the reflog
