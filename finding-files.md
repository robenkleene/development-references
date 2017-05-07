# Finding Files

To find files use an `ack`-like because it supports a `NUL` byte and automatically ignores files:

	rg --files -g '*.md'

(`rg` does not list directories)

To find directories use `find`, because it supports a `NUL` byte:

	find **/*.md -type d

Only use `ls` for quick listing not analysis, because it doesn't support a `NUL` byte. In a pinch, a good work-around is:

	ls | tr '\n' '\0'
