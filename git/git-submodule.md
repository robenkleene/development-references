# `git` Submodule

## Add

	git submodule add git@github.com:repla-app/HTML.replaplugin.git Repla/Packages/HTML.replaplugin

## Remove

Just use the `git_submodule_delete` script which automates these steps:

1. `git submodule deinit -f path/to/submodule`: Remove the submodule entry from `.git/config`
2. `rm -rf .git/modules/path/to/submodule`: Remove the submodule directory from `.git/modules`
3. `git rm -f path/to/submodule`: Remove the entry in `.gitmodules` and remove the submodule directory

## Switch from `git` to `https`

(Or vice versa.)

Edit `.gitmodules` and update the URL, then `git submodule sync`
