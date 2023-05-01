# `lldb`

- `lldb <path-to-program>`: Load program
- `(lldb) file <path-to-program`: Load program
- `(lldb) process launch`: Start program
- `(lldb) process launch -i <file-path>`: Start program, passing `<file-path>` to the programs STDIN
- `(lldb) process launch -i <file-path>`: Start program with STDIN and arguments
- `(lldb) run`: Start program
- `(lldb) r`: Start program
- `⌃D`: Quit

## Shorthand

- `r <parameters>`: Run passing parameters to the executable
- `n`: Step over
- `s`: Step in
- `c`: Continue
- `↩`: Repeat the last command (e.g., `next`)
- `b test.c:12`
- `fr s`: Print current line

## Commands

- `run <parameters>`: Run passing parameters to the executable
- `step`
- `next`
- `continue`
- `frame select 0` / `fr s 0`: Print the current frame information (e.g., current source code line)
- `source list`: Display source code for the current target process
- `source info <file path>`: Display source line information for the current target process
- `⌃C`: Seems to stop the process?

## Variables

- `frame variable` / `fr v`: Show all variables and arguments in the current frame
- `frame variable --no-args` / `fr v a`: Show only all variables in the current frame
- `frame variable <variable>` / `fr v <variable>`: Show value of frame `<variable>`
- `target variable` / `ta v`: Show all global (and static) variables defined in the current source file
- `target variable <variable>` / `ta v <variable>`: Show value of target `<variable>`
- `print <variable>`: Print a variable

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
