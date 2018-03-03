# `zsh` Programming

Most of this kind of documentation is found in `man zshexpn`.

## Associative Arrays

	typeset -A abbreviations

	assoc=(
	'key1' 'value1'
	'key2' 'value2'
	)

### Parameter Expansion Flags

List all keys:

	${(k)assoc}

Ascending order

	${(o)assoc}
