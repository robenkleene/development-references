# fish

## Scripting

Numeric values don't need to be quoted:

    if test $status -eq 0
        echo -n (basename $git_path)
    end

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

## Debugging

- `fish_key_reader`: Show key stroke code for bind

## Functions

- `type my_function`: Show definition of function
    - `type my_function | bat -l fish`: In a pager with syntax highlighting
- `funced`: Define an impromptu function
