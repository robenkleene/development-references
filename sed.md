# `sed`

- `-i`: Replace in files, note that for macOS this needs to be `-i ''`

## Remove Spaces

	sed 's/ //g'

## Replace Multiple Spaces With One Space

	sed "s/  */ /g"

## Capture Groups

	sed 's/.*:\(.*\):.*/\1/p'`

Another example:

    sed -E 's/^( *-) */\1 /g'

Note that the `-E` flag inverts whether the parentheses need to be escaped.

## Files

### With `rg`

    rg Raster -l -0 | xargs -0 sed -n 's/Raster/Cyclist/gp'

### Recursive

    sed -n 's/Raster/Cyclist/gp' **

- `-n` / `--quiet` / `--silent`: Don't print every matching line
- `/p`: Output each matching line
- Don't run it like this (without removing the `p`), because it will double each replaced line
