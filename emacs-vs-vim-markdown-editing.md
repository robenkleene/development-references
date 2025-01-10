# Emacs vs. Vim Markdown Editing

## Vim

### Pros

- Saving is easier
- Consistency with using Vim for editing

### Cons

- Syntax highlighting breaks with checkboxes followed by links

## Emacs

### Pros

- Emacs server allows editing the same file from multiple instances
- The return key works well for checking checkboxes and following links
- `⇥` indents a list item, rather than inserting a tab character
- File management with Dired is more effective
- Easier to close a window when we're finished with it
- With Emacs we can avoid the oddities with Vim's system clipboard interactions
- Emacs uses the directory of the current file by default when performing shell operations (e.g., to use a script to make a link to a relative file).
- Emacs supports `(setq markdown-enable-math t)` for Latex math wrapped in `$` or `$$`

### Cons

- Emacs doesn't handle a lot of buffers being moved underneath it at once well, e.g., when moving a directory externally  that has files and directories open in Emacs
- Eshell is a lot of duplication with regular shell in terminal, and encourages partial work that has to be migrated
- Organizing and renaming files in Emacs gets unwieldy and is error prone, because of the way future history works in this context (e.g., if there are other Dired buffers, it will use those paths first, which is sometimes helpful, but it is confusing when confusing when future history is also used for renaming)
