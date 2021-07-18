# Command-Line `git` Scripting Example

## Setup

1. `fd --hidden -p ".github/workflows/.*.yml"`: Find the files to be modified
2. `rg --hidden --multiline "runs-on: macos-latest\n    steps"`: Find the line to be modified
3. `rg -l --hidden --multiline "runs-on: macos-latest\n    steps"`: List the files to be modified
4. `dirname (rg -l --hidden --multiline "runs-on: macos-latest\n    steps") | uniq`: List the directories of the files to be modified
5. `for dir in (dirname (rg -l --hidden --multiline "runs-on: macos-latest\n    steps") | sort | uniq); cd $dir; echo $dir; git status; cd -; end`: Check the current `git` status in the directories to be modified
6. `for dir in (dirname (rg -l --hidden --multiline "runs-on: macos-latest\n    steps") | uniq); cd $dir; echo $dir; git checkout -b "add-timeout"; cd -; end`: Switch to a branch to make the edit

## Modifying

- `sd -p 'runs-on: macos-latest\n' 'runs-on: macos-latest\ntimeout-minutes: 20\n' OutOfTouch/.github/workflows/ci.yml`
- `sd -p '    runs-on: macos-latest\n' '    runs-on: macos-latest\n    timeout-minutes: 20\n' .github/workflows/ci.yml`
