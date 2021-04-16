# Unity VR Game

## Part 1: Head & Hand Tracking

After setting up a Unity project for VR (e.g., installing `XR Plugin Management`). Note that later parts of this process also require the Universal Render Pipeline, so the `Universal Render Pipeline` template should probably be used.

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
5. Rename it to `Bowling Ball`

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

There are two types of teleportation, teleport area, and teleport anchor.

### Teleport Area

The teleportation area allows teleporting to anywhere.

1. Create a `XR > Teleportation Area` under `SampleScene`, and offset it from the camera, and raise it up slightly so it isn't intersecting with the existing ground plane. The plane can be teleported to.
2. Add a cube to `SampleScene` and put it somewhere near the plane. Add a `Teleportation Area` component to the cube. This is to setup the cube as a teleportation destination as well, but it needs a collider to be set in order to work. By default it will just use the exiting `Box Collider` on the cube, so it does not need to be set now.

### Teleport Anchor

The teleportation anchor teleports exactly to the anchor.

1. Create a `XR > Teleportation Anchor` under `SampleScene`. Scale down the plane and place it next to the `Teleportation Area` plane.

At this point you should be able to run and teleport around the plane, or to the anchor.

## Tweaks

1. To have the teleport happen on trigger rather than grip, set `Right Teleport Ray > XR Controller (Device-based) > Select Usage: Trigger`. Also set `Axis To Press Threshold: 0.2`.
2. Use a cube to create a wall on the `Teleportation Area` to illustrate that the ray does not allow teleporting through walls.

### Bowling Ball

By default, the teleport also allows interacting with the `Bowling Ball` (the beam turns white why pointed at the ball, and pulling the trigger brings it to your hand). To prevent this, add a layer to the `Bowling Ball`.

1. Select the `Bowling Ball` and in the inspector, choose `Layer > Add Layer`. In the layer inspector that comes up, name `User Layer 8` to `Grab`. Select the `Bowling Ball` and set `Layer: Grab`.
2. Under `Right Teleport Ray > XR Ray Interactor > Raycast Mask`, toggle off the `Grab` layer.

### More

1. To make it so you can trigger in an invalid zone, then move to a valid zone and release, set `Right Teleport Ray > XR Ray Interactor > Selection Configuration: State Change` (the default is `State`)

## Updating the Teleport UI

1. Under `Right Teleport Ray > XR Ray Interactor`, set `Line Type: Projectile Curve`, `Velocity: 8`
2. To play a haptic when hovering a valid teleportation target, toggle on `XR Ray Interactor > Haptic Events > On Haptic Entered`, set `Haptic Intensity: 0.1` and `Duration: 0.1`.
3. To play a haptic when teleporting, toggle toggle on `XR Ray Interactor > Haptic Events > Play Haptic On Select Enter`, set `Haptic Select Enter Intensity: 0.3` and `Haptic Select Enter Duration: 0.1`.

### Reticle

To create a destination reticle.

1. Create a `Cylinder` under `SampleScene`, and rename it to `Teleport Reticle`. Remove the `Capsule Collider` component. Scale it down on all axes to `0.6`. Scale it down on the Y axis to `0.1`.
2. Create a new material and rename it to `Reticle Base`. Set `Shader > Universal Render Pipeline/Unlit`, set `Surface Type: Transparent`. Choose a blue for `Surface Inputs > Base Map`.
3. Drag the `Teleport Reticle` to the `Right Teleport Ray > XR Interactor Line Visual: Teleport Reticle`

Building and running now should show the reticle when hovering over a valid teleportation target

#### VFX Graph Reticle

1. Create a new cylinder as a child of the `Teleport Reticle`, Remove the `Capsule Collider` component, just like for the previous cylinder. Position the cylinder like a cup on top of a cup holder relative to the `Teleport Reticle` (so longer, and smaller radius).
2. Create a `Unlit Graph` shader and rename it to `Color Ramp`. With the `Color Ramp` selected click `Open Shader Editor`.

##### Shader Editor

1. In the `Graph Inspector`, set `Surface: Transparent`, and `Two Sided`.
2. Add two `Color` properties and rename them to `TopColor` and `BottomColor`.
3. Add a `Position` node, and set `Space: Object`.
4. Create a `Split` node and connect the `Position > Out` output to its `In` input. Drag out the `TopColor` and `BottomColor`. Create a `Lerp` node, and connect `BottomColor` to its `A` input, `TopColor` to its `B` input, and the `Split > G` output to its `T` input.
5. Drag the `Lerp > Out` output to the `Fragment > Base Color` input.

###### Material

1. Right-click the `Color Ramp` in the assets panel and choose `Create > Material`, this will create a new material called `Shader Graphs_Color Ramp`.
2. Drag `Shader Graphs_Color Ramp` to the `Teleport Reticle > Cylinder` in the scene view to apply the material to it..


###### Alpha

1. Edit the `Color Ramp` shader graph, add a `Split` node, connect the `Lerp > Out` output to the `Split > In` input. Connect the `Split > A` output to the `Fragment > Alpha` input.
2. Select `Shader Graphs_Color Ramp` and set `TopColor` to transparent black, and bottom color to a partially-transparent blue.

###### Particle Effect

1. In the Hierarchy, right-click `Teleport Reticle` and choose `Effects > Particle System`.
2. Resize the `Teleport Reticle > Particle System` so it fits within the beam, and rotate it so it points straight up. Set `Start Lifetime: 1` and `Start Speed: 2` in the inspector. Toggle on the `Color over Lifetime` and set the gradient to an opaque blue to a transparent white. Also set `Renderer > Material: Default-Particle`.
3. In the Hierarchy, drag the `Teleport Reticle` so it's a child of `SampleScene > VR Rig > Camera Offset > Right Teleport Ray`.
4. Select `Teleport Reticle` the Hierarchy and in the inspector set `Lighting > Casts Shadows: Off`.

At this point you should be able to build and run and see the reticle used for teleporting.

#### Fishing Pole

Customize the fishing pole line.

##### Photoshop

1. Make a texture PNG that's a white stripe with transparency on either side, and call it `White Trait.png`

##### Sprite

1. Drag `White Trait.png` to the `Assets` panel in Unity. In the inspector, set its `Texture Type: Sprite (2D and UI)` and `Wrap Mode: Repeat`.
2. Right-click in assets and choose `Create > Shader > Universal Render Pipeline > Sprite Unlit Shader Graph` *it appears this doesn't work using `Unlit` and `Lit` should be used instead*, and rename it to `Dotted Line`, and open the Shader Editor.

##### Shader Editor

1. Add two properties:
    - `Texture 2D` named `Texture`
    - `Vector 2` named `Speed`
2. Add a `Sample Texture 2D` node, drag in the `Texture` property and connect its output to  the `Simple Texture 2D > Texture` input. Connect the `Sample Texture 2D > RGBA` output to the `Fragment > Base Color` input.
3. Drag the `Time` property in, and create a `Time` node. Add a `Multiply` node, and connect the `Time > Time` output to its `A` input. Connect the `Speed` to its `B` input.
4. Add a `Tiling And Offset` node, and connect the `Multiply > Out` output to its `Offset` input. Connect its `Out` output to the `Sample Texture 2D > UV` input.
5. Add a `Split` and connect the `Simple Texture 2D > RGBA` to its `In` input. Connect its `A` output to the `Fragment > Alpha` input.

##### Material

1. Right-click the `Dotted Line` in the `Assets` folder and choose `Create > Material`, and drag the `White Trait` into its texture well.
2. In the Hierarchy, select `SampleScene > VR Rig > Camera Offset > Right Teleport Ray` and in the inspector, drag `Shader Graphs_Dotted Line` to `Line Renderer > Materials > Element 0`. In the inspector, under `Shader Graphs_Dotted Line`, set `Speed: -2 0 0 0` and set `Line Renderer > Texture Mode: Tile`.

##### Color

To improve the color of the dashed lines.

1. In the Hierarchy, select `SampleScene > VR Rig > Camera Offset > Right Teleport Ray`, and in the inspector, under `XR Interactor Line Visual` set `Valid Color Gradient` and `Invalid Color Gradient` to nice values. They look good with the farthest left value set to transparent, and the farthest right to opaque.

#### Both Hands

1. In the hierarchy, duplicate `SampleScene > VR Rig > Camera Offset > Right Teleport Ray` (`⌘D`) and rename it to `Left Teleport Ray`. In the inspector, under `XR Controller (Device-based)` set `Controller Node > Left Hand`.

#### Intermittent Teleport

1. Add a script to the `SampleScene > VR Rig` called `LocomotionController`.
2. Edit `LocomotionController.cs` and add the following:

        // Add this import
        using UnityEngine.XR.Interaction.Toolkit;

        // Replace the contents of `LocomotionController` with this
        public class LocomotionController : MonoBehaviour
        {
            public XRController leftTeleportRay;
            public XRController rightTeleportRay;
            public InputHelpers.Button teleportActivationButton;
            public float activationThreshold = 0.1f;

            // Update is called once per frame
            void Update()
            {
                if (leftTeleportRay)
                {
                    leftTeleportRay.gameObject.SetActive(CheckIfActivated(leftTeleportRay));
                }

                if (rightTeleportRay)
                {
                    rightTeleportRay.gameObject.SetActive(CheckIfActivated(rightTeleportRay));
                }
            }

            public bool CheckIfActivated(XRController controller)
            {
                InputHelpers.IsPressed(controller.inputDevice, teleportActivationButton, out bool isActivated, activationThreshold);
                return isActivated;
            }
        }

3. Select the `VR Rig` in the hierarchy, and under `Locomotion Controller (Script)`, drag `Left Teleport Ray` to the `Left Teleport Ray` variable field, and the same for the right. Set `Teleportation Activation Button: Trigger`.

At this point you should be able to build and run, the teleportation UI won't appear until holding the trigger, releasing the trigger will teleport.

## Continuous Movement

1. Add a script to the `VR Rig` called `ContinuousMovement`.
2. Add to the top of the `ContinuousMovement.cs` script:

        using UnityEngine.XR;
        using UnityEngine.XR.Interaction.Toolkit;

    And add an `XRNode` variable:

        public class ContinuousMovement : MonoBehaviour
        {
            // Add this:
            public XRNode inputSource;

3. With `VR Rig` selected, in the inspector, under `Continuous Movement` set `Input Source: Left Hand`.
4. Back in `ContinuousMovement.cs`, set `class ContinuousMovement` to the following:

        public class ContinuousMovement : MonoBehaviour
        {
            public float speed = 1;
            public XRNode inputSource;
            private Vector2 inputAxis;
            private CharacterController character;

            // Start is called before the first frame update
            void Start()
            {
                character = GetComponent<CharacterController>();

            }

            // Update is called once per frame
            void Update()
            {
                InputDevice device = InputDevices.GetDeviceAtXRNode(inputSource);
                device.TryGetFeatureValue(CommonUsages.primary2DAxis, out inputAxis);
            }

            private void FixedUpdate()
            {
                Vector3 direction = new Vector3(inputAxis.x, 0, inputAxis.y);

                character.Move(direction * Time.fixedDeltaTime * speed);
            }
        }

5. Add a `Character Controller` component to the `VR Rig`. This is the "Capsule Collider" that defines how the player interacts with obstacles. For the `Character Controller`, set `Radius: 0.15` and `Center: 0 1 0`. This makes the capsule tall and thin, starting from the ground.

You should be able to build and run now, and move with the left joystick (but not turn). But teleport also appears to be broken now?

### Fixing Direction

To set the movement direction towards where we are facing.

1. Edit `ContinuousMovement.cs`:

    Add a new variable to `class ContinuousMovement`:

        private XRRig rig;

    Set it in start:

        void Start()
        {
            character = GetComponent<CharacterController>();
            // Add this line:
            rig = GetComponent<XRRig>();
        }

    Use it in `FixedUpdate()`:

        // Get the `headYaw`:
        Quaternion headYaw = Quaternion.Euler(0, rig.cameraGameObject.transform.eulerAngles.y, 0);
        // Update the direction by multiplying by it:
        Vector3 direction = headYaw * new Vector3(inputAxis.x, 0, inputAxis.y);

You should be able to build and run now, and the movement will follow the direction your head is pointed in. Notably, this will not include gravity, you can add a plane as a ramp and walk off of it to illustrate this.

### Gravity

1. Edit `ContinuousMovement.cs`:

    Add variables:

        public float gravity = -9.81f;
        public LayerMask groundLayer;
        private float fallingSpeed;

    Implement gravity:

        private void FixedUpdate()
        {
            Quaternion headYaw = Quaternion.Euler(0, rig.cameraGameObject.transform.eulerAngles.y, 0);
            Vector3 direction = headYaw * new Vector3(inputAxis.x, 0, inputAxis.y);

            character.Move(direction * Time.fixedDeltaTime * speed);

            // Everything below here is new
            bool isGrounded = CheckIfGrounded();
            if (isGrounded)
                fallingSpeed = 0;
            else
                fallingSpeed += gravity * Time.fixedDeltaTime;

            character.Move(Vector3.up * fallingSpeed * Time.fixedDeltaTime);
        }

        bool CheckIfGrounded()
        {
            Vector3 rayStart = transform.TransformPoint(character.center);
            float rayLength = character.center.y + 0.01f;
            bool hasHit = Physics.SphereCast(rayStart, character.radius, Vector3.down, out RaycastHit hitInfo, rayLength, groundLayer);
            return hasHit;
        }

### Ground Layer

In order for `CheckIfGrounded()` needs to know the `groundLayer`. We could select `VR Rig`, and in the inspector set `Continuous Movement > Ground Layer: Everything`, but it's better to make a new ground layer.

1. In the upper right toolbar, choose `Layer > Add Layer`. Name a free layer `Ground`.
2. In the hierarchy, select each object that should be ground, and in the inspector set `Layer: Ground`.
3. Select `VR Rig` and in the inspector set `Continuous Movement > Ground Layer: Everything`.

### Character Collider

The character collider needs to be tied to the player if they move in VR without using the joystick.

1. Edit `ContinuousMovement.cs`:

    Add a new public variable:

        public float additionalHeight = 0.2f;

    Create a `CapsuleFollowHeadset()` method:

        void CapsuleFollowHeadset()
        {
            character.height = rig.cameraInRigSpaceHeight + additionalHeight;
            Vector3 capsuleCenter = transform.InverseTransformPoint(rig.cameraGameObject.transform.position);
            character.center = new Vector3(capsuleCenter.x, character.height / 2 + character.skinWidth, capsuleCenter.z);
        }

    Call it at the start of `FixedUpdate()`:

        private void FixedUpdate()
        {
            CapsuleFollowHeadset();

