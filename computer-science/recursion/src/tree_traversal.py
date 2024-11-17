#!/usr/bin/env python3

from collections import deque
from typing import Optional, List, TypeVar, Generic

T = TypeVar("T")

class Node(Generic[T]):
    def __init__(self, val: T):
        self.left: Optional[Node[T]] = None
        self.right: Optional[Node[T]] = None
        self.val: T = val

    def __repr__(self) -> str:
        return str(self.val)

    def chain_string(self, level: int = 0, is_left: Optional[bool] = None) -> str:
        result = ""
        if self.left:
            result += self.left.chain_string(level + 1, True)
        char = '' if is_left is None else '/ ' if is_left else '\\ '
        result += ' ' * 4 * level + char + str(self.val) + "\n"
        if self.right:
            result += self.right.chain_string(level + 1, False)
        return result

class Tree(Generic[T]):
    def __init__(self):
        self.root: Optional[Node[T]] = None

    def __repr__(self) -> str:
        return self.root.chain_string() if self.root else ""

    @staticmethod
    def make(arr: List[T]) -> "Tree[T]":
        n = iter(arr)
        root = Node(next(n))
        fringe = deque([root])
        while True:
            head = fringe.popleft()
            try:
                head.left = Node(next(n))
                fringe.append(head.left)
                head.right = Node(next(n))
                fringe.append(head.right)
            except StopIteration:
                break
        tree = Tree()
        tree.root = root
        return tree

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

def dfs_recu(curr: Node[T], goal: Optional[T] = None, visited: Optional[List[Node[T]]] = None) -> List[Node[T]]:
    visited = visited or [curr]
    if goal is not None and curr.val == goal:
        return visited
    if curr.left:
        visited += dfs_recu(curr.left, goal, [curr.left])
    if curr.right:
        visited += dfs_recu(curr.right, goal, [curr.right])
    return visited

arr = [3, 5, 2, 1, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14]
print("Array")
print(arr)
tree = Tree.make(arr)

if tree.root is None:
    raise ValueError("Tree root should not be None.")

print("Tree")
print(tree)

print("Depth-First")
print("Iterative")
result = dfs_iter(tree.root)
print(result)
result = dfs_iter(tree.root, 6)
print(result)

print("Recursive")
result = dfs_recu(tree.root)
print(result)
result = dfs_recu(tree.root, 6)
print(result)

print()
print("Breadth-First")
print("Iterative")
result = bfs_iter(tree.root)
print(result)
result = bfs_iter(tree.root, 6)
print(result)
