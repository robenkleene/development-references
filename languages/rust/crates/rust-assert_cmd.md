# `assert_cmd`

To debug by printing the output, with:

```
        let output = mov()
            .current_dir(tmp_dir_path)
            .write_stdin(input)
            .args(&["change", "altered", "-w"])
            .assert()
            .success().get_output();
```

Change to:

```
        let output = mov()
            .current_dir(tmp_dir_path)
            .write_stdin(input)
            .args(&["change", "altered", "-w"])
            .assert()
            .success().get_output();
```
