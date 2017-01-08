# Bundler

## Standalone 

1. Run `bundle init` to create a `Gemfile`
2. Add `.bundle` to `.gitignore`
3. Edit the `Gemfile` to add required gems
4. Run `bundle install --standalone`
5. Add `require_relative 'bundle/bundler/setup'` to the script

### Updating Gems

	bundle update
	bundle cleanup
	bundle install --standalone

Note that `bundle install --standalone` is necessary to update the `bundle/bundler/setup` to point to the new version of the gem.

## Changing the Ruby Version

1. Add `ruby '2.0.0'` to the `Gemfile`
2. Delete the `.bundle` directory
3. Delete the `bundle` directory
4. Delete the `Gemfile.lock` file
4. Run `bundle install --standalone`
