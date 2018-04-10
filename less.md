# `less`

Command to do `less` like `git` pager:

	less -FXRS

* `-F` / `--quit-if-one-screen`: Quit if output is shorter than one screen
* `-X` / `--no-init`: Don't re-draw the screen after quit
* `-R` / `--RAW-CONTROL-CHARS`: Allow color
* `-S` / `--shop-long-lines`: Truncate long lines
