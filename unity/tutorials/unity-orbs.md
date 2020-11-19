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