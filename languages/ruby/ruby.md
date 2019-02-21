# `ruby`

Run a focused unit test:

	ruby test/tc_window.rb --name test_two_windows

Break up long strings:

	string = "line #1"\
			 "line #2"\
			 "line #3"

## Performance Profiling

Just add:

	require 'profile'

The analysis will get printed to `STDIN`.

### Command Line

- `ruby -r profile`
- `rake -r profile`
