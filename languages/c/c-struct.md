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

Member values can be accessead with dot notation:

``` c
printf("%d, %d\n", pt.x, pt.y);
```

Declaring a struct and a variable at the same time;

``` c
struct point {
    int x;
    int y;
} myPoint;

int main() {
    myPoint.x = 5;
    myPoint.y = 10;
}
```
