# Visual Studio Code Settings

## Bindings

Bindings can be added to the `Code/User/keybindings.json` by selecting `Code > Preferences > Keyboard Shortcuts` (`⌘K ⌘S`), and clicking the exiting short to add a new one. This works for either changing an existing shortcut, or adding a shortcut to a command that already has one.

### Removing Bindings

- `⌘K ⌘⌫`: Remove binding

## Contextual Menus

It appears that contextual menus options for existing commands can only be added by editing an extension's `package.json`.

## Extensions

- `Extensions: Show Installed Extensions`

## Formatter

To choose a formatter, use "Format Document With..." this appears to only be available if there are multiple formatters to choose from?

## Colors

To see the scope at the cursor, select "Developer: Inspect Editor Tokens and Scopes".

## Language Specific Settings

- `Preferences: Configure Language Specific Settings...`

### Example

Toggle on word wrap only for Markdown files:

``` json
    "[markdown]": {
        "editor.wordWrap": "on"
    }
```
