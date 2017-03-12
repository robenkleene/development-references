# `rg`

* `-i` & `--ignore-case`: Ignore case
* `-s` & `--case-sensitive`: Case sensitive
* `-F`: Literal (no regular expression) search
* `--null`: Use NUL byte terminator

## Filenames

* `-l` & `--files-with-matches`: List files with matches
* `-g` or `--glob`: Filter by filename
	* To do a negative glob, precede with `!`, e.g., `rg -g "!*.html" import`
	* To match multiple file extensions, use a character group: `rg -g '*.[hm]'`
* `--files`: Print each file but don't search
* `--files -g`: Search for files matching glob.
