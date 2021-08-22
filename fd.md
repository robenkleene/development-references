# `fd`

- `-e`: Search by file extension
- `fd -t d`: Specify only directories
- `-p` / `--full-path`: Search the full path, not just the filename, e.g., `fd --hidden -p "workflows" -e yml` (This seems to be incompatible with the `-g` glob flag, e.g., `fd --full-path -g "name*json"` will not work)
- `-H` / `--hidden`: Search hidden files
- `-I` / `--no-ignore`: Include ignored files

## One Liners

- `fd --hidden "release.yml" --exec fish -c "cd {//}; pwd; git status"`: Perform commands
- `fd -e "md" . ./raster/`: Search a specific path without supplying a pattern (note the `.` as a pattern that matches everything)

## Troubleshooting

- `fd` doesn't search full paths by default, so `rg "dir.*file"` won't find a `file` in a `dir`, but `fd -p "dir.*file"` will

