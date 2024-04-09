# Linked List

- Arrays allow random access, while linked lists only allow sequential access. Random access is `O(n)` for a linked list (it's `O(1)` for an array).
- Items can be added to a linked list indefinitely, whereas arrays have a fixed size and eventually need to be resized.

## Notes

- Any linked list operation that can change the first node, e.g., to insert at index `0`, or remove the first element, needs to take a double pointer (e.g., `node_t **head`), instead of a pointer, because otherwise it's not possible to change the first element, since the a linked list is kept track of by holding a reference to the first node.