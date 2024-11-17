# LRU

## Node Class

It's a node to construct a doubly-linked list (because there's references to the next and previous nodes).

``` python
class Node():
    """
    A node in the doubly linked list used by the LRU Cache.
    """
    def __init__(self):
        self.key = None
        self.value = None
        self.prev = None
        self.next = None
```

## LRU Class

### Constructor

Setup sentinel nodes for the head and tail, these nodes never change.

``` python
class LRUCache():
    """
    LRU Cache with a fixed capacity.
    """
    def __init__(self, capacity):
        self.cache = {}
        self.size = 0
        self.capacity = capacity
        self.head, self.tail = Node(), Node()
        self.head.next = self.tail
        self.tail.prev = self.head
```

### Add

Inserts a node right after the head node.

``` python
def _add(self, node):
    node.prev = self.head
    node.next = self.head.next
    self.head.next.prev = node
    self.head.next = node
```

### Remove

``` python
def _remove(self, node):
    prev = node.prev
    new = node.next
    prev.next = new
    new.prev = prev
```
