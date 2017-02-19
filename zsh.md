# `zsh`

## Help

* `man zshconrib`: Help for user contributions

## Customization

List available colors:

	for code in {000..255}; do print -P -- "$code: %F{$code}Test%f"; done

Named colors

	autoload colors && colors
	echo ${(o)color} # or which colors
