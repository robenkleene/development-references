# Swift Style Guide

## Naming Conventions

* Don't restate type information, but do clarify roles, e.g., `processItem(atPath:` and `downloadItem(at:` are good, but `downloadItem(atURL:` is not.

### Prepositions

* Use `for`, e.g., `item(forIdentifier:` when retrieving an item from a collection. This matches `object(forKey:)`.
* Use `with` when initializing an object, e.g., `processItem(withData:)`. This matches standard Objective-C initializer conventions.
* Use `at` when referring to a location on the file system or a URL, e.g., `processItem(atPath:` or `downloadItem(at:`
* Use `of` when the method retrieves metadata from an object, e.g., `identifier(of:`
* Use `from` when performing a transformation `identifier(from:`
