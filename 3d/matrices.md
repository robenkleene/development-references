# Matrices

- 3x3 matrices are called "special orthogonal" (or "orthonormal") matrices and can represent "pure" rotations
- 4x4 matrices are "transformation matrices" and can represent rotation, translation, and scale.
- The inverse of a matrix is the matrix undoes the effects of a matrix. The inverse of `A` is represented as `A^-1`
- The transpose of a matrix is denoted with `A^T`, the inverse of a orthogonal (pure rotation) matrix is equal to its transpose

#### Combining

- If `P = A * B`, then `P` applies `A` and `B` (e.g., if `A` scales and `B` rotates then `P` scales and rotates)

## Rotation

Rotate a 2x2 matrix in two dimensions:

![2D Rotation](assets/matrix-rotation-2d.png)

This really a 3D rotation around the *z*-axis.

Rotation a 3x3 matrix:

![3D Rotation](assets/matrix-rotation-3d.png)

A 3x3 matrix cannot represent translations because translating a point **R** by a translation **T** requires adding the components of **t** to the components of **r** individually:

![Matrix Translation Equation](assets/matrix-translation-equation.png)
