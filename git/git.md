# `git`

## Log

* `git log -p` (`-u`, `--patch`): Generate a patch for the commit, this is a lot like a combined `git log` and `git diff`
* `git log -G`: Output all commits whose contents match a regular expression
* `git log -G <string> -p <path>`: Combining the above too flags, this will show the `diff` that contain a specific string, for a specific file

## Other Branches

* `git show master:Cartfile`: Show contents of file from another branch
* `git checkout master -- <path>`: Checkout a file from another branch, note this adds it to the index (`git reset` removes all files from the index)

### File Substitution

Using file substitution with with `vimdiff`:

	vimdiff <(git show development:Cartfile) Cartfile

## Remote

* `git ls-remote --get-url`: Print just the URL

### `git-remote`

* `--verbose` or `-v`: Print the full remote URL with additional info

### Branches

* `git branch -r`: List remote branches (`git fetch` first to make sure all the branches are listed)

## Information

* `git rev-parse HEAD`: Print current commit

## Listing Files

### `git ls-files`

* `-m` or `--modified`: List modified files
* `-o` or `--others`: List untracked and ignored files
* `--exclude-standard`: Exclude ignored files

So `git ls-files -o --exclude-standard` will list untracked files that aren't ignored.

