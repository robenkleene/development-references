# `tmux` Window Management

## Resizing

These can be repeated without doing the leader key (i.e., they're assigned with the `bind-key` `-r` flag).

- `<prefix>⌥←` / `<prefix>⌥↑` / `<prefix>⌥←` / `<prefix>⌥↓`: Resize window by `5` in direction
- `<prefix>^←` / `<prefix>^↑` / `<prefix>^←` / `<prefix>^↓`: Resize window by `1` in direction

## Layouts

- `<prefix>C-o` / `rotate-window`: Rotate windows
- `<prefix>␣` / `next-layout`: Rotate between layouts

## Special

- `<prefix>z` / `resize-pane -Z`: Make pane full screen
- `<prefix>L`: Go to last session
