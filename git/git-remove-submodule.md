# `git` Remove Submodule

# Old Method

To remove a submodule you need to:

1. Delete the relevant section from the `.gitmodules` file.
2. Stage the `.gitmodules` changes `git add .gitmodules`
3. Delete the relevant section from `.git/config`.
4. Run `git rm --cached path_to_submodule` (no trailing slash).
5. Run `rm -rf .git/modules/path_to_submodule`
6. Commit `git commit -m "Removed submodule <name>"`
7. Delete the now untracked submodule files `rm -rf path_to_submodule`

## New Method

1. `git submodule deinit -f path/to/submodule`: Remove the submodule entry from `.git/config`
2. `rm -rf .git/modules/path/to/submodule`: Remove the submodule directory from `.git/modules`
3. `git rm -f path/to/submodule`: Remove the entry in `.gitmodules` and remove the submodule directory
