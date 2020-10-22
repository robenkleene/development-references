# Visual Studio Code Remote

## Shell

- `Preferences: Open Remote Settings (SSH: <hostname>)`, add the line:

        "terminal.integrated.shell.linux": "/home/linuxbrew/.linuxbrew/bin/fish"

## Extensions

- There's a command `Remote: Install Local Extensions in <host>...`
- To update an extension in development, connect to the remote machine then use `Extensions: Install from VSIX...`.

### Specific

The C/C++ for Visual Studio Code extension (`vscode-cpptools`) requires a different installer for remote, otherwise an error will pop-up that says:

> This MacOS version of the extension is incompatible with your OS. Please download and install the "cpptools-linux.vsix" version of the extension.

The `cpptools-linux.vsix` file can be downloaded from `Releases` at the GitHub page, and then installed on the server by connecting to the sever and selecting `Extensions: Install from VSIX...`.
