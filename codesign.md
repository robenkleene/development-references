# `codesign`

- `codesign -dvvv <path>`: Check code sign status
- `codesign --verify --verbose  <path>`: Verify code sign
- `codesign --force --options runtime --sign "Developer ID Application" <path>`: Re-sign
- `codesign -d --entitlements :- /Applications/Whatever.app/`: List entitlements
