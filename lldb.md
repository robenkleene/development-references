# `lldb`

- `lldb <path-to-program>`: Load program
- `(lldb) file <path-to-program`: Load program
- `(lldb) process launch`: Start program
- `(lldb) run`: Start program
- `(lldb) r`: Start program
- `⌃D`: Quit

## Commands

- `step`
- `next`
- `continue`
- `s`: Step over
- `n`: Step in
- `↩`: Repeat the last command (e.g., `next`)
- `frame variable` / `fr v`: Show all variables in the current frame
- `print <variable>`: Print a variable
- `source list`: Display source code for the current target process
- `source info <file path>`: Display source line information for the current target process

## Breakpoints

Note that `b` is *not* simply shorthand for `breakpoint`, these commands require `breakpoint`.

- `breakpoint set -n`: Set a breakpoint by a symbol, e.g., for a function name
- `breakpoint set --file test.c --line 12` / `b test.c:12`
- `breakpoint list`: List breakpoints (note `b list` does not work)
- `breakpoint delete 1`
- `breakpoint enable 1`
- `breakpoint disable 1`
- `breakpoint delete`: Delete all breakpoints

## Debug Builds

### Linux

- `file`: Will say `not stripped` if it's a debug build
- `objdump --syms`: Dumps debug symbols

### macOS

- `otool -Iv`
