# Unreal Engine Oculus

## Launching

You can launch directly to device, even if it's not listed in `LaunchOptions`, by going to `LaunchOptions > ProjectLauncer...` and clicking `Launch`.

(Try this if the Oculus Quest isn't showing up in the `LaunchOptions`.

## Project Settings

First choose `Virtual Reality` game.

- `Blueprint`
- `Scalable 3D or 2D`
- `Mobile / Tablet`

### Configuration

Use the default configuration except set these paths in `Edit > Project Settings` (note that these can just use the defaults if using a default install of Android Studio).

You'll need to restart your project after making these changes.

#### Under `Plattforms > Android SDK`

- `Location of Android SDK`: `/Volumes/Excalibur/Library/Android/sdk`
- `Location of Android NDK`: `/Volumes/Excalibur/Library/Android/sdk/ndk/22.1.7171670`

##### Java Locations

- `Location of Java`: `/Volumes/Excalibur/Applications/Android Studio.app/Contents/jre/jdk/Contents/Home/`
- `Location of Java`: `/Applications/Unity/Hub/Editor/2020.2.7f1/PlaybackEngines/AndroidPlayer/OpenJDK`

#### Under `Engine > Rendering`

- `Mobile MSAA`: `4x MSAA`
- `Mobile HDR`: Toggle off
