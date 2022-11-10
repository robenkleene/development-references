# Helix Runtime

Package managers make a wrapper script that sets the Helix runtime path:

```
cat (which hx)  Dotfiles (master=)
#!/bin/bash
HELIX_RUNTIME="/home/linuxbrew/.linuxbrew/Cellar/helix/22.08.1/libexec/runtime" exec "/home/linuxbrew/.linuxbrew/Cellar/helix/22.08.1/libexec/bin/hx"  "$@"
```