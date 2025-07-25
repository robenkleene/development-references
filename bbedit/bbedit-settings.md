# BBEdit Settings

- Toggle off `Preferences > Application > Open documents into the front window when possible` because it's more flexible to use multiple windows
- Toggle off `Preferences > Editing > Display instances of selected text` because it's distracting when writing prose
- Toggle off `Preferences > Completion > Insert matching delimiters while typing` because otherwise it's hard to add Markdown code blocks with three backticks
- Toggle on `Preferences > Text Files > Strip trailing whitespace` since BBEdit doesn't have a good way to show trailing whitespace, this helps prevent it
- Set `Preferences > Completion > Show text completions: Only manually` because it's distracting when writing prose otherwise
- Toggle on `Preferences > Editor Defaults > Soft wrap text to: Page guide` because it's better for writing prose

## Expert Settings

Make `⌥⌫` delete the entire previous word instead of just the space:

```
defaults write com.barebones.bbedit Editor_ModernWordMovement -bool YES
```

Revert this setting with:

```
defaults delete com.barebones.bbedit Editor_ModernWordMovement
```

## Languages

- Set `Preferences > Languages > New Documents: Markdown`
- Under `Preferences > Languages > Custom Settings` Add Markdown and set `Editor: Soft wrap text to: Page guide` the provides the best balance of wrapping Markdown and not wrapping code

## Font

BBEdit will automatically use `Consolas` and `Inconsolata` if it's installed.
