# Xcode Caches

## iOS DeviceSupport

This is just used to symbolicate logs, it can be deleted and there's no official way to delete it in the UI, so just delete the folders for all the OS versions that are no longer needed.

    ~/Library/Developer/Xcode/iOS DeviceSupport/

## Simulators

Command to delete old simulators:

    xcrun simctl delete unavailable
