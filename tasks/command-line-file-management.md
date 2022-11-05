# Command-Line File Management

## One Parameter

- `mkdir <path>`: Make a directory
- `mkdir -p <path>`: Make a directory including intermediary directories
- `rmdir <path>`: Remove an empty directory
- `rm -r <path>`: Delete directory

## Two Parameters

- `<cp-or-mv> <source> <destination>`: Copy or rename
- `<cp-or-mv> <source> <destination>/`: Copy or move into a directory
- `<cp-or-mv> <source>/* <destination>`: Move contents of a directory
- `cp -R <source> <destination>`: Duplicate a directory
- `cp -RT <source> <destination>`: Overwrite a directory
- `cp -R <source> <destination>/`: Copy a directory into a directory
- `cp -R <source>/ <destination>/`: Copy the contents of a directory into a directory

## Other

- `df -h`: Show available disk space
