# Visual Studio Code Snippets

## Creating

The easiest way to create a complex snippet, with multiple lines and escaped characters, is to leverage multiple cursors.

1. Select the multi-line snippet
2. Enter multiple cursors (`⇧⌘I`).
3. Go to the beginning of each line (`⌃A`)
4. Hit delete, and then entire `\n`.
5. Select a character that needs escaping and do a find for it with `⌘E`. Select the entire line, make sure `Find in selection` is on (`⇧⌘L`). Hit `⌥↩` to create a cursor for each selection match.