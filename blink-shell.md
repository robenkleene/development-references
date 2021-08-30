# Blink Shell

## Bindings

- To make `⌃␣` work, e.g., as for `set-mark-command` in Emacs, add it as `Preference > Keyboard > Custom Presses`, `⌃␣` to `⌃␣`
    - For this to work you also have to disable the iOS Emoji keyboard `Settings > General > Keyboard > Keyboards`

## Theme

Use the theme `Blazer` from the gallery.

## Resizing

When a keyboard toolbar appears, Blink resizes the terminal, for example, when using an app with a keyboard toolbar in slide over. You can stop Blink from resizing when this toolbar appears by three-finger tapping and toggling on "Lock".

## Keys

Key-based authentication occasionally randomly stops working, the solution is to delete and re-add the key.

You can get more information by running `ssh -vv <host>` in Blink Shell. The error where you have to re-generate the key is "could not find public key files".

Potential solution to the above key issue: It seems like there's a conflict between iCloud Sync and private keys. The host information is synced but the keys aren't, so the solution seems to be to name the two keys the same on the two different devices, so the synced host information will still point to valid key.

## New Device

If a device is failing with a confusing error, like SSH failing silently, that’s probably because a new device is missing the private key. The solution is to copy the private key from a working device and import it as a new key on the other device.
