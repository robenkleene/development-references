# Unity VR Game

After setting up a Unity project for VR (e.g., installing `XR Plugin Management`).

## Packages

1. This tutorial uses the `XR Rig` which is part of the `XR Interaction Toolkit`. This is a preview package, so before it will show up in the `Window > Package Manager`, you need to choose `Package Manager > Advanced Project Settings` (this is under the gear icon), then in the new window that opens, toggle on `Package Manager > Advanced Settings > Enable Preview Packages`. After performing these steps, install `XR Interaction Toolkit` from `Window > Package Manager`.

## Head Tracking

1. Right-click in the Hierarchy and choose `3D Object > Plane`. Scale the plane up to around `4.5` by clicking and dragging the inner cube
2. Create a material by right-clicking `Assets` and choosing `Create > Material`. Rename the material to `Black`, and set `Albedo: Black`.
3. Delete the `Main Camera`.
4. Right-click and choose `Create Empty`, and rename it to `VR Rig`, click `Add Component` and add a `XR Rig`.
5. Right-click `XR Rig` and choose `Create Empty`, rename it to `Camera Offset`.
6. Right-click `Camera Offset` and choose `Camera`, rename it to `VR Camera`. Click `Add Component` and add a `Tracked Pose Driver`.
7. Select `VR Rig` and drag `Camera Offset` to the `VR Floor Camera Field` and `VR Camera` to the `Camera Game Object`. Set `Tracking Origin Mode: Floor`.

At this point `Build and Run` to test on device will work.

## Hand Tracking

1. Create two empties under `SampleScene > VR Rig > Camera Offset` called `Left Hand` and `Right Hand`
2. Select both hands and click `Add Component`, add a `XR Controller (Device-Based)` *`XR Controller (Device-Based)` is being phased out in favor of `XR Controller (Action-Based)`, so that should probably be used for future projects*
3. Set `Right Hand` `Controller Node: Right Hand`, and the same for the left.

### Hand Models

1. Create an empty under `SampleScene` and name it `Controller`.
2. Create a cube as a child of the `Controller` (right-click and choose `3D Object > Cube`). Use the scale tool (`R`) to scale it down to about `0.06`. Set `Z: 0.116`.
3. Create a material, and make sure it's color is white (it should be by default), drag this material onto the cube.
4. To make the `Controller` into a prefab, drag it into the `Assets` panel. After doing so, right-click and delete `Controller` from under `SampleScene`.
5. Drag the `Controller` prefab to `Left Controller > Inspector > Model Prefab`, and the same for the right controller.

At this point you should be able to run and see blocks for hands in VR.

## Ball & Table

1. Create a `Cube` and make a table from it
2. Create a `Sphere` and put it above, put not on, the table
3. Make a new material called `Red` to make the `Sphere` red
4. Add a `RigidBody` component to the sphere

At this point you should be able to run and touch the sphere with your block hands in VR.

## Grab Sphere

1. Add an `XR Grab Interactable` component to the sphere
2. Select both `Left Hand` and `Right Hand` and add an `XR Direct Interactor` component to them
