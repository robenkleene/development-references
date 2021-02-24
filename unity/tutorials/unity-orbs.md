# Unity Orbs

## Setup

1. Create a new project using the `Universal Project Template`.
2. Select `Window > Package Manager` and install `Visual Effect Graph` and `Shader Graph`.
3. Delete the `Example Assets`.
4. Right-click in `Assets` and select `Create > Visual Effects > Visual Effect Graph`, name it `Magic_Orb`.
5. Drag `Magic_Orb` into the `SampleScene` to make it appear in the scene.
6. With `Magic_Orb` selected in the scene, click `Edit` in the inspector to the right of `Visual Effect > General > Asset Template`.
7. Dock the `Magic_Orb` edit panel to the right of the scene viewport by dragging its tab.
8. In the `Magic_Orb` edit panel, toggle off the `Target GameObject` tab.
9. Select the existing nodes and right-click to delete them.

## Graph

1. Hover over the `Magic_Orb` panel and hit `␣` to add a `Simple Head & Trails (System)` node system.
2. Set `Spawn > Rate: 50`.
3. Set `Initialize Particle > Capacity: 1000`.
4. Set `Initialize Particle Strip > Capacity: 1000`.
5. Add a `float` property by clicking the `+` button then `float` in the properties panel.
6. Rename the property to `TrailsSpawnRate`. Toggle the disclosure triangle, and turn on `Exposed`, and set `Value: 30`.
7. Drag the `TrailsSpawnRate` property out to the nodes editor area to create a node, and connect its output to the `Spawn > Rate` input.
8. In `Initialize Particle`, delete `Set Velocity Random (Per-component)` and `Set Color Random from Gradient` (with `⌘⌫`).

### Color

1. Add a `Set Color (Attribute Set)` block above the `Set Lifetime Random (Uniform)` block.
2. Add a `Color` property and rename it to "Color" and move it above `TrailsSpawnRate`. Click the `Color` disclosure triangle and toggle on `Exposed`.
3. Drag the property to the left of the `Set Color` block and connect the output of the `Color` property to the input of the `Set Color` block.
4. Double-click the color well in the inspector to open the color picker and choose a light blue color and increase the intensity slightly.

### Position

1. Add a `Position (Sphere)` below the `Set Color`.
2. Add a `float` property to the inspector and rename it to "Size", toggle on `Exposed` and set `Value: 1`.
3. Drag the `Size` property onto the canvas. Add a `Multiply (Operator Math Arithmetic)`, connect the output of `Size` to its top input, and connect its output to the `Position (Sphere) > Arc Sphere > Sphere > Radius` input.

### Trails

1. Add a `float` property to the inspector and rename it to "Trails Lifetime". Toggle on `Exposed` and set `Value: 1`.
2. Drag the `Trails LIfetime` property onto the canvas. Add a `Multiply (Operator Math Arithmetic)`, connect the output of `Trails Lifetime` to its top input, and connect its output to the `Set Lifetime Random (Uniform) > A` input.
3. Add a second `Multiply (Operator Math Arithmetic)`, also connect the output of `Trails Lifetime` to its top input, and connect its output to the `Set Lifetime Random (Uniform) > B` input. Set the `B: 3`. (`A` is the minimum and `B` is the maximum, so this sets the trails lifetime range to `n < x < n * 3`.)

### Sphere

1. Add a `Conform to Sphere (Force)` block below `Turbulence`.
2. Drag another copy of the `Size` property onto the canvas to the left of the `Conform to Sphere` block. Add another `Multiply (Operator Math Arithmetic)`, and connect the output of the `Size` to its `A` input. Set `B: 1.5`. Connect the output of the `Multiply (float)` to the `Sphere > Radius` input.
3. In the `Conform to Sphere`, set `Attraction Force: 10` and `Stick Force: 5`.

### Lifetime

1. Delete the `Initialized Particle Strip > Set Lifetime` block, and replace it with a `Inherit Source Lifetime (Set)` block.
2. Add a `Set Size (Attribuate Set)` above `Output ParticleStrip Quad > Set size over Life`, and uncheck the toggle for `Inherit Source Lifetime (Set)` to disable it. 
3. Drag out the `Size` property from the inspector to the left of `Output ParticleStrip Quad > Set Size`.
4. Add two `Multiply (Operator Math Arithmetic)` nodes, and connect the output of `Size` to their `A` input. Set the `B` for the top node to `0.001`, and `B` for the second node to `0.02`.
5. Add a `Random Number (Operator Random)`, and connect output of the top `Multiply (float)` to its `Min` input, and the output of bottom `Multiply (float)` to its `Max` input. Connect the `Random Number` output to the `Output ParticleStrip Quad > Set Size > Size` input.
6. Click the checkbox to the far left of `Set Size over Life` to toggle it on, and in the Inspector, set `Composition: Add`.

## Group

1. Select all the nodes and right-click and select `Group Selection`, rename the group to `TRAILS`.

## New Particle System

1. Create a new `Empty Particle System (System)` off to the right by hitting `␣`.
2. Select the first block, `Spawn`, and right-click and select `Create Block`, and choose `Periodic Burst (Spawn)`. Set `Count: 1` and `Delay: 1`.
3. Make some space by dragging `Update Particle` and `Output Particle Quad` down.
4. Create a `Add Lifetime (Attribute Set)` block under `Initialize Particle`.
5. Under `Output Particle Quad > Main Texture`, click the circle to the right, and choose the `Default-Particle` texture.

### Size

1. Add a `Add Size (Attribute Set)` at the bottom of the `Output Particle Quad`.
2. Drag the `Size` property out to the left of the `Set Size`, and add a `Multiply (Operator Math Arithmetic)` node.
3. Connect the output of `Size` to the `A` input of `Multiply (float)`, set `B: 10`, and connect the output of the `Multiply` to the input `Add Size > Size` input.
4. Add a `Set Color (Attribute Set)` above the `Set Size`.
5. Drag the `Color` property to the left of the `Set Color`, add a `Divide (Operator Math Arithmetic)`. Connect the output of the `Color` property to the input of the `Divide (Vector4)` and set its `B: 4`. Connect the output of the `Divide (Vector4)` to the `Set Color > Color` input.
6. Set the `Output Particle Quad > Blend Mode: Additive`

## Fading In and Out Particles

1. In `Output Particle Quad`, add an `Add Color over Life (Gradient) [Attribute Curve]` above `Set Color`.
2. Edit the `Add Color over Life` gradient, so there are three stops, one at each end with `Alpha: 0`, and one in the middle with `Alpha: 255`. This fades the particles in and out.

## Group

1. Select all of the nodes on the right, then right-click and select `Group Selection`. Rename the group to `BEAM`.

## Particle System

1. Insert a `Simple Particle System (System)` node.
2. Under `Output Particle Quad` click the icon next to `Texture`, and select `Default-Particle` (you can search for it at the top). Then set `Blend Mode: Additive`.
3. Under `Initialize Particle`, above `Set Lifetime Random (Uniform)`, insert a `Position (Sphere) [Position]`.
4. Drag the `Size` out from the properties panel to the left of `Position (Sphere) > Arc Sphere > Sphere > Radius`. Insert a `Multiply` node between the `Size` property and `Radius` input, connect the `Size` output to the `Multiply (float) > A` input. Connect the `Multiply` output to `Radius`. Set ``Multiply (float) > B: 2`.
5. In `Set Velocity Random (Per-Component)` set all the values under `A` to `-0.5` and `B` to `0.5`.
6. Set `Initialize Particle > Capacity: 1000000`
7. In the property inspector, click the `+` button and add a new `float` rename it to `SpawnRate`. Toggle on `Exposed` and give it a default value of `5000`.
8. Drag the `SpawnRate` property to the left of `Spawn > Constant Spawn Rate`, and connect its output to the `Rate` input.
9. Under `Output Particle Quad`, add a `Set Size` below `Set Size over Life`. Disable `Set Size over Life` by toggling off its checkbox.
10. Add a `Random Number (Operator Random)` to the left of `Set Size`, set `Min: 0.01` and `Max: 0.02` and connect its output to the input of `Set Size`.
11. Add a `Set Color (Attribute Set)` above `Set Color over Life`. Disable `Set Color over Life` by toggling off its checkbox. Drag the `Color` property from the properties panel to the left of `Set Color`, and connect the output of the `Color` property to the `Set Color` input.
