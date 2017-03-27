# `zsh`

## Editing

* `^_` or `^Xu` or `^X^U`: Undo
* `^[.`: Insert last parameter of previous command
* `^[^-`: Insert previous word
* `^[h`: Help for current command (runs `man`)
* `^[q`: Push current line (clears the line, execute one command and then return the line)

### Substitutions

#### History

* `!-1` or `!!`: Expand previous command

#### Parameters
* `!#:$`: Insert last parameter in current line
* `!#:1`: Insert any previous parameter in current line (`1` maps to the parameter spot)
* `!!:n-$`: `n`'th argument to last from previous command
* `!-i:n-$`: `n`'th argument to last from command `i` commands ago
* `!!:1-$`: All argument from previous command

### Menu

When the menu is visible to select various options.

- `^g`: Cancel

## Commands

* `rehash`: Rebuild auto-complete index
* `setopt`: List enabled options
* `unsetopt`: List disabled options

### Bindings

* `zle -la`: List all available commands to bind
* `bindkey -l`: List key maps
* `bindkey -M emacs`: List bindings for a key map
* `bindkey -M menuselect`: Bindings for tab menu
* `bindkey -L`: List currently active bindings

Simple way to get a key code: hit `^v` then the key.

## Help

* `man zshconrib`: Help for user contributions
* `man zshzle`: Some information about key bindings

## Customization

### Colors

List available colors:

	for code in {000..255}; do print -P -- "$code: %F{$code}Test%f"; done

Named colors

	autoload colors && colors
	echo ${(o)color} # or which colors

### Prompt

* `man zshmisc`: `/SIMPLE PROMPT ESCAPES` has a list of escape sequences

## Redirection

`1` is `stdout` and `2` is `stderr`.

* `1>filename` or `>filename`: Redirect `stdout` to a file
* `1>>filename` or `>>filename`: Redirect and append `stdout` to a file
* `2>filename`: Redirect `stderr` to a file
* `2>>filename`: Redirect and append `stderr` to a file
* `&>filename`: Redirect `stdout` and `stderr` to a file
* `2>&1`: redirect `stderr` to `stdout`
* `>/dev/null 2>&1`: Discard `stdout` and `stderr`
* `>/dev/null`: Discard `stdout`
