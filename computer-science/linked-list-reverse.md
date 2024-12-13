# Linked List Reverse

## Code

``` cpp
struct Node {
    int data;
    Node* next;
    Node(int value) : data(value), next(nullptr) {}
};

Node* reverseLinkedList(Node* head) {
    Node* prev = nullptr;
    Node* current = head;
    Node* next = nullptr;
    while (current != nullptr) {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }
    return prev;
}
```

## Initial Setup

``` mermaid
graph TD
    A[Head: 1] --> B[2]
    B --> C[3]
    C --> D[4]
    D --> NULL
    style A fill:#f96
    style NULL fill:#fff,stroke:#000
```
- `prev`: nullptr (no link yet)
- `current`: Points to Node 1
- `next`: Unset (will store the next node)

## Step 1: Reverse the Link of Node 1

``` mermaid
graph TD
    prev[nullptr]
    A[1] --> prev
    B[2] --> C[3]
    C --> D[4]
    D --> NULL
    style A fill:#f96
    style prev fill:#6f9,stroke:#000
    style NULL fill:#fff,stroke:#000
```
- `next`: Points to Node 2
- Reverse `1->next`: to point to `nullptr`
- `Update `prev` to Node 1, and move current to Node 2

## Step 2: Reverse the Link of Node 2

``` mermaid
graph TD
    A[1] --> prev
    prev --> B[2]
    B --> A
    C[3] --> D[4]
    D --> NULL
    style B fill:#f96
    style prev fill:#6f9,stroke:#000
    style NULL fill:#fff,stroke:#000
````

- `next`: Points to Node 3
- `Reverse `2->next` to point to 1
- Update `prev` to Node 2, and move current to Node 3

## Step 3: Reverse the Link of Node 3

``` mermaid
graph TD
    B[2] --> prev
    A[1] --> B
    prev --> C[3]
    C --> B
    D[4] --> NULL
    style C fill:#f96
    style prev fill:#6f9,stroke:#000
    style NULL fill:#fff,stroke:#000
```

- `next: Points to Node 4
- Reverse `3->next` to point to 2.
- Update `prev` to Node 3, and move current to Node 4.

## Step 4: Reverse the Link of Node 4

``` mermaid
graph TD
    C[3] --> prev
    B[2] --> C
    A[1] --> B
    prev --> D[4]
    D --> C
    style D fill:#f96
    style prev fill:#6f9,stroke:#000
    style NULL fill:#fff,stroke:#000
```

- `next`: Points to `nullptr`
- Reverse `4->next` to point to 3
- Update prev to Node 4, and move current to `nullptr`

## Final State (Reversed Linked List)

``` mermaid
graph TD
    D[Head: 4] --> C[3]
    C --> B[2]
    B --> A[1]
    A --> NULL
    style D fill:#6f9,stroke:#000
    style NULL fill:#fff,stroke:#000
```

- `prev`: Now points to the new head (Node 4).
- The traversal ends because current is `nullptr`.

This visualization explains how the pointers prev, current, and next interact at each step of reversing the linked list. Each step involves breaking the forward link and reconnecting it backward.
