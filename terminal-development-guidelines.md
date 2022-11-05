# Terminal Development Guidelines

- **The shell is omnipresent:** Prefer shell customization to editor customization, e.g., in Vim use `!<command>` rather than defining a new command. Shell commands are automatically available in every TUI editor (since every TUI editor can spawn a shell).
- **Make themes for 8-bit color, use themes for 24-bit color:** 8-bit's 256 is small enough that it's better to make your own theme, but with 24-bit color, just use an off-the-shelf theme.

