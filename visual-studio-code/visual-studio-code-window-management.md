# Visual Studio Code Window Management

- `⌘1` Focus editor
- `⌘0`: Focus currently active sidebar

## Bottom Panel

- `⌃backtick`: Toggle Terminal
- `⌘B`: Toggle sidebar
- `⌘J`: Toggle bottom panel

### Sidebar

- `⇧⌘E`: Focus Explorer (files)
- `⌘K ⌘W`: Close all editors
- `⌘K F` (`File > Close Folder`): Close folder in workspace (e.g., if there's only one open folder this will result in an empty document)
- `⌘K E`: Focus open editors
- `⌘-click` in sidebar: Select a file without opening it, or select a directory without expanding it
- `⌘K ⌘0`: Collapse folders in sidebar (note that this will not collapse search results unfortunately)

### Splits

- `⌘⌥0`: Toggle between horizontal and vertical splits
- `⌘\`: Split the editor vertically
- `⌘K ⌘\`: Split editor horizontally
- `⌘⌥←` / `⌘⌥→`: Focus left / right editor

The tab navigation keys (`⇧⌘[` / `⇧⌘]`) also work to go between side-by-side splits.

There's no shortcut to close splits, but "View: Single Column Editor Layout" is a command that does this.

## Explorer

- `⌃↩`: Open file in a split
- `␣`: Open file

## Quick Open

After using `⌘P` to fuzzy open a file:

- `↩`: Opens in a new tab
- `⌘↩`: Opens in a new vertical split
- `⌥↩`: Opens in a new vertical split
- `⌃↩`: Opens in a new vertical split

There does not appear to be a way to open a file from Quick Open in a horizontal split, as a workaround, first open the file in vertical split and then use `⌘⌥0` to swap the layout.

## Tips

To quickly preview files in succession, when the Explorer has focus use `␣` to open the file. The Explorer will maintain focus and you can go to the next file with the arrow keys, and hit `␣` to open a different file.