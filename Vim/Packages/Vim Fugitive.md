# `vim` Fugitive

* `:Glog`: Load revisions of a file into the quickfix list (`[q` & `]q` go through versions of the file)
* `:Gstatus`: Git Status
	* `⌃N`: Next file
	* `⌃P`: Pervious file
	* `-`: Toggle git add (works with visual selection)
	* `↩`: Open file under cursor
	* `C`: Git Commit
* `:Gedit :path/to/file`: Edit index version of file
	* `:Gedit :0`: Edit index version of the current file
* `:Gdiff`: Left is index copy, right is working copy
	* `:Gwrite`: Writes which ever file is active to the index
	* `:Gread`: Replace the contents of this file with the version in the index
	* `:Gread` and `:Gwrite`: Reconcile the differences between the index version and the working copy version of a file by replacing one with the other (`:Gread` replaces this one with the other, `:Gwrite` replaces the other with this one)
	* `diffget` (shorthand `do`, for "diff obtain"): Takes the current range from the other file into this file
	* `diffput` (shorthand `dp`): Puts the change from this file in the other file
	* After doing `diffget` or `diffput`, you have to save (`:w`) the file to write it to the index
	* `diffupdate`: Update the diff highlighting, for if you've "confused `vimdiff`"
* `:Git diff`: Show diff output in pager
* `:Git! diff`: Show diff output in `vim` buffer

## `:Gstatus`

All of these act on the selected file.

* `dp`: Diff patch, like git output. To get back to where you where just do `<c-o>`, because this doesn't leave around a buffer.
* `D`: `vimdiff` diff, to exit this, do `<c-w><c-o>` (close other window)

## `:Gblame`

* `o`: Open current commit in a split (close it with `bd`)
