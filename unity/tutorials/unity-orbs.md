# Unity Orbs

## Setup

1. Create a new project using the `Universal Project Template`.
2. Select `Window > Package Manager` and install `Visual Effect Graph` and `Shader Graph`.
3. Delete the `Example Assets`.
4. Right-click in `Assets` and select `Create > Visual Effects > Visual Effect Graph`, name it `Magic_Orb`.
5. Drag `Magic_Orb` into the `SampleScene` to make it appear in the scene.
6. With `Magic_Orb` selected in the scene, click `Edit` in the `Inspector` to the right of `Visual Effect > General > Asset Template`.
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
9. Add a `Set Color (Attribute Set)` block above the `Set Lifetime Random (Uniform)` block.
10. Add a `Color` property and rename it to `Color` and move it above `TrailsSpawnRate`. Click the `Color` disclosure triangle and toggle on `Exposed`.
11. Drag the property to the left of the `Set Color` block and connect the output of the `Color` property to the input of the `Set Color` block.
12. Double-click the color well in the inspector to open the color picker and choose a light blue color and increase the intensity slightly.
13. Add a `Position (Sphere)` below the `Set Color`.
14. Add a float to the inspector and rename it to `Size`, toggle on `Exposed` and set `Value: 1`.
15. Add a `Multiply (Operator Math Arithmetic)`