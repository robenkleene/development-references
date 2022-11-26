# Cargo

- `cargo new <project>`: Create a new project
- `cargo run`: Run current project (from the root directory)
- `cargo test`: Run tests for current project (from the root directory)
- `cargo run --bin <filename>`: Run file in `src/bin`
- `cargo test --bin <filename>`: Run tests for file in `src/bin`
- `cargo check`: Validate current project
- `cargo run -- <arg1> <arg2>`: Run with arguments (the `--` is optional)
- `cargo add <crate>`: Add a dependency and update the `Cargo.toml` file

## Tests

- When running tests, output is suppressed for successful tests, this can be disabled by passing the `--nocapture` option, which oddly has to be prefixed with `--` resulting in:

```
cargo test -- --nocapture
```

- `cargo test <test-function-name>`: Run a single test


## Running Single Files

`cargo new <project>` will have created a directory structure with `Cargo.toml` and `src/` directory.

1. Add a `src/bin` directory and add single `<filename>.rs` files in it
2. To run them, use `cargo run --bin <filename>`
3. To run tests, use `cargo test --bin <filename>`

## Installing

```
cargo install [--path <path-to-dir>]
```
