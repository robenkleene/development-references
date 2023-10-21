# Visual Studio Code Ruby

## Debugging

1. Click the debug tab in VSCode
2. Click the gear icon and select "Listen for rdebug-ide"
3. Start your command to debug in the terminal, prefixed with `rdebug-ide`, e.g.:

        JEKYLL_NO_BUNDLER_REQUIRE=true rdebug-ide /Users/robenkleene/Development/Projects/Cocoa/Repla/Packages/Jekyll.replaplugin/Contents/Resources/bin/jekyll serve

4. Hit the play button in VSCode, the script will stop on the first breakpoint

(It's nice to use VS Code's built-in terminal when debugging Ruby.)