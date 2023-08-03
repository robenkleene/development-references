# `tmux` Window Management

## Splits

- `<prefix>"`: Split window horizontally
- `<prefix>%`: Split window vertically

## Navigation

## Sessions

- `<prefix>L`: Last session
- `<prefix>s`: Session picker

## Window

- `<prefix>w`: Window picker
- `<prefix>&`: Kill window
- `<prefix>l`: Last window
- `<prefix>c`: Create window
- `<prefix>p`: Previous window
- `<prefix>n`: Next window

## Panes

- `<prefix>x`: Kill pane
- `<prefix>!`: Move current pane to new window
- `<prefix>;`: Last pane
- `<prefix>M-o`: Swap panes

## Resizing

These can be repeated without doing the leader key (i.e., they're assigned with the `bind-key` `-r` flag).

- `<prefix>⌥←` / `<prefix>⌥↑` / `<prefix>⌥←` / `<prefix>⌥↓`: Resize window by `5` in direction
- `<prefix>^←` / `<prefix>^↑` / `<prefix>^←` / `<prefix>^↓`: Resize window by `1` in direction

## Layouts

- `<prefix>C-o` / `rotate-window`: Rotate windows
- `<prefix>␣` / `next-layout`: Rotate between layouts

## Special

- `<prefix>z` / `resize-pane -Z`: Make pane full screen

