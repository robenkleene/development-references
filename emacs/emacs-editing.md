# `emacs` Editing

* `M-;`: Comment or uncomment selected region
* `C-x C-;`: Comment or uncomment line
- `C-o`: Open empty line
- `C-x C-o`: Delete empty blank lines

## Undo & Redo

- `C-x u` or `C-/` or `C-_`: Undo
  - `C-g`: Followed by an undo binding to redo, to do this repeatedly, then use `C-x z` to repeat, followed by tapping `z` over and over again to keep repeating.

### Selection

- `C-SPC`: Select
- `M-w`: Copy
- `C-w`: Cut
- `C-y`: Paste
- `M-y`: Cycle through matches (after a `C-y`)
- `C-x C-x`: Restore previous region

## Movement

- `M-m`: Move to first character on line (skip white space)
- `M-m`: Cycle between top, center and bottom of window
- `M-{`: Backward by paragraph
- `M-}`: Forward by paragraph

## Macros

- `C-x (`: Start recording a macro
- `C-x )`: Finish recording a macro
- `C-x e`: Replay macro

## Special

- `M-q`: Wrap comment

## Spelling

- `M-S-$`: Correct misspelled word
