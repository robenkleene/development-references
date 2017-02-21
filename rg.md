# `rg`

* `-i` & `--ignore-case`: Ignore case
* `-s` & `--case-sensitive`: Case sensitive

## Filenames

* `-l` & `--files-with-matches`: List files with matches
* `-F`: Literal (no regular expression) search
* `-g` or `--glob`: Filter by filename
	* To do a negative glob, precede with `!`, e.g., `rg -g "!*.html" import`
* `--files`: Print each file but don't search
* `--files -g`: Search for files matching glob.
