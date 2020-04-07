# CSS BEM

- **Block**: A standalone entity (`.block`).
- **Element**: Something that is only ever nested inside a block (`.block__elem`).
- **Modifier**: Types of blocks or elements (`.block--mod` or `.block__elem--mod`).

## Rules

- Never nest CSS rules
- You should apply a reset to the element you are styling.
- Avoid tag selectors

## Resets

BEM does not recommend CSS resets because it break independence. If the reset is not applied, then the style will not look right, therefore the styles are not independent.