# Visual Studio Code Extensions

- `code --list-extensions`: List extensions
- `code --list-extensions >> vs_code_extensions_list.txt`: Store extensions
- `cat vs_code_extensions_list.txt | xargs -n 1 code --install-extension`: Re-install extensions

## Extension Development

- The default extension template sets up a debug action so the extension can be tested with `F5`
