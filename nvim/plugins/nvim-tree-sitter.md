# `nvim` Tree-Sitter

## Customizing Colors

- `TSPlaygroundToggle`: Use the `treesitter-playground` (with the plugin installed) in order to get the Treesitter syntax groups
- `TSCaptureUnderCursor`: Show the groups at cursor

## Troubleshooting

- Start with `TSUpdate` if something seems broken
- Don't run `TSInstall all`, that installs all parsers
- The required parsers should just be auto-installed on startup
- Using `TSInstall <language>` to re-install a parser can help
- `:checkhealth nvim-treesitter` gives some diagnostic information
- If parsers are constantly being re-compiled, run `:checkhealth` and search for `packer`, if packer is also there, that path should probably be deleted

### Fixing Query Node Errors

Check which paths parsers are installed at:

```
:echo nvim_get_runtime_file('parser', v:true)
```

If any parsers are in a directory that's not owned by the treesitter plugin, than those parsers must also be installed by treesitter so the plugin finds the override versions.

### Installation Directory

- Tree-Sitter parsers are installed to `~/.local/share/nvim/site/pack/packer/start/nvim-treesitter`
