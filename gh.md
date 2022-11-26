# `gh`

## `pr create`

- `-B` / `--base`: Specify the branch you want your code merged into

## Basic

- `gh pr create`: Create PR
- `gh pr merge`: Merge PR (while on the current branch to be merged)

## Examples

Create a pull request into `master`:

	gh pr create

Create a pull request into a different branch:

	gh pr create -B <branch name>

Open pull request creation page in the browser:

	gh pr create --web

