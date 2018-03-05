# `git` Search

## Searching `git` Log

* `git log --grep "something"`: Search commit messages for a string
* `git log -G`: Output all commits whose contents match a regular expression
* `git log -p` (`-u`, `--patch`): Generate a patch for the commit, this is a lot like a combined `git log` and `git diff`
* `git log -G <string> -p <path>`: Combining the above too flags, this will show the `diff` that contain a specific string, for a specific file
