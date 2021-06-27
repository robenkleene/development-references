# `fd`

- `-e`: Search by file extension
- `fd -t d`: Specify only directories
- `-p` / `--full-path`: Search the full path, not just the filename, e.g., `fd --hidden -p "workflows" -e yml`
- `-H` / `--hidden`: Search hidden files

## One Liners

- `fd --hidden "release.yml" --exec fish -c "cd {//}; pwd; git status"`: Perform commands
- `fd -e "md" . ./raster/`: Search a specific path without supplying a pattern (note the `.` as a pattern that matches everything)
