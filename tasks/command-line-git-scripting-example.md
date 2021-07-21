# Command-Line `git` Scripting Example

## Setup

1. `fd --hidden -p ".github/workflows/.*.yml"`: Find the files to be modified
2. `rg --hidden --multiline "runs-on: macos-latest\n    steps"`: Find the line to be modified
3. `rg -l --hidden --multiline "runs-on: macos-latest\n    steps"`: List the files to be modified
4. `dirname (rg -l --hidden --multiline "runs-on: macos-latest\n    steps") | uniq`: List the directories of the files to be modified
5. `for dir in (dirname (rg -l --hidden --multiline "runs-on: macos-latest\n    steps") | sort | uniq); cd $dir; echo $dir; git status; cd -; end`: Check the current `git` status in the directories to be modified
6. `for dir in (dirname (rg -l --hidden --multiline "runs-on: macos-latest\n    steps") | uniq); cd $dir; echo $dir; git checkout -b "add-timeout"; cd -; end`: Switch to a branch to make the edit

## Modification

1. `rg -l --hidden --multiline "runs-on: macos-latest\n    steps" -0 | xargs -0 sd -p 'runs-on: macos-latest\n' 'runs-on: macos-latest\n    timeout-minutes: 20\n'`: Preview the modification, then remove the `-p` to execute
2. `for v in (dirname (fd --hidden -p ".github/workflows/.*.yml")); git -C $v diff --quiet || echo $v; end`: Print the modified repos
