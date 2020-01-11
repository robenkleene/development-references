# Escape Sequences

- To print the escape sequence for a key in a shell, print `⌃v` then the character.

## Hex Sequences

To print the hex sequence for a key use `xxd`.

1. Run `xxd`
2. Hit `⌃v` then the key
3. Hit return to separate the output visually, then hit `⌃d` for end of file.

### Example Output

For `⌃z`:

	% xxd
	^Z
	00000000: 1a0a

Result is `1A` (`0a` is the line feed, same sequence for return).
