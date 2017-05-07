# `tr`

* `tr 'A-Z' 'a-z'`: Convert uppercase to lowercase

## Examples

Rename file and directories using title case with spaces to lowercase with hyphens:

	for i in *; do { mv $i `echo $i | tr 'A-Z' 'a-z' | tr " " "-"` } done
