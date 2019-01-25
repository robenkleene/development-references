# Gem Management

## System Ruby

Use system Ruby for Repla:

	chruby system

When installing system gems, use `--user-install` to avoid cluttering the system Ruby space:

	gem install --user-install test-unit

This installs gems at `/Users/robenkleene/.gem/ruby/2.3.0`. (Note that this does not require `sudo`.)

Since the default executable path is not setup by default, bundler must specify it when being installed:

	gem install --user-install bundler --bindir /usr/local/bin

## Correct Installation

Here's how Bundler should work after being correctly installed:

	$ which bundle
	/Users/robenkleene/.gem/ruby/2.5.3/bin/bundle
	$ chruby system
	$ which bundle
	/usr/local/bin/bundle

Note that for system Ruby, the gem directory is `2.3.0` (not `2.3.7`):

	$ ls .gem/ruby
	2.3.0  2.5.3