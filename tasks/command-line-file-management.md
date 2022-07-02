# Command-Line File Management

## One Parameter

- `mkdir <path>`: Make a directory
- `mkdir -p <path>`: Make a directory including intermediary directories
- `rmdir <path>`: Remove an empty directory
- `rm -r <path>`: Delete directory

## Two Parameters

- `cp <source> <destination>`: Copy a file
- `cp <source> <destination>/`: Copy a file into a directory
- `cp -R <source> <destination>`: Duplicate a directory
- `cp -RT <source> <destination>`: Overwrite a directory
- `cp -R <source> <destination>/`: Copy a directory into a directory
- `cp -R <source>/ <destination>/`: Copy the contents of a directory into a directory
- `mv <source> <destination>`: Rename a file or directory
- `mv <source> <destination>/`: Move a file or directory into another directory
- `mv <source>/* <destination>`: Move contents of a directory
