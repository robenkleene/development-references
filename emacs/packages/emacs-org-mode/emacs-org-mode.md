# Org Mode

## Outline

### Editing

- `M-RET` / `C-RET`: New list item at current level before / after children
    - Hold `⇧` to make the new item a todo
    - The best way to add a child is to just hit tab after adding a new item at the same level
- `C-c C-x C-w` / `C-c C-x C-y`: Kill / paste subtree

### Moving

- `M-left` / `M-right`: Demote / promote item
- `M-up` / `M-down`: Move item up / down

## URL

- `C-c C-l`: Add URL (just `C-y` after to paste from clipboard)
- `C-c C-o`: Open URL

## Todo

- `M-S-<ret>` / `C-S-<ret>`: Add todo at current level before / after children
- `S-<left>` / `S-<right>`: Cycle todo states (`DONE` / `TODO`)
- `C-c C-t`: Cycle todo state
- `C-c C-d` / `C-u C-c C-d`: Insert / remove deadline
- `C-c C-s` / `C-u C-c C-s`: Insert / remove schedule
- `C-c .`: Change date
- `S-<left>` / `S-<right>` on a date changes the date by one day

### Date Picker

- `S-<left>` / `S-<right>`: Move day left / right
- `S-<up>` / `S-<down>`: Move week backward / forward
- `+1` / `+1d`: Schedule date to tomorrow
- `.`: Go to today

## Misc

- `C-c C-x C-s`: Archive item
- `C-c ^` / `org-sort`: Sort (then `d` to sort by deadline)

## Column View

- `C-c C-x C-c` / `C-c C-c`: Turn on / off column view for the current subtree
