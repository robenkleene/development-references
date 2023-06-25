# `cargo` Test

- When running tests, output is suppressed for successful tests, this can be disabled by passing the `--nocapture` option, which oddly has to be prefixed with `--` resulting in:

```
cargo test -- --nocapture
```

- `cargo test <test-function-name>`: Run a single test

