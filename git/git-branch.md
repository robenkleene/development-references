# `git` Branch

## Rebase

Rebase from the first common ancestor of `<features>` branch and `<master>`:

```
git rebase -i `git merge-base <feature> <master>`
```

## Log

- `git log master..`: list all the commits on the current branch that aren't on master

## Checking out files

- `git show master:Cartfile`: Show contents of file from another branch
- `git checkout master -- <path>`: Checkout a file from another branch, note this adds it to the index (`git reset` removes all files from the index)

## Remote

- `git branch -r`: List remote branches (`git fetch` first to make sure all the branches are listed)
- `git branch -vv`: See which remote branch a local branch is tracking
- `git branch -m <oldname> <newname>`: Rename a branch, `<oldname>` defaults to the current branch so can be omitted.
