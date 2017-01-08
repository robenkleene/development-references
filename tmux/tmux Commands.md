# `tmux`

## Sessions

* `<prefix>s`: Choose session
* `tmux ls`: List sessions from terminal
* `tmux attach`: Attach if there is only one session
* `tmux attach -t [target session]`: Attach to a specific session
* `<prefix>$`: Rename session
* `<prefix>d`: Detach

## Panes

* `<prefix>%`: Vertical Split
* `<prefix>"`: Horizontal Split
* `<prefix>o`: Next pane
* `<prefix>;`: Previous pane
* `<prefix>x`: Kill pane
* `<prefix>}` / `<prefix>{`: Move pane
* `<prefix>M-Up` / `<prefix>M-Down` / `<prefix>M-Left` / `<prefix>M-Right`: Resize pane
* `<prefix>q`: Switch to numbered pane
* `<prefix>!`: Switch a pane to window
* `respawn-pane -k`: Restart current shell

### Move Panes

* `<prefix>{` / `<prefix>{`: Move panes

## Windows

* `<prefix>c`: New Window
* `<prefix>l`: Last Window
* `<prefix>n`: Next Window
* `<prefix>,`: Rename Window
* `<prefix>&`: Kill window
* `<prefix>0`, `<prefix>1`...: Switch to that window number
* `<prefix>.`: Move window (Prompt to enter window number)
* `<prefix>,`: Switch to window (Prompt to enter window number)	
* `:movew`: Move window to next unused window number
* `swap-window -s 3 -t 1`: Move window index 3 to index 1
* `swap-window -t 1`: Move current window to index 1

## Miscellaneous

* `tmux kill-server`: Kill everthing
* `:source-file ~/.tmux.conf`: Reload `tmux.conf`
* `tmux source-file ~/.tmux.conf`: Reload `tmux.conf`
* `tmux list-keys -t vi-edit`

## Scrolling

* `<prefix>[`: Enter scroll mode
* `q`: Quit scroll mode
* `<prefix>Page Up`: Enter copy mode and page up one screen
