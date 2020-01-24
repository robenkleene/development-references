# Bitwise Operators

- `&`: AND, used to mask off some set of bits, e.g., `n & 0177` masks off all but the lower-order 7 bits of `n` because `0177` (which is in octal) is 127 in base-10, which is seven ones in the lower-order bits in binary.
- `|`: OR
- `^`: Exclusive OR
- `<<`: Left shift, e.g., `0b100 << 2 = 0b10000`
- `>>`: Right shift, e.g., `0b100 >> 2 = 0b1`
- `~`: One's complement (unary operator), inverts all `1` and `0`. E.g., `~00001 = 11110`

## Interesting Numbers

- `0` is of course all zeros.
- `~0` is an easy way to make all ones.
- `~(~0 << n)` is `n` ones to the right and the rest zeros.
