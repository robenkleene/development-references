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
9. Click `Particle System > Circle` and toggle on `Color over Lifetime`, click the `Color` bar, and make a gradient that has `0` alpha on each side and `255` alpha in the center.
10. Set the `Start Color` for the circle to a purple.

## More Particles

1. Add a new particle system under `PS_OrbElectric` and rename it to `Particles`
3. With `Hierarchy > Sample Scene > PS_OrbElectric > Particles` selected, click `Particles` and under `Shape` set `Shape: Sphere`
