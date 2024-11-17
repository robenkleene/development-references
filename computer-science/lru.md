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

### Add (Private)

Inserts a node right after the head node.

``` python
def _add(self, node):
    node.prev = self.head
    node.next = self.head.next
    self.head.next.prev = node
    self.head.next = node
```

### Remove (Private)

``` python
def _remove(self, node):
    prev = node.prev
    new = node.next
    prev.next = new
    new.prev = prev
```

### Move to Head (Private)

Since adding it inserts it as the first node, removing and adding moves to the first node.

``` python
def _move_to_head(self, node):
    self._remove(node)
    self._add(node)
```

### Pop (Private)

Remove the least recently used node.

``` python
def _pop(self):
    node = self.tail.prev
    self._remove(node)
    return node
```

### Get

Retrieves a value from the cache by key:

1. Looks up the key in the dictionary.
2. If the key is found, moves the node to the head of the list and returns its value.
3. If the key is not found, returns `None`.

``` python
def get(self, key):
    """
    Retrieves the value associated with the key.
    """
    node = self.cache.get(key, None)
    if not node:
        return None
    self._move_to_head(node)
    return node.value
```

### Put

Inserts or updates a key-value pair in the cache:

1. If the key exists, updates its value and moves the node to the head.
2. If the key does not exist, creates a new node and adds it to the head.
3. If adding the new node exceeds the cache's capacity, removes the least recently used node.

``` python
def put(self, key, value):
    """
    Inserts or updates a key-value pair in the cache.
    """
    node = self.cache.get(key)

    if not node:
        # Key not in cache; create a new node.
        new = Node()
        new.key = key
        new.value = value
        self.cache[key] = new
        self._add(new)
        self.size += 1
        if self.size > self.capacity:
            # Cache is full; remove the least recently used item.
            tail = self._pop()
            del self.cache[tail.key]
            self.size -= 1
    else:
        # Key exists; update the value and move to head.
        node.value = value
        self._move_to_head(node)
```
