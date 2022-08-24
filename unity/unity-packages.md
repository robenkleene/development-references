# Unity Packages

## Local Overrides

1. Copy the package from `Library/PackageCache` to `Packages` (and remove the version suffix)
2. Edit `package-lock.json`, find the top level entry for the reverse URL, change the `version:` to `file:<reverse url>`, and change the `source:` to `embedded`, remove the URL

