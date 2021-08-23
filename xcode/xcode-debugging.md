# Xcode Debugging

## Breakpoints

To make a conditional breakpoint, double-click the breakpoint and set something that returns a boolean, like `dict[@"key"] != nil` in the `Condition` field.

## Expressions

    expr dict = [dict mutableCopy]
    expr dict[@"key"] = @"string"

### Troubleshooting

`"cast the message send to the method's return type"`, add casting, e.g.:

    expr (NSString *)[value method] == (NSString *)dict[@"key"]

## `lldb`

Put aliases in `.lldbinit`:

    command alias my_po expression --object-description

Load with:

    command source ~/.lldbinit

Aliases can't use `po` instead replace it with `expression -O -l swift --` or `expression -O -l objective-c --` depending on the language.
