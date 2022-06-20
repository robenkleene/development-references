# iTerm

## Settings

- Turn on `Edit > Selection Respects Soft Boundaries` this is necessary to get iTerm to work well with tmux panes
    - The setting to open a new window if none are open is under `Preferences > Advanced` and is called `Open a new window when you click the dock icon and now windows are already open, and also on app launch when no other windows are open?`

## Sync

- iTerm supports storing settings in a synced folder (e.g., Dropbox), but it doesn't actually support syncing. The only solution is to quit iTerm, then overwrite the settings file with the correct settings, then re-open iTerm.
- Setting an arbitrary location makes iTerm store preferences as plain text, otherwise they're stored as a binary `plist`.

## Minimal Menu Bar

- Set `Preferences > Appearance > General > Theme > Minimal`
- The title can be hidden by toggling on `Profiles > Window > Custom window title` and setting it to empty, but it's useful to show to tell when an SSH session is active.
