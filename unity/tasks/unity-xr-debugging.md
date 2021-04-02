# Unity XR Debugging

To view a log when wearing the device.

Use `adb`:

    adb logcat -s Unity

There's also a `CanvasWithDebug` package that comes with the Oculus package.

There's also the `Android logcat` package that provides easy log window integration within Unity (this merges all Unity platform output, but allows filtering).

## `adb` Path

To get the path to `adb` go to `Preferences... > External Tools` and get the path for `Android SDK Tools Installed with Unity`, `adb` is in the `platform-tools` directory.
