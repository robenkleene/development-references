# `hg`

- `hg status`
- `hg amend`: Amend last commit (`hg` has no staging)
- `hg id -i`: Print commit ID
- `hg update`: Checkout a commit

## Commit

- `hg commit`: Commit (`hg` has no staging)
- `hg commit <file>`: Commit just a specific file

## Files

- `hg add`: Add all untracked files
- `hg addremove`: Add and remove all files
- `hg rm <file>`: Remove
- `hg record`: Make partial commits

## Pull

- `hg pull`: Fetch commits (does not merge like `git`, only downloads, more like `git fetch`)

## Rebase

- `hg rebase -d master`: Get branch up-to-date with master (`arc pull` is better)

## Patch

- `hg import --prefix . --no-commit -`: Import commit from STDIN
    - `hg import -`: Read a patch from STDIN
    - `hg import --no-commit -`: Read a patch from STDIN without creating a commit
- `hg diff`: Print a patch

## Diff

- `hg diff -r bottom^`: Diff master
- `hg diff -r bottom^ --stat`: Diff stats, including just change filenames
- `hg diff -pr .^1`: Diff of last commit plus local changes
- `hg log -pr .^1`: Diff master
- `hg status --change .`: List uncommitted changed files
- `hg status --change bottom`: List changed files on current branch
- `hg status --rev bottom`: List all changed files on current branch

## Reverting

- `hg revert --all`: Revert all files
- `hg purge --files`: Delete all untracked files (marked by `?`)
- `hg checkout . --clean`: Checkout all changed files
- `hg revert -r <rev> filename`: Checkout version of a file from a different branch
- `hg revert filename`: Checkout a locally deleted file

## Squashing

- `hg histedit`: Delete

## Conflicts

- `hg resolve --all`: Resolve all merge conflicts

## Workflow

- `hg log -pr .`: Show last commit
- `hg backout -r .`: Revert last commit

## Stash

- `hg shelve --list`: List stashed changes
- `hg unshelve`: Pop from stash
- `hg shelve -d default`: Drop default stash

## Rebase

- `hg histedit`: Interactive history re-order
