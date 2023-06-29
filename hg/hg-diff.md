# `hg` Diff

- `hg diff -r .^1`: Diff of last commit plus local changes
- `hg diff -r bottom^`: Diff master
- `hg diff --root .`: Relative
- `hg diff -r bottom^ --stat`: Diff stats, including just change filenames
- `hg status --change .`: List uncommitted changed files
- `hg status --change bottom^`: List changed files on current branch
- `hg status --rev bottom^`: List all changed files on current branch
- `hg status --rev bottom^ -n`: Omit the per file statuses
