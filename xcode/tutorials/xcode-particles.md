# Xcode Particles

1. Create a new Xcode project, select the `Game` template
2. Use `File > New File...` (`⌘N`) to create a new file, select type `SpriteKit Particle File`
3. Replace the contents of the `GameScene` class in `GameScene.swift` with the following:

        override func didMove(to view: SKView) {
            backgroundColor = UIColor.black

            if let rainParticles = SKEmitterNode(fileNamed: "Rain.sks") {
                rainParticles.position = CGPoint(x: size.width/2, y: size.height)
                rainParticles.name = "rainParticle"
                rainParticles.targetNode = scene

                addChild(rainParticles)
            }
        }

