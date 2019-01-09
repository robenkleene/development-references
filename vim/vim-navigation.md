# `vim` Navigation

## `vim` Marks

- `ma`: Make mark called `a`
- ```a``: Go to `x` (line and column)
- `'x`: Go to `x` (line only)
- `:marks`: List marks

### Special Marks

- `.`: Last change
- `[` and `]`: Beginning and end of last yank or change
- `<` and `>`: Beginning and end of last visual selection

## Operating What's Under Cursor

* `gx`: Open URL under cursor
* `gf`: Open file under cursor
- `<C-w>gf`:  Open the file under the cursor in a new tab
- `<C-w>f`:  Open the file under the cursor in a new split

## Jump List

- `:[ju]mps`: Show the `jumplist`
- `<C-o>`: Go to the previous position in the `jumplist`
- `<C-i>`: Go to the next position in the `jumplist`

## Buffers

- `:ls`: List open buffers
- `:b[uffer]`: go to buffer number 
- `:bd`: Close buffer

## `argslist`

- `:args`: Show the contents of the `argslist`
- `:next`: Next file
- `:prev`: Previous file

Once files have been opened as arguments, `##` can be used to represent them in `ex` commands, e.g.:

	:vimgrep /Lorem/ ##

## Language Specific

* `]}` & `[{`: Go to next or previous brace (only works from inside a brace pair)
* `]m` & `[m`: Go to next or previous method

## View

* `zz`: Center cursor
* `zt`: Top cursor
* `zb`: Bottom cursor
* `zs`: Cursor end
* `ze`: Cursor beginning
