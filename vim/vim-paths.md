# `vim` Paths

- `%`: Path
- `%:p`: Full path
- `%:h`: Head (parent)
- `%:t`: Tail (filename)
- `%:e`: File extension
- `%:r`: Filename without extension

## Command-Line Mode

- `<c-r>%`: Insert the path

## Insert Mode

- `<c-r>%`: Insert the path
- `<c-r>=expand("%:p")`: Insert with a modifier
