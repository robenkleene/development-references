# React 3D Cube

1. Make a new react project with `npx create-react-app 3d`.
3. Install dependencies with `npm install react-three-fiber three`
3. Replace the contents of `App.js` with the following:

    ``` javascript
    import React from "react";
    import { Canvas } from "react-three-fiber";

    import './App.css';

    function Cube() {
      return (
        <mesh rotation={[10, 10, 0]} position={[0, 0, 0]}>
          <boxBufferGeometry attach="geometry" args={[1, 1, 1]} />
          <meshStandardMaterial attach="material" color="pink" />
        </mesh>
      );
    }

    function Scene() {
      return (
        <>
          <ambientLight />:
          <pointLight intensity={0.3} position={[-1, 2, 4]} />
          <Cube />
        </>
      );
    }

    function App() {
      return (
        <Canvas>
          <Scene />
        </Canvas>
      );
    }

    export default App;
    ```
4.

5. Run `npm start` to run your project