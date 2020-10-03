#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int val;
    struct Node *next;
} Node;

void printList(Node *obj) {
    Node *current = obj;
    while (current) {
        printf("%d ", current->val);
        current = current->next;
    }
    printf("\n");
}

void freeList(Node *obj) {
    Node *current = obj;
    while (current) {
        Node *head = current;
        current = current->next;
        free(head);
    }
}

void testPointer(Node **ptr) {
    *ptr = (Node *)malloc(sizeof(Node));
    (*ptr)->val = 10;
    (*ptr)->next = NULL;
}

int main() {
    Node *null_node = NULL;
    Node *null_node2 = NULL;
    Node *malloc_node = (Node *)malloc(sizeof(Node));
    Node *node = (Node *)malloc(sizeof(Node));
    node->val = 3;
    node->next = NULL;

    char *message = "Illustrate that pointers to `NULL` have different memory addresses"
                    "(and therefore can point to different values later).";
    printf("%s\n", message);
    printf("%p is memory address of `null_node`\n", &null_node);
    printf("%p is memory address of `null_node2`\n", &null_node2);
    printf("%p is memory address of `malloc_node`\n", &malloc_node);
    printf("%p is memory address of `node`\n", &node);
    free(null_node2);
    free(malloc_node);

    printf("Print `null_node`: ");
    printList(null_node);

    message = "Illustrate that pointing a NULL pointer to a new node doesn't change the pointer's memory address.";
    printf("%s\n", message);
    null_node = node;
    printf("%p is memory address of `null_node`\n", &null_node);
    printf("Print `null_node`: ");
    printList(null_node);

    message = "Illustrate that pointer a NULL pointer in a function is valid";
    printf("%s\n", message);
    testPointer(&null_node);
    printf("%p is memory address of `null_node`\n", &null_node);
    printf("Print `null_node`: ");
    printList(null_node);

    free(node);
    freeList(null_node);
}
