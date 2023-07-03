# Cargo `lldb`

1. `lldb target/debug/reap`
2. `process launch` (or `process launch -i tests/data/grep.txt`)

## Tests

To run a test in `lldb` we first need the path to the compiled test binary, which is printed out when `cargo test` is run, it looks like this:

    target/debug/deps/<project-name>-d1d452730bf9464b

Note that `cargo tests` runs *2 test targets*, one for integration tests and one for unit tests, you'll need to get the target for the one that's running your test. It's usually the second one.

- Use `rust-lldb` for niceties like pretty printing.

1. Run `rust-lldb target/debug/deps/<project-name>-d1d452730bf9464b`
2. Set breakpoints, e.g., `b src/file.rs:20`
3. In `lldb` run `run <test-name>` (or `run --test <test-name>`)

## Installed

1. `cargo install --path . --debug`
2. `lldb .cargo/bin/reap`
3. Set breakpoints, e.g., `b src/file.rs:20`
