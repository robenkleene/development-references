# `git` Branch

## Rename

- `git branch -m <newname>`: Rename the current branch
- `git branch -m <oldname> <newname>`: Rename a specific branch by name

## Log

- `git log main..`: list all the commits on the current branch that aren't on main

## Checking out files

- `git show master:Cartfile`: Show contents of file from another branch
- `git checkout master -- <path>`: Checkout a file from another branch, note this adds it to the index (`git reset` removes all files from the index)

## Remote

- `git branch -r`: List remote branches (`git fetch` first to make sure all the branches are listed)
- `git branch -vv`: See which remote branch a local branch is tracking

## Delete

- `-d` / `--delete`: Delete a branch
- `git push origin --delete`: Delete remote branch
