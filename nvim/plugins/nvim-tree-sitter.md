# `nvim` Tree-Sitter

## Customizing Colors

- `TSPlaygroundToggle`: Use the `treesitter-playground` (with the plugin installed) in order to get the Treesitter syntax groups
- `TSCaptureUnderCursor`: Show the groups at cursor

## Troubleshooting

- Don't run `TSInstall all`, that installs all parsers
- The required parsers should just be auto-installed on startup
- Using `TSInstall <language>` to re-install a parser can help
- `:checkhealth nvim-treesitter` gives some diagnostic information

### Fixing Query Node Errors

```
:echo nvim_get_runtime_file('parser', v:true)
```

### Installation Directory

- Tree-Sitter parsers are installed to `~/.local/share/nvim/site/pack/packer/start/nvim-treesitter`
