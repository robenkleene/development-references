# `git` Rebase

## Rebase

Rebase from the first common ancestor of the current branch (`HEAD`) and `<master>`:

```
git rebase -i `git merge-base HEAD main`
```
