# `git` Ignore

- `git clean -dfX`: Delete all ignored files

## Ignored Files

List ignored files:

    git ls-files -c --ignored --exclude-standard

Remove all ignored files:

    git ls-files -c --ignored --exclude-standard -z | xargs -0 git rm --cached

Remove all ignored files (this isn't a great way to do this, this removes every file from the repo, then you just re-commit without the ignored files):

    git rm -r --cached .

