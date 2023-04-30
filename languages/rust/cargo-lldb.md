# Cargo `lldb`

## Tests

To run a test in `lldb` we first need the path to the compiled test binary, which is printed out when `cargo test` is run, it looks like this:

    target/debug/deps/<project-name>-d1d452730bf9464b

1. Run `lldb target/debug/deps/<project-name>-d1d452730bf9464b`
2. Set breakpoints, e.g., `b src/file.rs:20`
3. In `lldb` run `run --test <test-name>`

## Installed

1. `cargo install --path . --debug`
2. `lldb .cargo/bin/reap`
3. Set breakpoints, e.g., `b src/file.rs:20`
