# C Strings

C has two ways of storing a string:

- `char*`: A pointer
- `char[]`: An array

These are technically different types, but a `char` array is coerced into a pointer if it's passed as a parameter to a function that takes a `char` pointer.