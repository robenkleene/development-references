# Unity VR Game

## Part 1: Head & Hand Tracking

After setting up a Unity project for VR (e.g., installing `XR Plugin Management`).

### Packages

1. This tutorial uses the `XR Rig` which is part of the `XR Interaction Toolkit`. This is a preview package, so before it will show up in the `Window > Package Manager`, you need to choose `Package Manager > Advanced Project Settings` (this is under the gear icon), then in the new window that opens, toggle on `Package Manager > Advanced Settings > Enable Preview Packages`. After performing these steps, install `XR Interaction Toolkit` from `Window > Package Manager`.

### Head Tracking

1. Right-click in the Hierarchy and choose `3D Object > Plane`. Scale the plane up to around `4.5` by clicking and dragging the inner cube
2. Create a material by right-clicking `Assets` and choosing `Create > Material`. Rename the material to `Black`, and set `Albedo: Black`.
3. Delete the `Main Camera`.
4. Right-click and choose `Create Empty`, and rename it to `VR Rig`, click `Add Component` and add a `XR Rig`.
5. Right-click `XR Rig` and choose `Create Empty`, rename it to `Camera Offset`.
6. Right-click `Camera Offset` and choose `Camera`, rename it to `VR Camera`. Click `Add Component` and add a `Tracked Pose Driver`.
7. Select `VR Rig` and drag `Camera Offset` to the `VR Floor Camera Field` and `VR Camera` to the `Camera Game Object`. Set `Tracking Origin Mode: Floor`.

At this point `Build and Run` to test on device will work.

### Hand Tracking

1. Create two empties under `SampleScene > VR Rig > Camera Offset` called `Left Hand` and `Right Hand`
2. Select both hands and click `Add Component`, add a `XR Controller (Device-Based)` *`XR Controller (Device-Based)` is being phased out in favor of `XR Controller (Action-Based)`, so that should probably be used for future projects*
3. Set `Right Hand` `Controller Node: Right Hand`, and the same for the left.

#### Hand Models

1. Create an empty under `SampleScene` and name it `Controller`.
2. Create a cube as a child of the `Controller` (right-click and choose `3D Object > Cube`). Use the scale tool (`R`) to scale it down to about `0.06`. Set `Z: 0.116`.
3. Create a material, and make sure it's color is white (it should be by default), drag this material onto the cube.
4. To make the `Controller` into a prefab, drag it into the `Assets` panel. After doing so, right-click and delete `Controller` from under `SampleScene`.
5. Drag the `Controller` prefab to `Left Controller > Inspector > Model Prefab`, and the same for the right controller.

At this point you should be able to run and see blocks for hands in VR.

### Ball & Table

1. Create a `Cube` and make a table from it
2. Create a `Sphere` and put it above, put not on, the table
3. Make a new material called `Red` to make the `Sphere` red
4. Add a `RigidBody` component to the sphere

At this point you should be able to run and touch the sphere with your block hands in VR.

### Grab Sphere

1. Add an `XR Grab Interactable` component to the sphere
2. Select both `Left Hand` and `Right Hand` and add an `XR Direct Interactor` component to them
3. Also add a `Sphere Collider` component to both hands and set its `Radius: 0.2` and toggle on `Is Trigger`.

At this point you should be able to build and run to grab the ball *I wasn't able to get this to work*

### Fixing Clipping

Fix the camera clipping objects when they get to close.

1. Set `VR Camera > Inspector > Camera > Near: 0.1`

The rest of this tutorial creates a bowling alley, which we're skipping.

## Controller Script

1. Create a new empty called `Hand Presence`, set its position to `0 0 0`
2. Add component to `Hand Presence`, search for `HandPresence` and click `New Script`, then `Create and Add`
3. Double-click the `HandPresence` script to edit it in a text editor

### `HandPresence.cs`

#### 1

Add to imports at the top:

    using UnityEngine.XR;

Replace `Start()` method:

    void Start()
    {
        List<InputDevice> devices = new List<InputDevice>();
        InputDevices.GetDevices(devices);

        foreach (var item in devices)
        {
            Debug.Log(item.name + item.characteristics);
        }
    }

At this point, you can run on the device and it will print out controller information to the console (use `adb -d logcat -s Unity` to log the console to standard out).

#### 2

Replace start:

    void Start()
    {
        List<InputDevice> devices = new List<InputDevice>();
        InputDeviceCharacteristics rightControllerCharacteristics = InputDeviceCharacteristics.Right | InputDeviceCharacteristics.Controller;
        InputDevices.GetDevicesWithCharacteristics(rightControllerCharacteristics, devices);

        foreach (var item in devices)
        {
            Debug.Log(item.name + item.characteristics);
        }

        if (devices.Count > 0) {
            targetDevice = devices[0];
        }
    }

And update:

    void Update()
    {
        targetDevice.TryGetFeatureValue(CommonUsages.primaryButton, out bool primaryButtonValue);
        if (primaryButtonValue) {
            Debug.Log("Pressing primary button");
        }
        targetDevice.TryGetFeatureValue(CommonUsages.trigger, out float triggerValue);
        if (triggerValue > 0.1f) {
            Debug.Log("Trigger pressed " + triggerValue);
        }

        targetDevice.TryGetFeatureValue(CommonUsages.primary2DAxis, out Vector2 primary2DAxisValue);
        if (primary2DAxisValue != Vector2.zero) {
            Debug.Log("Primary Touchpad " + primary2DAxisValue);
        }
    }

This prints values based when the primary button, mini joystick, or trigger are used.

### Skipped

There was a section here with adding support for a bunch of different types of controllers.

### Adding Hands

1. Drag the `Oculus Hands.unitypackage` package to `Assets`
2. Drag `SampleScene > Hand Presence` to `Assets` to create a prefab, then delete it from the `SampleScene`.
3. Duplicate the `Hand Presence` prefab
4. Add a public variable to `HandPresence.cs`:

        public class HandPresence : MonoBehaviour
        {
            public InputDeviceCharacteristics controllerCharacteristics;

    This will expose a variable to the prefab inspector where the characteristics can be configured.

3. Choose `Right Hand Presence` and set `Controller Characteristics`, toggling on `Right` and `Controller`, do the same for `Left Hand Presence`
4. Drag the `Right Hand Presence` prefab onto the `Right Hand`, and the same for the left hand.
5. For the left and right hand presence, click the target to the right of `Hand Model Prefab` and choose the appropriate model (e.g., `Right Hand Model`).

### Animating Hands

1. Create an `Animator Controller` under `Assets` (right-click `Create > Animator Controller`) and rename it to `Right Hand Animator`
2. Drag the `Right Hand Animator` as the `Controller` in the `Right Hand Model` inspector
3. With `Right Hand Animator` selected, open the `Animator` (`Window > Animation > Animator`). In the `Animator`, switch to the `Parameters` tab. Use the `+` button to two `float` and call them `Grip` and `Trigger`.
4. Create a `Blend Tree` node (right-click `Create State > From New Blend Tree`).
5. Double-click into the `Blend Tree` node and click the `Blend Tree` there, and in the inspector set `Blend Type: 2D Freeform Cartesian`, `Parameters: Grip Trigger`.
6. In the inspector, add four `Motion` fields (using the `+` button), set them to the following values, and drag the models matching the corresponding states:
    - `0 0`: Default
    - `0 1`: Pinch
    - `1 0`: Grip
    - `1 1`: Grip (Pinch & Grip Simultaneously)
7. To get the preview to work, show the inspector for the `Take 001` and drag the `Right Hand Model` prefab onto the preview area.
8. In `Assets`, duplicate `Right Hand Animator` and rename it to `Left Hand Animator`. Select the `Left Hand Model` prefab and in the inspector set `Animator > Controller: Left Hand Animator`.
9. Open the `Left Hand Animator` in the `Animator` and replace the models with the left hand versions.
10. Update the `HandPresence.cs` script, add a new function:

    Add a new variable:

        private Animator handAnimator;

    Instantiate the `handAnimator`:

        handAnimator = spawnedHandModel.GetComponent<Animator>();

    Add a new function:

        void UpdateHandAnimation()
        {
            if (targetDevice.TryGetFeatureValue(CommonUsages.trigger, out float triggerValue))
            {
                handAnimator.SetFloat("Trigger", triggerValue);
            }
            else
            {
                handAnimator.SetFloat("Trigger", 0);
            }

            if (targetDevice.TryGetFeatureValue(CommonUsages.grip, out float gripValue))
            {
                handAnimator.SetFloat("Grip", gripValue);
            }
            else
            {
                handAnimator.SetFloat("Grip", 0);
            }
        }

    Call it in the `Update()` function:

        UpdateHandAnimation();

### Activating Controllers

To fix the script so controllers become activated after launching.

Add a new function and move the contents of `Start()` into it:

    void TryInitialize()

Replace `start()` with:

    void Start()
    {
        TryInitialize();
    }

In `update()` add:

    if (!targetDevice.isValid)
    {
        TryInitialize();
    }
    else
    {
        // Put previous contents of `update()` here.
    }

## Teleportation

1. Select the `VR Rig` and add two components: `Locomotion System` and `Teleportation Provider`. (The `Locomotion System > XR Rig` and `Teleportation Provider > System` both automatically get set when running so do not have to set manually.)
2. Create a `XR > Device-based > Ray Interactor` (this tutorial uses the `Device-based` but the `Action-Based` is the preferred method) under `SampleScene > VR Rig > Camera Offset`, and rename it to `Right Teleport Ray`. Set `Position: 0 0 0`. In the inspector, make sure `XR Controller (Device-Based): Right Hand` is set.

At this point it should be able to build and run and see a red bar extending from the right hand.
