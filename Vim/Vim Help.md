# Vim Help

See `:help help-summary`.

## General

- `:h :command`: Used for `cmdline` commands (e.g., `:help :help`)
- `:h 'option'`: Options (e.g., `:help 'incsearch'`)
- `:h function()`: Functions (e.g., `bufnr()`)

### Prefixes

- `c_`: prefix for command line (e.g., `:help c_%`)
- `i_`: prefix for insert mode (e.g., `:help i_CTRL-[`)
- `v_`: prefix for visual mode (e.g., `:help v_CTRL-]`)
- No prefix for normal mode commands (e.g., `:help CTRL-]`).

### Less Used

- `>`: Prefix for commands for debugging (`:help >cont`)
- `/`: Prefix for regular expression items (`:help /\+`)
- `quote`: Prefix for registers (`:help quote:`)

## Tag Match List

After executing `help {subject}` command, the matches for the `{subject}` are stored on the `tag-matchlist`

* `:[ts]elect`: Show the matches in the `tag-matchlist`
* `:[tn]ext`: Jump to the next match
* `:[tp]revious`: Jump the previous match

## Tag Stack

Navigating to help tags adds those tags to the `tagstack`.

* `:tags`: Show the contents of the `tagstack`
* `g]`: Show a list for matches of the item under the cursor
* `<C-]>`: Jump to definition of the keyword under the cursor, this adds it to the `tagstack`
* `<C-t>`: Jump to the backwards in the `tagstack` (`<C-o>` can usually also be used instead, which uses the `jumplist`)
* `:[ta]g`: Jump to the next entry in the `tagstack`

## Tips

* `/|` or `f|`: Jump to the next tag in the document or line

## Help Example

			       *'ballooneval'* *'beval'* *'noballooneval'* *'nobeval'*
	'ballooneval' 'beval'	boolean	(default off)
				global
				{not in Vi}
				{only available when compiled with the |+balloon_eval|
				feature}
		Switch on the |balloon-eval| functionality.

- `*'ballooneval'*`: Tags for this help entry
- `'ballooneval' 'beval'`: Long and short form of the option name
- `{}`: Nothing special about these notes
- `|balloon-eval|`: Tags that you can jump to (with `<C-]>`)
