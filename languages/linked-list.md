# Linked List

- Arrays allow random access, whle linked lists only allow sequential access. Random access is `O(n)` for a linked list (it's `O(1)` for an array).
- Items can be added to a linked list indefinitely, whereas arrays have a fixed size and eventually need to be resized.

## Notes

- Any linked list operation that can change the first node, e.g., to insert at index `0`, or remove the first element, needs to take a double pointer, rather than a pointer, because otherwise changing the first element wouldn't be possible.