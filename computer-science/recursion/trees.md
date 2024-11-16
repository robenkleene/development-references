# Trees

There are four common types of tree traversal:

1. Depth-First Recursive (uses the call stack as the stack)
2. Depth-First Iterative (uses an array as a stack)
3. Breadth-First Iterative (uses an array as a queue)

## Depth-First Recursive

``` python
def dfs_recu(curr: Node[T], goal: Optional[T] = None, visited: Optional[List[Node[T]]] = None) -> List[Node[T]]:
    visited = visited or [curr]
    if goal is not None and curr.val == goal:
        return visited
    if curr.left:
        visited += dfs_recu(curr.left, goal, [curr.left])
    if curr.right:
        visited += dfs_recu(curr.right, goal, [curr.right])
    return visited
```

## Depth-First Iterative

``` python
def dfs_iter(start: Node[T], goal: Optional[T] = None) -> List[Node[T]]:
    visited, stack = [], [start]
    while stack:
        curr = stack.pop()
        visited.append(curr)
        if goal is not None and curr.val == goal:
            return visited
        if curr.left:
            stack.append(curr.left)
        if curr.right:
            stack.append(curr.right)
    return visited
```

## Breadth-First Iterative

``` python
def bfs_iter(start: Node[T], goal: Optional[T] = None) -> List[Node[T]]:
    visited, queue = [], [start]
    while queue:
        curr = queue.pop(0)
        visited.append(curr)
        if goal is not None and curr.val == goal:
            return visited
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
    return visited
```

