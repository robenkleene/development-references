# 2022 Unity VR Game

1. Create a new 3D project
2. Add the following packages in the `Package Manager`:
    - `XR Interaction Toolkit` (use `Add package by name...` `com.unity.xr.interaction.toolkit`)
    - `OpenXR Plugin`
    - `Oculus XR Plugin`
3. Under `Project Settings... > XR Plug-in Management`, for `Android`, make sure `OpenXR` is checked

## Tracking Head Movement

1. In the Scene hierarchy, right-click and choose `Create Empty`, name it `VR Rig`
2. Select `VR Rig` and click `Add Component` and add an `XR Origin`
3. Right-click `VR Rig` and choose `Create Empty`, name it `Camera Offset`
4. Right-click `Camera Offset` and choose `Camera`, name it `VR Camera`
5. Select `VR Camera` and click `Add Component` and add a `Tracked Pose Driver`
6. Select `VR Rig` and drag `Camera Offset` to `Camera Floor Offset`, and drag `VR Camera` to `Camera GameObject`

# New Simpler Setup

1. Just add the Oculus Integration SDK
2. Drag the `OVRCameraRig` from `Assets > Oculus > VR > Prefabs` into the Hierarchy
