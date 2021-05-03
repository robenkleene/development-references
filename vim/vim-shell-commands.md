# `vim` Shell Commands

- `:!%`: Run current file
- `:.w !bash`: Run current line in bash (or another command)
- `:w !bash`: Run file in bash (or another command)
- `:%w !bash`: Run file in bash (or another command)
- `:'<,'>w !bash`: Run visual selection in bash
- `:'<,'>!sort`: Pipe visual selection through sort
- `:%!sort`: Pipe file through sort
- `:r !ls`: Read the output of `ls` into the buffer
- `!clear`: Clear the external command buffer
- `!!bash`: Execute current line in bash (note that this is a normal mode command, not a command line command)

