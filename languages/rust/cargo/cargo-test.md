# `cargo` Test

- `cargo test <test-function-name>`: Run a single test

## Binary

These options are passed to the test binary and therefore *go after the `--`*.

- `cargo test -- --nocapture`: Don't suppress output for successful tests

## Diff

In test diff output, the expected output is shown first.
