# `vim` Shell Commands

## Common

### Output in Echo Area

Note that the space after `w` is mandatory!

- `:.w !bash`: Current line
- `:w !bash`: File
- `:%w !bash`: File
- `:'<,'>w !bash`: Visual selection (note this only works for *line-wise* selection, sub-line selection will not work! This is because `:` `ex` commands are all line based)

### Replacing Selection

- `:'<,'>!sort`: Pipe visual selection through sort
- `:%!sort`: Pipe file through sort

### Appending Output to Current Buffer

- `:r !ls`: Input the result of a shell command below the current line
- `:0r !ls`: Input the result of a shell command at the beginning of the document

## Special

- `!clear`: Clear the external command buffer
- `!!bash`: Execute current line in bash (note that this is a normal mode command, not a command line command)
- `:!%`: Run current file
