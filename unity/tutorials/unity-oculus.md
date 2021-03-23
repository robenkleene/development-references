# Unity Oculus

## Setup

1. Oculus support in Unity requires the following modules with the Unity installation:
    - `Android Build Support`
        - `Android SDK & NDK Tools`: (C & C++ Support)
        - `OpenJDK`: Java Support
2. Oculus development requires the  `XR Plug-in Management` installed with the project (under `Edit > Project Settings...`), this installs the following packages:
    - `XR Legacy Input Helpers`
    - `XR Plugin Management`
    - `Subsystem Registration`

## Running on Device

### Developer Mode

Make sure developer mode is turned on on the device.

1. On the Oculus app on your phone, in settings toggle on `More Settings > Developer Mode`
2. When the device is plugged in, click `Confirm` for `Allow USB Debugging`

### Running

With the device plugged in, and turned on and after confirming `Allow USB Debugging`:

1. Go to `File > Build Settings...` and set `Android > Run Device > Oculus Quest`
