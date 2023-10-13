# 3D File Formats

- Things you need to display 3D: Canvas, Scene, Lights, and Mesh.
- Not all exporters export all information.

## Model

Only includes the model.

- `OBJ`: Includes has simple material model (no PBR). But doesn't have lights, cameras, animation, or shadows

## Scene Graph

Includes a scene graph (multiple models laid out in a graph), usually includes material definitions and animations.

- `glTF`: Includes materials, animations, cameras, lights, and ambient occlusion. You need to either bake in shadows or enable them (with the JavaScript API) on any lights in your scene.
- `fbx`
- `abc`

## Universal Scene Description

Supports above features, and has features for collaboration.