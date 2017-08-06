# `xcodebuild`

## Build

	xcodebuild -alltargets -configuration Debug

* `-configuration Debug`: Configuration must be `Debug`, otherwise targets that use `@testable` will fail.
* `-alltargets`: Test targets won't be built without this


## Test

## Other Commands

* `xcodebuild -list`: List the schemes