# Visual Studio Code Debug

- `F5`: Continue or start debugging (attach)
- `⇧F5`: Stop debugging (detach)
- `F9`: Toggle breakpoint
- `⇧F9`: Insert inline breakpoint
- `Toggle Activate Breakpoints` (two circles icon in the `Breakpoints` panel): Toggle breakpoints

## Debugger

- `F5`: Continue
- `F10`: Step over
- `F11`: Step in
- `⇧F12`: Step out

## Tips

- If you have a valid `launch.json` setup, just go to the debug tab `⇧⌘D` and click `Debug`. Breakpoints should just work.

## Languages

Generally, you can configure debugging by clicking `create a launch.json file` from the `Run` panel

### Live Server

Just a basic configuration to load HTML.

``` json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Live Server",
      "type": "node",
      "request": "launch",
      "runtimeExecutable": "live-server",
      "args": [ "--no-browser"],
      "serverReadyAction": {
        "pattern": "https?://127.0.0.1:([0-9]+)",
        "uriFormat": "http://localhost:%s"
      }
    },
    {
      "name": "Debug With Chrome",
      "type": "node",
      "request": "launch",
      "runtimeExecutable": "live-server",
      "args": [ "--no-browser"],
      "serverReadyAction": {
        "pattern": "https?://127.0.0.1:([0-9]+)",
        "action": "debugWithChrome",
        "uriFormat": "http://localhost:%s"
      }
    }
  ]
}
```
### C & Swift

Working configuration for C, which is just the default auto-generated configuration with `a.out` added.

The binary must be compiled with `cc -g <source file>` for C and Swift with `swiftc -o a.out -g <source file>`.

``` json
{
    "version": "0.2.0",
    "configurations": [
        {
            "type": "lldb",
            "request": "launch",
            "name": "Debug",
            "program": "${workspaceFolder}/a.out",
            "args": [],
            "cwd": "${workspaceFolder}"
        }
    ]
}
```

### Node

A working configuration for Node:

``` json
{
  // Use IntelliSense to learn about possible attributes.
  // Hover to view descriptions of existing attributes.
  // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Launch via npm",
      "type": "node",
      "request": "launch",
      "cwd": "${workspaceFolder}",
      "runtimeExecutable": "npm",
      "runtimeArgs": ["run-script", "start"]
    }
  ]
}
```

It's unclear why this is hard-coded to open Chrome rather than the system default browser.

If you close the browser window, you can usually open it again by checking the debug console for a URL (`⇧⌘Y`).

To disable opening a browser automatically with `npm start`, add:

    "env": {"BROWSER": "none"},

### Opening Browser Windows

The following will open your default browser when the matched string is output.

``` json
      "serverReadyAction": {
        "pattern": "https?://localhost:([0-9]+)",
        "uriFormat": "http://localhost:%s",
        "action": "openExternally"
      }
```

Use `"action": "debugWithChrome"` to use Chrome with the debugger attached.

This is the only way to make breakpoints work in VS Code while running in a browser. E.g., there's no way to use VS Code breakpoints with Safari.

### Troubleshooting

If a command is having trouble running in the Debug Console, e.g., if the full output isn't showing up, then running it in the integrated terminal instead can be helpful:

    "console": "integratedTerminal",
