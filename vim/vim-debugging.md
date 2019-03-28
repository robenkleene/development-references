# `vim` Debugging

## Test a Key Code

	:<C-V><enter>

After doing above you'll see what appears for `<enter>`.

## Debugging Bindings

List any manually set bindings:

	verbose map <leader>c

You might need to specify `nmap`, etc...

## Debugging Commands

	verbose command Ag

## Show all loaded `vim` Scripts

	:scriptnames

## Profiling

	:profile start ~/Downloads/profile.log
	:profile func *
	:profile file *
	" Do something
	:profile pause
	:noautocmd qall!
