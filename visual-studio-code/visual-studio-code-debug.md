# Visual Studio Code Debug

- `F9`: Toggle breakpoint
- `⇧F9`: Insert inline breakpoint

## Tips

- If you have a valid `launch.json` setup, just go to the debug tab `⇧⌘D` and click `Debug`. Breakpoints should just work.

## Languages

### C

Working configuration for C, which is just the default auto-generated configuration with `a.out` added.

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