# Dired

## General

* `^`: Up directory
* `+`: Create directory
* `m`/ `u`: Mark / Remove mark
* `C-x C-f`: Create a new file (`ido-mode` interferes with this, just hit `C-f` to disable `ido-mode` to enter a filename. Although it doesn't actually appear to be necessary to disable `ido-mode` just hit enter to confirm creating a new file)
* `D`: Delete file

## Dired Write Mode

* `C-x C-q` or `dired-toggle-read-only`: Change to writable mode
	* `C-c C-c` or `C-x C-s`: Save changes
	* `C-c ESC`: Abort changes

## File Management

### Copying or Moving Files

- `R`: Rename or move file (`↓` inserts the current filename)
- `C`: Copy file

With `(setq dired-dwim-target t)`, if two `dired` buffers are open use the other one as the default destination.
