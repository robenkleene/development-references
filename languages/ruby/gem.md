# `gem`

## Building Gems

	gem build webconsole.gemspec

Installing a gem locally:

	gem install webconsole-0.0.0.gem

## Publish Ruby Gem

	gem push webconsole-0.0.3.gem

## Where are Gems installed?

Printing installation locations:

	gem env

## Viewing Gem source code

	gem open sass

Requires `gem-open`:

	gem install gem-open 

## Testing a Gem

	gem unpack websonsole-0.0.1.gem

Unpacks it in the current directory.

## Gem Cache

Clear gem cache:

	gem source --clean-all
	gem source -c
