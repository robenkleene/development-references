# Updating an Atom Package

## 1. Setup for Development

1. Navigate to the folder in Terminal
2. Create a dev link:

	apm link --dev

## 2. Publish

Pick one:

	apm publish patch
	apm publish minor
	apm publish major

## 3. Unlink

	apm unlink --dev