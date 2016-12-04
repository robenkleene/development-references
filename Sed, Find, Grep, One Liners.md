# One Liners

## Find Matching Glob

	find . -name '*.py'
	# Case-Insensitive
	find . -iname "*write*"

## Delete Blank Lines

	grep .

## Remove Spaces

	sed 's/ //g'

## Print Group Match

	sed -n 's/.*:\(.*\):.*/\1/p'`

* `-n` suppresses outputting every line to only show matches.