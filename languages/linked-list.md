# Linked List

- Random access is `O(n)` for a linked list (it's `O(1)` for an array).
- Arrarys have a fixed sized, linked lists can easily grow or shrink.

## Notes

- Good use cases for linked lists are stacks and queues. *Why?*
- Any linked list operation that can change the first node, e.g., to insert at index `0`, or remove the first element, needs to take a double pointer, rather than a pointer, because otherwise changing the first element wouldn't be possible.