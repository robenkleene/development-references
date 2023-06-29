# Emacs Mark

## Movement

- `C-u C-SPC`: Pop buffer local mark (go to previous mark, repeatable)
- `C-x C-SPC`: Pop global mark
- `C-x C-x`: Swap the point and mark (e.g., to adjust the other side of a selection)
- `C-SPC C-SPC`: Push mark (set a mark with no region)
- `isearch` automatically sets a mark when entering a search result with `RET`

## Setting Mark

- `C-M-]`: Mark s-expression
- `C-x h`: Mark buffer
- `M-h`: Mark paragraph
- `C-M-h`: Mark `defun`
- `C-x C-p`: Mark page
