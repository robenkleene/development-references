# `tr`

* `tr 'A-Z' 'a-z'`: Convert uppercase to lowercase

## Examples

Convert title case filenames with spaces to lowercase filenames with hyphens:

	for i in *; do { mv $i `echo $i | tr 'A-Z' 'a-z' | tr " " "-"` } done
