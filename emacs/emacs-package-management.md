# `emacs` Package Management

- `M-x package-list-packages`: List Packages
- `i`: Mark selected package for installation
- `d`: Mark selected package for deletion
- `u`: Unmark selected package
- `U`: Update all packages
- `x`: Execute commands on marked packages

## Upgrading

- `M-x package-autoremove`: Delete unused packages
- `~`: Mark obsolete packages for deletion (then `x` to execute)

## Troubleshooting

If a package won't install, try `package-refresh-contents`.
