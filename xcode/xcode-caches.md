# Xcode Caches

## iOS DeviceSupport

This is just used to symbolicate logs, it can be deleted and there's no official way to delete it in the UI, so just delete the folders for all the OS versions that are no longer needed.

    ~/Library/Developer/Xcode/iOS DeviceSupport/

## Simulators

Command to delete unavailable simulators:

    xcrun simctl delete unavailable

To delete simulators data from `~/Library/Developer/CoreSimulator/Devices/`:

    xcrun simctl delete <uuid>

## System Information

`About this Mac > Storage > Manage`, `Developer` has an option to select and delete "Xcode Caches".
