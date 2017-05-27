# Swift Style Guide

## Naming Conventions

* Don't restate type information, but do clarify roles, e.g., `processItem(atPath:` and `downloadItem(at:` are good, but `downloadItem(atURL:` is not.

### Prepositions

* Use `with` when initializing an object, e.g., `processItem(withData:)`. This matches standard Objective-C initializer conventions.
* When retrieving an object based on an argument: Use `for` if the argument is entity if and of itself, e.g., `forKey` or `forResource`, but use `with` if the argument only exists as an attribute of what's being retrieved, e.g., `withIdentifier` or `withName`.
* Use `at` when referring to a location on the file system or a URL, e.g., `processItem(atPath:` or `downloadItem(at:`
* Use `of` when the method retrieves metadata from an object, e.g., `identifier(of:`
* Use `from` when performing a transformation `identifier(from:`
