# Visual Studio Code CLI

- `-r` / `--reuse-window`: Re-use an existing window (e.g., `code -r .` will replace the currently open project with the current directory from the terminal)
- `-n` / `--new-window`: Create a new window

## Extensions

- `code --list-extensions`: List extensions

## Opening at Line Number

	code -g
	code --goto

### Example:

	code -g /Users/robenkleene/Development/Projects/Cocoa/Repla/Packages/Jekyll.replaplugin/Contents/Resources/bundle/ruby/2.4.0/gems/jekyll-4.0.0/lib/jekyll/theme.rb:74
