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
        let command = mov()
            .current_dir(tmp_dir_path)
            .write_stdin(input)
            .args(&["change", "altered", "-w"])
            .assert()
            .success();
        let output = command.get_output();
        println!("stdout = {:?}", String::from_utf8_lossy(&output.stdout));
        println!("stderr = {:?}", String::from_utf8_lossy(&output.stderr));
```
