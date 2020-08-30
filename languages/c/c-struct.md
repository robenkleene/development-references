# C Struct

Declare a `struct`:

``` c
struct point {
    int x;
    int y;
};
```

Declare a `struct` variable:

``` c
struct point pt;
```

A `struct` variable can be declared and initialized at once by providing memeber values:

``` c
struct point maxpt = { 320, 200 };
```


``` c
typedef struct node {
    int val;
    struct node *next;
} node_t;
```