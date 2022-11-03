# `vim` Shell

## Common

### Output in Echo Area

Note that the space after `w` is mandatory!

- `:.w !bash`: Current line
- `:w !bash`: File
- `:%w !bash`: File
- `:'<,'>w !bash`: Visual selection

### Replacing Selection

- `:'<,'>!sort`: Pipe visual selection through sort
- `:%!sort`: Pipe file through sort

### Appending Output to Current Buffer

- `:r !ls`: Read the output of `ls` into the buffer

## Special

- `!clear`: Clear the external command buffer
- `!!bash`: Execute current line in bash (note that this is a normal mode command, not a command line command)
- `:!%`: Run current file
