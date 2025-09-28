# Visual Studio Code Find & Replace

- `⇧⌥F`: Find & replace in folder (when the Explorer has focus)
- `⇧⌘H`: Find & replace
- `⌘↓`: Go to first result
- `⇧⌘J`: Toggle search details

## Find & Replace in Multiple Files

1. `⇧⌘H`: Find & replace
2. `⌘⌥↩`: Replace all occurrences

## Find & Replace Occurrences

1. Select the text to replace
2. Use `⌘D` to add cursors for each additional occurrence

## Find & Replace in Selection

`Find & Replace Occurrences` is a usually a better approach if it's appropriate.

### Dialog

1. Select the term to replace and `Find with Selection` (`⌘E`)
2. Optional: Make a selection to replace in
3. Open find and replace with `⌥⌘F`
4. Toggle on `Find in selection` with `⌥⌘L`
5. Replace all with `⌘↩`

### Multiple Cursors

1. Select the term to replace and `Find with Selection` (`⌘E`)
2. Optional: Make a selection to replace in
3. Toggle on `Find in selection` with `⌥⌘L`
4. Make a cursor for each match with `⌥↩`

### Notes

- The `Auto Find in Selection` removed the need to toggle `Find in Selection` but it breaks this breaks using `⌘E` and `⌘G` to iterate through matches in a document.
