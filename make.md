# Make

In `Makefile`, it's really difficult to pass a parameter to a `make` command, e.g., `make force_deploy -f`. This is because in `make` parlance the arguments are all supposed to be files to run the command on, so it breaks the paradigm. Instead to solve this just make a separate shell script.

## Tips

To suppress output of a command, precede it with an `@`:

    hello:
        @echo "hello world"

## Functions

    define test_message
        remote=$$(git config --get remote.origin.url | tr -d '\n'); \
        if [[ $${remote}  =~ (https://|git@)github.com[/:](.*) ]]; then \
          remote_subpath="$${BASH_REMATCH[2]}"; \
          remote_subpath=$${remote_subpath%.git}; \
          remote_url="https://github.com/$${remote_subpath}/pulls"; \
        else \
          echo ""; \
          exit 0; \
        fi; \
        echo "Hello $${remote_url} $1"
    endef

    run_test: test_start test_finish

    test_start:
        @$(call test_message,CISTARTED)

    test_finish:
        @$(call test_message,CIFINISHED)

## Variables

    NAME = robenkleene_macos
    ERGODOX_DIR = ../qmk_firmware/keyboards/ergodox_ez/keymaps/
    PLANCK_DIR = ../qmk_firmware/keyboards/planck/keymaps/
    ERGODOX = $(ERGODOX_DIR)$(NAME)
    PLANCK = $(PLANCK_DIR)$(NAME)

    link:
        ln -s ergodox_ez/$(NAME) $(ERGODOX_DIR)
        ln -s planck/$(NAME) $(PLANCK_DIR)

