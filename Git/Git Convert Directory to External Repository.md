# Git Convert to External Repository

For making submodules, Frameworks, etc...

	# Startout with a fresh checkout:
	git clone git@github.dowjones.net:DJMobile/ios-thesituation.git IssueKit
	
	# Extract a specific directory:
	git filter-branch --prune-empty --subdirectory-filter ExJsonKit development
	
	# Clean up unnecessary data
	git reflog expire --expire=now --all
	git repack -ad  # Remove dangling objects from packfiles
	git prune       # Remove dangling loose objects
	
	# Detach from origin
	git remote remove origin
	
	# Delete all tags
	git tag | xargs git tag -d
	
	# Rename Development Branch to master
	git branch --move master
