# C Hash

This hash implementation is from chapter 6.6, "Table Lookup" from the *C Programming Language*:

> The hashing function, which is used by both lookup and install, adds each character value in the string to a scrambled combination of the previous ones and returns the remainder modulo the array size. This is not the best possible hash function, but it is short and effective.

``` c
unsigned hash(char *s)
{
    unsigned hashval;
    for (hashval = 0; *s != '\0'; s++)
      hashval = *s + 31 * hashval;
    return hashval % HASHSIZE;
}
```

This function takes a `char` pointer, and returns an `unsigned` to use as 

- `*s + 31 * hashval`: Multiplying by `31` looks to be just to multiply by a prime number 
- `hashval % HASHSIZE`: This is probably just to get the result in the range `0` to `HASHSIZE`.