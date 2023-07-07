# `lldb` Process

- `(lldb) process launch`: Start program
- `(lldb) process launch -i <file-path>`: Start program, passing `<file-path>` to the programs STDIN
- `(lldb) process launch -i <file-path>`: Start program with STDIN and arguments
- ``(lldb) process attach --name <binary-name> --waitfor`: Attach to process after it launches
