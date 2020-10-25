# Vim Troubleshooting

If a binding with modifiers doesn't work, try entering it using `^v` followed by the bind combination. For example:

    nnoremap <M-O> :QuickFiles<CR>
    " For some reason the above binding doesn't work, but the below one does
    nnoremap O :QuickFiles<CR>
