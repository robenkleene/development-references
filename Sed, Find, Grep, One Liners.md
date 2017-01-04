# One Liners

## Find Multiple Patterns

	grep -E "open class|open var"

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

## Sort Xcode Test Output by Performance

	grep "^Test Case.*passed" | sed -E 's/(.*)(\(.*\))/\2\1/' | sort -r

## Add Hierarchy to Xcode Test Output

	sed 's/^/			/' | sed 's/^			Test Suite/Test Suite/' | sed 's/^			Test Case/	Test Case/' | sed 's/^				 Executed/Executed/'
