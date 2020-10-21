# Visual Studio Code Remote

## Shell

- `Preferences: Open Remote Settings (SSH: <hostname>)`, add the line:

        "terminal.integrated.shell.linux": "/home/linuxbrew/.linuxbrew/bin/fish"

## Extensions

- There's a command `Remote: Install Local Extensions in <host>...`
- To update an extension in development, connect to the remote machine then use `Extensions: Install from VSIX...`.
