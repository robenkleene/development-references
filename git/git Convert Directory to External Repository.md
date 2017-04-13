# `git` Convert to External Repository

Useful for convert a single folder to a submodule or a Frameworks while preserving history.

	# Startout with a fresh checkout:
	git clone git@github.com:robenkleene/webconsole.git XCTestTemp
	
	# Extract a specific directory:
	git filter-branch --prune-empty --subdirectory-filter Web\ Console/XCTestTemp master
	
	# Clean up unnecessary data
	git reflog expire --expire=now --all
	git repack -ad  # Remove dangling objects from packfiles
	git prune       # Remove dangling loose objects
	
	# Detach from origin
	git remote remove origin
	
	# Delete all tags
	git tag | xargs git tag -d
	
	# Rename the branch to master
	git branch --move master

