# `grep`, `find`, `sed`, One Liners

## Find & Replace in Place

	ack -i -l --print0 "foo" | xargs -0 sed -i '' "s/foo/bar/g"

Add `-i ''` to sed to run

## Find Multiple Patterns

	grep -E "open class|open var"

## `grep` Quick Case Insensitive

	[c|C]hecker

## Find Matching Glob

	find . -name '*.py'
	# Case-Insensitive
	find . -iname "*write*"

## Remove Spaces

	sed 's/ //g'

## Print Group Match

	sed -n 's/.*:\(.*\):.*/\1/p'`

* `-n` suppresses outputting every line to only show matches.

## Sort Xcode Test Output by Performance

	grep "^Test Case.*passed" | sed -E 's/(.*)(\(.*\))/\2\1/' | sort -r

## Add Hierarchy to Xcode Test Output

	sed 's/^/			/' | sed 's/^			Test Suite/Test Suite/' | sed 's/^			Test Case/	Test Case/' | sed 's/^				 Executed/Executed/'
