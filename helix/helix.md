# Helix

## Movement

- `<number>G`: Go to line number
- `gg`: Start of file
- `ge`: End of file
- `gl`: End of line
- `gs`: Start of line

### Pairs

- `[p` / `]p`: Previous / next paragraph
- `[f` / `]f`: Previous / next file
- `[c` / `]c`: Previous / next class
- `[a` / `]a`: Previous / next function argument

## Deletion

- `d`: Delete current character

## Selection

- `;`: Deselect
- `w`: Select to the beginning of the next current word
- `e`: Select to the end of the current word
- `x`: Select current line (hit `x` againt to select the next line)
- `ma"`: Select around delimiter
- `mi"`: Select in delimiter
- `f` / `F`: Select to character
- `t` / `T`: Select up to character
- `A-.`: Extend last `f` or `t` command
- `R`: Replace selection with yanked text
- `%`: Select whole file

## Editing

- `>`: Indent
- `<`: Outdent
- `C-a` / `C-x`: Increment / decrement
- `u` / `U`: Undo / redo

## Multiple Cursors

- `A-s`: Split selection on new lines (e.g., make a cursor on each line)
- `,`: Remove multiple cursors
- `C`: Add cursor to "next suitable line"
- `s`: With an active selection, search for a phrase in the selection and select it, e.g., to change multiple occurrences
- `S`: With an active selection, make multiple cursors for each occurrence

### Select Mode

After using `s` to select a term.

- `(` / `)`: Jump between matches
- `A-,`: Remove a match

## Clipboard

- `<space>p`: Paste from system clipboard after
- `<space>P`: Paste from system clipboard before

## Search

- `*`: Copy the selection to the search register

### Search & Multiple Cursors

1. Select text to search for
2. Hit `*` to put it in the search register
3. Hit `v` to enter select mode
4. Hit `n` to select more instances
5. Hit `c` (or `r`) to replace all selected instances

Use `(` / `)` to jump between matches, and `A-,` to remove a match

## Tree Sitter

- `⌥↑` / `⌥↓`: Move up / down through syntax tree

## Fuzzy Find

- `␣f`: Fuzzy find file in project (by source control)
- `␣F`: Fuzzy find file from working directory
- `␣'`: Re-open last fuzzy finder

## Window Management

- `gn` / `gp`: Goto next / previos buffer
