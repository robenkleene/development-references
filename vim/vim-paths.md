# `vim` Paths

- `%`: Relative path
- `%:p`: Absolute path
- `%:h`: Head (parent)
- `%:t`: Tail (filename)
- `%:e`: File extension
- `%:r`: Filename without extension

## Command-Line Mode

- `<c-r>%`: Insert the relative path

## Insert Mode

- `<c-r>%`: Insert the absolute path
- `<c-r>=expand("%:p")`: Insert with a modifier
