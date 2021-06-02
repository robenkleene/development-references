# `fd`

- `-e`: Search by file extension
- `fd -e "md" . ./raster/`: Search a specific path without supplying a pattern (note the `.` as a pattern that matches everything)
- `fd -t d`: Specify only directories
- `-p` / `--full-path`: Search the full path, not just the filename, e.g., `fd --hidden -p "workflows" -e yml`
- `-H` / `--hidden`: Search hidden files
