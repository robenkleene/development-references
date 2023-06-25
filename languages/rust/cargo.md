# Cargo

- `cargo new <project>`: Create a new project
- `cargo run`: Run current project (from the root directory)
- `cargo test`: Run tests for current project (from the root directory)
- `cargo run --bin <filename>`: Run file in `src/bin`
- `cargo test --bin <filename>`: Run tests for file in `src/bin`
- `cargo check`: Validate current project
- `cargo run -- <arg1> <arg2>`: Run with arguments (the `--` is optional)
- `cargo add <crate>`: Add a dependency and update the `Cargo.toml` file

## Build

- `cargo build`: Build project
- Once the project has been built, the binary can be accessed at `./target/debug/<executable-name>`

## Removing

- To remove a dependency, just delete its line from `Cargo.toml` and run `cargo build` (which should remove it from `Cargo.lock`)

## Troubleshooting

- `cargo clean` and try again
