# `lldb`

- `lldb <path-to-program>`: Load program
- `(lldb) file <path-to-program`: Load program
- `(lldb) process launch`: Start program
- `(lldb) run`: Start program
- `(lldb) r`: Start program


## Breakpoints

Note that `b` is *not* simply shorthand for `breakpoint`, these commands require `breakpoint`.

- `breakpoint set --file test.c --line 12` / `b test.c:12`
- `breakpoint list`
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
