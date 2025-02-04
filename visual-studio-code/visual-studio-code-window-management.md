# Visual Studio Code Window Management

## Editors

- `⌘1` Focus editor
- `⌘K ⌘W`: Close all editors

## Sidebar

- `⌘B`: Toggle sidebar
- `⌘0`: Focus currently active sidebar

### Sidebar Tabs

- `⇧⌘E`: Focus Explorer (files)
    - There's a `File: Reveal Active File in Sidebar` command, but there's no default shortcut for it
- `⇧⌃G`: Source control
- `⇧⌘D`: Run and Debug
- `⇧⌘X`: Extensions
- `⌃backtick`: Focus terminal

#### Explorer

These only works in Explorer.

- `⌘K E`: Focus open editors
- `⌘K ⌘0`: Collapse folders in sidebar (note that this will not collapse search results unfortunately)
- `⌘-click`: Select a file without opening it, or select a directory without expanding it

## Workspace

- `⌘K F` (`File > Close Folder`): Close folder in workspace (e.g., if there's only one open folder this will result in an empty document)

## Tabs

- `⌥⌘T`: Close all tabs except this one
- `⌃⇥`/ `⇧⌃⇥`: Cycle forward / backward through open tabs
- `⇧⌘T`: Re-open last closed tab
- `⌃⌘↑` / `⌃⌘↓`: Switch between header and source files

## Bottom Panel

- `⌘J`: Toggle bottom panel
- `⌃backtick`: Toggle Terminal
- `⇧⌘M`: Show Problems (issues)
- `View: Toggle Maximized Panel`: Maximize the panel

### Splits

- `View: Maximize Editor Group`: Zoom into a single split
- `View: Close Editors in Other Groups`: Close all other splits

#### Opening & Closing

- `⌘\`: Split the editor vertically
- `⌘K ⌘\`: Split editor horizontally
- `⌘W`: Close current split

#### Moving

- `⌘⌥0`: Toggle layout between horizontal and vertical splits
- `⌘K ←` / `⌘K ↑` / `⌘K →` / `⌘K ↓`: Move split left / up / down / right

#### Navigating

- `⌘K ⌘←` / `⌘K ⌘↑` / `⌘K ⌘→` / `⌘K ⌘↓`: Focus left / top / bottom / right editor
- `^⌘←` / `^⌘→`: Move a split left / right
- `⇧⌘[` / `⇧⌘]`: Switch tabs and splits

## Explorer

- `⌃↩`: Open file in a split
- `␣`: Open file

## Terminals

- `⇧^backtick`: Make new Terminal
- `⇧⌘[` / `⇧⌘]`: Switch terminals

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
