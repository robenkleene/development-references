# Visual Studio Code Window Management

- `⌘1` Focus editor
- `⌘0`: Focus currently active sidebar

## Bottom Panel

- `⌃backtick`: Toggle Terminal
- `⌥⌘M`: Show Problems
- `⌘B`: Toggle sidebar
- `⌘J`: Toggle bottom panel
- `View: Toggle Maximized Panel`: Maximize the panel

### Sidebar

- `⇧⌘E`: Focus Explorer (files)
    - There's a `File: Reveal Active File in Sidebar` command, but there's no default shortcut for it
- `⌘K ⌘W`: Close all editors
- `⌘K F` (`File > Close Folder`): Close folder in workspace (e.g., if there's only one open folder this will result in an empty document)
- `⌘K E`: Focus open editors
- `⌘-click` in sidebar: Select a file without opening it, or select a directory without expanding it
- `⌘K ⌘0`: Collapse folders in sidebar (note that this will not collapse search results unfortunately)

### Tabs

- `⇧⌘T`: Re-open last closed tab

### Splits

- `⌘⌥0`: Toggle between horizontal and vertical splits
- `⌘\`: Split the editor vertically
- `⌘K ⌘\`: Split editor horizontally
- `⌥⌘←` / `⌥⌘→`: Focus left / right editor
- `^⌘←` / `^⌘→`: Move a split left / right

The tab navigation keys (`⇧⌘[` / `⇧⌘]`) also work to go between side-by-side splits.

There's no shortcut to close splits, but "View: Single Column Editor Layout" is a command that does this.

## Explorer

- `⌃↩`: Open file in a split
- `␣`: Open file

## Terminals

- `⇧^backtick`: Make new Terminal (there are not default keybindings to switch between these)

## Quick Open

After using `⌘P` to fuzzy open a file:

- `↩`: Opens in a new tab
- `⌘↩`: Opens in a new vertical split
- `⌥↩`: Opens in a new vertical split
- `⌃↩`: Opens in a new vertical split

There does not appear to be a way to open a file from Quick Open in a horizontal split, as a workaround, first open the file in vertical split and then use `⌘⌥0` to swap the layout.

## Preview

- `⌘K ↩` / `View: Keep Editor`: Exit preview mode
- Filenames in italics are in preview mode
- To quickly preview lots of files from the sidebar, use `␣` to preserve the focus while previewing a file.

## Tips

To quickly preview files in succession, when the Explorer has focus use `␣` to open the file. The Explorer will maintain focus and you can go to the next file with the arrow keys, and hit `␣` to open a different file.

### Untitled in Split

A trick to get an untitled window in a split, first use `⌘N` to create a new untitled file, then use `Move Editor into Below Group` to move it to a horizontal split.
