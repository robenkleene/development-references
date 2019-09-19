# `git` Remove Submodule

## New Method

Just use the `git_submodule_delete` script which automates these steps:

1. `git submodule deinit -f path/to/submodule`: Remove the submodule entry from `.git/config`
2. `rm -rf .git/modules/path/to/submodule`: Remove the submodule directory from `.git/modules`
3. `git rm -f path/to/submodule`: Remove the entry in `.gitmodules` and remove the submodule directory
