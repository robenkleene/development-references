# `tee`

Pipe to `stdout` and print to the terminal at the same time:

	echo "test" | tee /dev/tty | pbcopy

Pipe `stdout` to multiple commands:

	xcodebuild | xcpretty | tee >(mate) | wc -l

Pipe to a file and `stdout`:

	xcodebuild | tee build.log
