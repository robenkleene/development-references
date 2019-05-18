# Make

In `Makefile`, it's really difficult to pass a parameter to a `make` command, e.g., `make force_deploy -f`. This is because in `make` parlance the arguments are all supposed to be files to run the command on, so it breaks the paradigm. Instead to solve this just make a separate shell script.


