# Cargo

- `cargo new <project>`: Create a new project
- `cargo run`: Run current project (from the root directory)
- `cargo test`: Run tests for current project (from the root directory)
- `cargo run --bin <filename>`: Run file in `src/bin`
- `cargo test --bin <filename>`: Run tests for file in `src/bin`
- `cargo check`: Validate current project

## Tests

- When running tests, output is suppressed for successful tests, this can be disabled by passing the `--nocapture` option, which oddly has to be prefixed with `--` resulting in:

```
cargo test -- --nocapture
```

## Running Single Files

`cargo new <project>` will have created a directory structure with `Cargo.toml` and `src/` directory.

1. Add a `src/bin` directory and add single `<filename>.rs` files in it
2. To run them, use `cargo run --bin <filename>`
