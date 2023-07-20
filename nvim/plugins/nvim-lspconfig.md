# `nvim` `lspconfig`

- `q`: Dismiss floating overlay

## Bindings

There's no way to scroll the popup window, instead you have to focus it, and then navigate within it.

## Troubleshooting

For "other clients that match the filetype":

- Try `LspStart`
- Try running the LSP command directly, e.g., `rust-analyzer` was failing with `error: 'rust-analyzer' is not installed for the toolchain 'stable-x86_64-unknown-linux-gnu'`
