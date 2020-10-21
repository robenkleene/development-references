# fish

- Commands that start with a space, ` ls` will be hidden from history

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

## Debugging

- `fish_key_reader`: Show key stroke code for bind
- `fish --profile /tmp/fish.prof -ic exit`: Profiling

## Functions

- `type my_function`: Show definition of function
    - `type my_function | bat -l fish`: In a pager with syntax highlighting
- `funced`: Define an impromptu function
