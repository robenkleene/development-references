# `zsh`

## Bindings

* `ESC-.`: Enter last parameter of previous command

## Options

* `setopt`: List enabled options
* `unsetopt`: List disabled options

## Help

* `man zshconrib`: Help for user contributions

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

### Key Bindings

* `man zshzle`: Some information about key bindings
* `bindkey -l`: List key maps
* `bindkey -M emacs`: List bindings for a key map
* `bindkey -L`: List currently active bindings

#### Key Maps

* `bindkey -M menuselect`: Bindings for tab menu
