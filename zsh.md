# `zsh`

## Line Editor

* `^X^U`: undo
* `^Xu`: undo
* `^_`: undo
* `!#:$`: Insert last parameter in current line
* `!#:1`: Insert any previous parameter in current line (`1` maps to the parameter spot)

## Bindings

* `^[.`: Enter last parameter of previous command
* `^[^-`: Insert previous word
* `^-`: Undo

## Expansion

* `!!:n-$`: `n`'th argument to last from previous command
* `!-i:n-$`: `n`'th argument to last from command `i` commands ago
* `!!:1-$`: All argument from previous command

### Bindings Configuration

* `man zshzle`: Some information about key bindings
* `zle -la`: List all available commands to bind
* `bindkey -l`: List key maps
* `bindkey -M emacs`: List bindings for a key map
* `bindkey -M menuselect`: Bindings for tab menu
* `bindkey -L`: List currently active bindings

Simple way to get a key code: hit `^v` then the key.

## Completion

* `rehash`: Rebuild auto-complete index

## Options

* `setopt`: List enabled options
* `unsetopt`: List disabled options

## Help

* `man zshconrib`: Help for user contributions
* `^[h`: Get help for current command

## Menu

When the menu is visible to select various options.

- `^g`: Cancel

## Customization

### Colors

List available colors:

	for code in {000..255}; do print -P -- "$code: %F{$code}Test%f"; done

Named colors

	autoload colors && colors
	echo ${(o)color} # or which colors

### Prompt

* `man zshmisc`: `/SIMPLE PROMPT ESCAPES` has a list of escape sequences
