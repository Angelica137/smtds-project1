class Node:
    """
    Represents a node in a linked lists.

    Attributes:
        value (int): The value stored in the node.
        next (optional[Node]): reference to the enxt node
    """

    def __init__(self, value):
        """
        Initialises a new Node object.

        Args:
            value (int): The value to be stored in the Node

        Time complexity O(1)
        """
        self.value = value
        self.next = None

    def __repr__(self) -> str:
        """
        Returns a string representation of the node.

        Time complexity O(1)
        """
        return str(self.value)


class LinkedList:
    """
    Represents a singly linked list.

    Provides methods to create and manage a linked list,
    including adding new nodes and calculating the size of the list.

    Attributes:
        head (Optional[Node]): The first node in the list, or None if the list is empty.
    """

    def __init__(self):
        """
        Initialise a new empty list
        """
        self.head = None

    # string representation of an object
    def __str__(self):
        """
        String representation of the linked list object.

        Returns the complete list as a string.

        Time complexity: O(n) where n is the number of nodes.
        """
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):
        """
        Appends a new node with the given value to the end of the list.

        If the list is empty, the new node becomes the head of the list.
        Otherwise, it iterates to the end of the list and adds the new node there.

        Args:
            value (int): The value to be stored in the new node.

        Time complexity: O(n), where n is the number of nodes in the list.
        """
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        """
        Retutrns the size of the list

        Time compelxity: O(n) where n is the number of nodes.
        """
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1: list, llist_2: list) -> set:
    """
    Finds and return the union set of two linked lists.

    Args:
        llist_1 (LinkedList): The first linked list.
        llist_2 (LinkedList): The second linked list.

    Returns:
        Set[int]: A set containing all unique values from both linked lists.

    Time complexity: O(n + m), where n and m are the lengths of llist_1 and llist_2 respectively.
    """
    result = set()

    # tuple packing
    for llist in (llist_1, llist_2):
        current = llist.head
        while current:
            result.add(current.value)
            current = current.next
    return result


def intersection(llist_1, llist_2):
    """
    Find and return the intersection set of two linked lists.

    Args:
        llist_1 (LinkedList): The first linked list.
        llist_2 (LinkedList): The second linked list.

    Returns:
        Set[int]: A set containing values that exist in both linked lists.

    Time complexity: O(n + m), where n and m are the lengths of llist_1 and llist_2 respectively.
    """
    result = set()
    set_2 = set()

    # add all values from llist_2 to a set
    current_2 = llist_2.head
    while current_2:
        set_2.add(current_2.value)
        current_2 = current_2.next

    # check each value in llist_1 against set_2
    current_1 = llist_1.head
    while current_1:
        if current_1.value in set_2:
            result.add(current_1.value)
        current_1 = current_1.next

    return result


## Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(union(linked_list_1, linked_list_2))
print(intersection(linked_list_1, linked_list_2))

## Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(union(linked_list_3, linked_list_4))
print(intersection(linked_list_3, linked_list_4))


"""
Tests are in test file
"""

## Add your own test cases: include at least three test cases
## and two of them must include edge cases, such as null, empty or very large values

## Test Case 1

## Test Case 2

## Test Case 3
