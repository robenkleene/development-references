# Vim Command Line

`:` to enter `Command-line-mode`

* `<C-r><C-f>`: Insert file under cursor
* `<C-r><C-w>`: Insert word under cursor
* `<C-r><C-a>`: Insert WORD under cursor
* `<C-r>%`: Insert name of current file
* `<C-c>` or `ESC`: Close command line and command line window
* `<cfile>`: Another reference to the cursor file, this is particularly useful with `e <cfile>` to start create the file at the cursor (`<C-r><C-f>` can also be used in this case).

## Examples

- `:!%`: Run current file
- `:.w !bash`: Run current line in bash
- `:%w !bash`: Run file in bash
- `:'<,'>!sort`: Pipe visual selection through sort
- `:read !ls`: Read the output of `ls` into the buffer

## Command Line Window

### Opening

- `q/`: Open search command line window
- `q:`: Enter command line window (normal history)
- `<C-f>`: Enter command line window from command line (command history)

### Closing

- `<C-w>c`: Close command line window, return to buffer
- `<C-c>`: Leave command line window open, return to command line

From the command line `<C-c>` (or `ESC`) will close the command line window and return to the buffer, so `<C-c><C-c>` also closes the command line window and returns to the buffer.

## `wildmenu`

- `<TAB>`: Show the wild menu
- `<UP>`: Move up in hierarchy
- `<DOWN>`: Move down in hierarchy
