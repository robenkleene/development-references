# `emacs` Debugging

Enabled debugger:

	(setq debug-on-error t)

On startup:

	emacs --debug-init

Debug a function:

	M-x debug-on-entry <function-name>

Debugger:

- `d`: Step forward
- `c`: Continue

Debugging Desktop Restore

If there are problems restoring windows on startup (with the `(desktop-save-mode 1)` option on), then turn on debugging with `(setq debug-on-error t)`, then run `desktop-revert`, this should catch the error in the debugger.
