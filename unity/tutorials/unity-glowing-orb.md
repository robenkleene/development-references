# Unity Glowing Orb

## Setup

1. Start a new 3D project called `Glowing Orb`
2. Right-click in the Hierarchy and choose `Create Empty` and name it `PS_OrbElectric`
3. Right-click `PS_OrbElectaric` and choose `Effects > Particle System` and name it `Circle`. Select `Circle`, and in the inspector, set `Transform > Rotation > X: -90` so it points straight up.
4. Select `PS_OrbElectric` and set `Transform > Position` `X: -17` and `Y: 3.01`.

## Circle

1. Under `Project > Assets`, right-click and make a new folder called `ParticleSystems`. Inside that folder, create another folder called `Orb_Electric`.
2. Make a glowing circle in Photoshop and export it as `Circle.png`, and then drag it into the `Orb_Electric` folder to add it to the project
3. Create a material by right-clicking the `Orb_Eletric` folder and choosing `Create > Material`.
4. Set `Shader` to `Mobile > Particles > Additive`.
5. Drag the `Circle` image asset onto the `None Texture Select` box for the `Circle` material
6. Drag the `Circle` material onto the `Hierarchy > SampleScene > PS_OrbElectric > Circle`, the particle system should start animating now, as long as `Hierarchy > SampleScene > PS_OrbElectric > Circle` is selected.
7. With `Hierarchy > SampleScene > PS_OrbElectric > Circle` selected, under `Particle System` in the inspector, set `Max Particles: 3`, `Duration: 5`, `Start Lifetime: 5`, `Start Size: 5`, and `Start Speed: 0`.
8. Click `Particle System > Circle`, toggle off `Shape`, and set `Emission > Rate Over Time: 1`. Toggle on `Size over Lifetime` and click the `Size` graph. Click the linear growth, i.e., `O` to `1`, graph preset (this might already be the default), then move the left side to `0.6`.
9. To stop the circles from disappearing instantly, click `Particle System > Circle` and toggle on `Color over Lifetime`, click the `Color` bar, and make a gradient that has `0` alpha on each side and `255` alpha in the center.
10. Set the `Start Color` for the circle to a purple.

## More Particles

1. Add a new particle system under `PS_OrbElectric` and rename it to `Particles`
2. With `Hierarchy > Sample Scene > PS_OrbElectric > Particles` selected, click `Particles` and under `Shape` set `Shape: Sphere`
3. Change `Start Speed` to a `Random Between Two Constants` by clicking the disclosure arrow to its right. Set the values to `0.1 1.2`
4. Change `Start Size` to a `Random Between Two Constants` by clicking the disclosure arrow to its right. Set the values to `0.1 0.5`
5. Select `Hierarchy > PS_OrbElectric > Circle`, `Particle System > Circle` and click `Renderer` to add it to the panel. Under `Renderer` in the panel, set `Max Particle Size: 3`
6. Select `Hierarchy > PS_OrbElectric > Particles` again and set `Start Lifetime` to `Random Between Two Constants`, and `Start Lifetime: 2 5`
7. Set the `Start Size: 0.05`
8. Set the `Start Color` to a purple
10. To stop the particles from disappearing instantly, click `Particle System > Particles` and toggle on `Color over Lifetime`, click the `Color` bar, and make a gradient that has `0` alpha on each side and `255` alpha in the center.
11. Click `Particle System > Particles` and toggle on `Size over Lifetime`, and set the graph to an ease in ease out from `1.0` to `0.5`
12. Set `Emission > Rate over Time: 50`

## Point of Light

### Photoshop

1. Create an 500x500 image
2. Give a layer an inner glow from the center of a purple color
3. Use another layer as a clipping mask that removes the center
    - To make the Clipping Mask layer itself (the base layer) transparent, right-click the base layer and select `Blending Options...` and toggle off `Blending Options > Advanced Blending > Blend Clipped Layers as Group`, then set the base layers `Fill: 0`.
4. Export as PNG

## Beam

1. Create a new material under `Project > ParticleSystems > Assets > Orb_Electric` named `Beam`
2. In the inspector, choose `Shader: Additive (Legacy Shaders/Particles/Additive`
3. Drag and drop the point of light PNG into `Assets > ParticleSystems > Orb_Electric`, then drag and drop it from there into the `Beam` inspectors `Name (Texture)` box
4. Drag and drop the `Beam` material onto `Hierarchy > SampleScene > PS_OrbElectric > Particles`
5. Select `Hierarchy > SampleScene > PS_OrbElectric > Particles` and choose `Start Rotation: Random Between Two Constants` and set `0` and `360` (this probably isn't necessary if your point of light is circularly symmetrical).
6. Add `Velocity over Lifetime` from the `Particles` drop-down menu in the inspector. Under the `Velocity over Lifetime` attribute, choose `Random Between Two Constants` for `Linear`. Set `-1` to `1` for X, Y, and Z.
7. Toggle on `Noise` and `Trails` in the inspector for `Particles`. In the `Renderer` section set the `Trail Material: Beam`
8. Under `Noise`, set `Strength: 5` and `Frequency: 2.3`

## Electric Beam

1. Create a new `Particle System` under `PS_OrbElectric`, and name it `ElectricBeam`. Set its `Position: 0 0 0` and `Rotation: -90 0 0`. Set its `Max Particles: 1` and `Start Speed: 0`. Toggle off `Shape`.
2. Create a new material and name it `ElectricCenter`. Set its `Shader` to `Legacy Shaders > Particles > Additive`. Drag and drog the point of light PNG from `Project` panel to the `Texture` well.
3. Drag and drop the `ElectricCenter` material from the `Project` panel to the `ElectricBeam` in the `SampleScene`.
4. Select `SampleScene > ElectricBeam` and in the inspector set `Particle System > ElectricBeam > Start Size` to `Random Between Two Constants` `0.5` `4.72`, set `Max Particles: 16`. Set `Emission > Rate over Time: 1`. Set the `Start Rotation` `Random Between Two Constants` `0` `360`. Set the same `Color over Lifetime` as before, a gradient transparent at both ends and opaque at the center. Set the `Size over Lifetime` to a linear graph, then move the left edge up to about `0.5`. Turn on `Rotation over Lifetime`.

## Light

1. Create a `Point Light` in `SampleScene`, rename it to `BeamLight`, in the inspector, set `Range: 4`. Make it a prefab by dragging and dropping it into the `Orb_Electric` folder in the project. Then delete it.
2. Select `ElectricBeam`, and toggle on `Lights`. In the `Lights` section in the inspector, drag `BeamLight` to the `Light` field. Set `Ratio: 1`. (This won't show up unless you add a surface under the orb for the light to shine onto.)
3. Set the `BeamLight` `Color` to a blue, then select `Circle` in the hierarchy and copy its pink color (by right-clicking), and paste it to `ElectricBeam > Start Color`.
4. Select `EletricBeam` and in the inspector set `Lights > Maximum Lights: 3`

## Smoke

1. Create a new `Particle System` under `PS_OrbElectric` and rename it to `SmokeOutside`. In the inspect set `Shape > Shape: Sphere`. Set `Start Speed: 0.31`, `Max Particles: 50`, and `Emission > Rate over Time: 25`.
2. Download a smoke PNG from Google and drag it into the `Orb_Electric` assets folder.
3. Create a new material in `Orb_Electric` and rename it to `SmokeOutside`. Choose `Shader: Additive (Legacy Shaders/Particles/Additive`.
4. Drag the smoke PNG image to the `SmokeOutside` material well, and drag the material itself to `SmokeOutside`.
5. Select `SmokeOutside` and set `Shape > Radius: 1.85`. Set `Start Lifetime: 1 4`, `Start Speed: 0.05 0.25`, `Start Rotation: 0 360` (all set to `Random Between Two Constants`). Set the `Start Color` to `Random Between Two Colors`, using the same pink used elsewhere, for the second color reduce the transparency to the smoke looks more realistic. Use the same trick for `Color over Lifetime`, a gradient transparent at both ends and opaque in the center. Change the `Size over Lifetime` to linear, and raise the left side a bit above `0.5`. Toggle on `Rotation over Lifetime`. Set `Renderer > Max Particle Size: 3`.
