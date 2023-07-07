# Cargo `lldb`

1. `lldb target/debug/reap`
2. `process launch` (or `process launch -i tests/data/grep.txt`)

## Tests

To run a test in `lldb` we first need the path to the compiled test binary, which is printed out when `cargo test` is run, it looks like this:

    target/debug/deps/<project-name>-d1d452730bf9464b

Note that `cargo tests` runs *2 test targets*, one for integration tests and one for unit tests, you'll need to get the target for the one that's running your test. It's usually the second one.

- Use `rust-lldb` for niceties like pretty printing (I couldn't get this to work with a non-default `lldb` install location like on Linux).

1. Run `rust-lldb target/debug/deps/<project-name>-d1d452730bf9464b`
2. Set breakpoints, e.g., `b src/file.rs:20`
3. In `lldb` run `run <test-name>` (or `run --test <test-name>`)

### Troubleshooting

## Installed

1. `cargo install --path . --debug`
2. `lldb .cargo/bin/reap`
3. Set breakpoints, e.g., `b src/file.rs:20`

## CLI Tests

CLI tests (e.g., using `Command::cargo_bin("rep")`) involve two different binaries, one is the CLI binary, and the other is the test binary.

To test these, the following steps should work, but they don't (attaching fails with `unable to start the exception thread`):

1. `lldb target/debug/<binary-name>`
2. `(lldb) process attach --name <binary-name> --waitfor`
3. `cargo test`
