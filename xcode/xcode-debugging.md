# Xcode Debugging

## Breakpoints

To make a conditional breakpoint, double-click the breakpoint and set something that returns a boolean, like `dict[@"key"] != nil` in the `Condition` field.

## Expressions

    expr dict = [dict mutableCopy]
    expr  dict[@"key"] = @"string"
