# Linked List

- You can't access an arbitrary element in a linked list in constant time. If you want to get an item by index, you have to traverse through each node, resulting in linear time (`O(N)`).
- Good use cases for linked lists are stacks and queues.
- Any linked list operation that can change the first node, e.g., to insert at index `0`, or remove the first element, needs to take a double pointer, rather than a pointer, because otherwise changing the first element wouldn't be possible.