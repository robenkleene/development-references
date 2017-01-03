# fish

## History

* `history merge`: Merge history from all running sessions

## Iterate Directories

Checkout master, reset, clean dead branches.

	for directory in */
       echo "Entering $directory"
       cd $directory
       git-reset
       git checkout master
       git pull
       git-reset
       git-prune-remote-origin 
       cd ..
	end
