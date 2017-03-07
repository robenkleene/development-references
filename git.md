# `git`

## Log

- `git log -p` (`-u`, `--patch`): Generate a patch for the commit, this is a lot like a combined `git log` and `git diff`
- `git log -G`: Output all commits whose contents match a regular expression
- `git log -G <string> -p <path>`: Combining the above too flags, this will show the `diff` that contain a specific string, for a specific file

## Show

- `git show master:Cartfile`
