# Terminal Emulator Comparison

## Terminal

- Mouse reporting is more accurate
- Only 256 colors
- Clicking the window once focuses, second registers mouse input
- Doesn't support URLs

## iTerm

- `⌥`-click to disable mouse reporting while selecting text is more compatible with third-party keyboards than Terminal app which uses `fn` key
- iTerm can be configured to not open a new terminal window when it activates
- Includes a hot key window
- iTerm selection interferes with built-in selection in Vim, Emacs, and tmux
- Can be customized to have a minimal title bar
- Clicking the window once focuses, second registers mouse input
- Supports URLs
- Has custom file-system support, e.g., `ls` results can be opened in Finder and `make`-style build errors can be opened in Visual Studio Code automatically

## kitty

- kitty has a problem if Emacs is in a `tmux` pane and clicking between it and another pane triggers mouse selection.

## Alacritty

- Alacritty has no option to disable passing through the first mouse click (so clicking a window focuses it and sends the click event to the terminal). There are two key consequences of this: 1. We're always fixing the cursor position after clicking in the window to focus it, 2. It works differently than Emacs, which only focuses on first click, resulting in conflicting muscle memory between Emacs and the shell.
- Dotfiles config sync
- Alacritty does not support the default Emoji picker (with `⌃⌘␣`)

## Ghostty

- Least customization reguired
- Dotfiles config sync
- Supports URLs

## Scrolling

- Of Ghostty, Alacritty, and iTerm2, iTerm2 is the only terminal where mouse wheel scrolling works properly in `tmux` (a single mouse wheel click starts copy mode or moves by `5` lines if already in copy mode)
