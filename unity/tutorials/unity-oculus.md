# Unity Oculus

## Setup

### Unity

- Oculus support in Unity requires the following modules with the Unity installation:
    - `Android Build Support`
        - `Android SDK & NDK Tools`: (C & C++ Support)
        - `OpenJDK`: Java Support

### Project

- Oculus development requires the `XR Plugin Management` package be installed with the project. Go to `Window > Package Manager`, choose `Packages: Unity Registry`, then search for "XR", and install `XR Plugin Management`. This installs the following packages:
    - `XR Legacy Input Helpers`
    - `XR Plugin Management`
    - `Subsystem Registration`
- Toggle on `Edit > Project Settings... > XR Plug-in Management > Android > Oculus`

## Running on Device

### Developer Mode

Make sure developer mode is turned on on the device.

1. On the Oculus app on your phone, in settings toggle on `More Settings > Developer Mode`
2. When the device is plugged in, click `Confirm` for `Allow USB Debugging`

### Running

With the device plugged in, and turned on and after confirming `Allow USB Debugging`:

1. Go to `File > Build Settings...` and set `Android > Run Device > Oculus Quest 2`
2. Click `Refresh` (note that devices aren't added live to this list, even after closing and re-opening the panel, so always click `Refresh`)
3. The app will run on the platform with the Unity icon next to it, so if `Android` doesn't have the unity icon next to it then select `Android` and click `Switch Platform`.
4. Click `Build And Run`
