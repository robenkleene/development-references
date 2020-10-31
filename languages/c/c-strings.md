# C Strings

C has two ways of storing a string:

- `char*`: A pointer
- `char[]`: An array

These are technically different types, but a `char` array is coerced into a pointer if it's passed as a parameter to a function that takes a `char` pointer.

A `char` pointer can be iterated through with `s++`, as in the following examples to print the string:

``` c
void hash_test(char *s) {
    while (*s != '\0') {
        printf("%c", *s);
        s++;
    }
}
```