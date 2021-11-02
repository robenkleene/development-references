# `git` Ignore

List ignored files:

    git ls-files -c --ignored --exclude-standard -z

Remove all ignored files (this sometimes deletes files that aren't ignored):

    git rm -r --cached .

