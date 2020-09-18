# `npm`

- `npm init`: Create a `package.json`
- `npm publish`: Publish a new version

## Notes

- `--save` is not necessary because that's the default now, `--no-save` used to be the default.

## Other

- `-g`: install globally, e.g., `npm install -g markdown-toc`
- `npm install --save-dev` / `npm i -D`: Install for development only

## Uninstall

- `npm uninstall <package>`

## Clean Up

- `npm prune` is supposed to uninstall unused packages

## Update All Dependencies

This requires the separate `npm` module `npm-check-updates` (usually installed globally).

1. `ncu --upgrade` / `ncu -u`
2. `npm install`

## Info

    npm view yarn

## Scripts

List available commands:

    npm run
