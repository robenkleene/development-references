# Cargo

- `cargo new <project>`: Create a new project
- `cargo run`: Run current project (from the root directory)
- `cargo check`: Validate current project

## Running Single Files

`cargo new <project>` will have created a directory structure with `Cargo.toml` and `src/` directory.

1. Add a `src/bin` directory and add single `<filename>.rs` files in it
2. To run them, use `cargo run --bin <filename>.rs`
