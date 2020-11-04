# C Format String

Format specifiers.

## Integer (also unsigned)

    printf("INT_MAX = %d\n", INT_MAX);

Or

    printf("%i", r);

## Char

    printf("%c", s2[k]);

## String (Character Array)

    char longest[MAXLINE];
    printf("%s", longest);

## Float

    printf("%3d %6.1f\n", cel, cel * (9.0 / 5.0) + 32);

## Unsigned Long

    printf("%lu\n", strtol(s, NULL, 16));

## Unsigned Long Long

    printf("ULLONG_MA = %llu\n", ULLONG_MAX);
