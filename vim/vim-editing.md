# `vim` Editing

## Insert Mode

- `cc`: Enter insert mode at correct indent level

## Completion

- `^n`: Start auto-complete
- `^y`: Accept from auto-complete list
- `^e`: Cancel auto-complete

### Completion Types

- `^x^f`: File paths (after starting file path completion, `^f` selects a match and goes one deeper in the hierarchy)
- `^x^k`: Dictionary words

## Selecting

- `⌃v`: Visual Block Mode
- `gv`: Reselect last visual block

## Undo

- `u`: Undo
- `⌃r`: Redo

## Numbers

- `C-a` / `C-x`: Increment/decrement number

## Quick Tabs to Spaces

	set expandtab
	set shiftwidth=2
	" Retab document with `gg=G`
