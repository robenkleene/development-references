# Dired

## General

* `^`: Up directory
* `+`: Create directory
* `C-x C-f`: Create a new file

## Dired Write Mode

* `C-x C-q` or `dired-toggle-read-only`: Change to writable mode
	* `C-c C-c` or `C-x C-s`: Save changes
	* `C-c ESC`: Abort changes

## File Management

### Copying or Moving Files

- `R`: Rename or move file
- `C`: Copy file

With `(setq dired-dwim-target t)`, if two `dired` buffers are open use the other one as the default destination.
