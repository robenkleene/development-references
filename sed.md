# `sed`

## Remove Spaces

	sed 's/ //g'

## Replace Multiple Spaces With One Space

	sed "s/  */ /g"

## Capture Groups

	sed 's/.*:\(.*\):.*/\1/p'`

Another example:

    sed -E 's/^( *-) */\1 /g'

Note that the `-E` flag inverts whether the parentheses need to be escaped.
