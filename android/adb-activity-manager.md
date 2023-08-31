# `adb` Process

- `adb shell ps -A`: List all running processes
- `adb shell am force-stop <package-name>`: Quit a process
- `adb shell am kill <package-name>`: Kill an process
- `adb shell am start -n com.package.name/com.package.name.ActivityName`: Launch a package (usually `adb shell am start -n "$1/$1.MainActivity"`)
