# `git` Ignore

List ignored files:

    git ls-files -c --ignored --exclude-standard -z

Remove all ignored files (this isn't a great way to do this, this removes every file from the repo, then you just re-commit without the ignored files):

    git rm -r --cached .

