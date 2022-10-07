 Dired

## General

- `^`: Up directory
- `+`: Create directory
- `m`/ `u`: Mark / Remove mark
- `C-x C-f`: Create a new file (`ido-mode` interferes with inserting spaces in a filename, to get around those use `C-f` to drop down to the default `find-file` interface)
- `D`: Delete file
- `s`: Toggle between alphabetical and date sorting

## Multiple Files

- Use `m` to mark and then another command, e.g., `R` to move all

## Sorting

- `s`: Toggle sort by name or date
    - `(`: Toggle showing details
- `C-u s`: Set specific flags to pass to `ls`

## Dired Write Mode

- `C-x C-q` or `dired-toggle-read-only`: Change to writable mode
	- `C-c C-c` or `C-x C-s`: Save changes
	- `C-c ESC`: Abort changes

## File Management

### Copying or Moving Files

- `R`: Rename or move file (`↓` inserts the current filename)
- `C`: Copy file

With `(setq dired-dwim-target t)`, if two `dired` buffers are open use the other one as the default destination.

To move a file to a new directory, do a rename, but just specify a directory as a path, and the file will be moved with the existing file name.
