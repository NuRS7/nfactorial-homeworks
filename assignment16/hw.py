from typing import List, Any, Dict, Set, Generator


class StaticArray:
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("Capacity must be greater than zero.")
        self.capacity=capacity
        self.data=[None] * capacity

    def set(self, index: int, value: int) -> None:

        if index < 0 or index >= self.capacity:
            raise IndexError("Index out of bounds.")
        self.data[index]=value

    def get(self, index: int) -> int:

        if index < 0 or index >= self.capacity:
            raise IndexError("Index out of bounds.")
        return self.data[index]


class DynamicArray:
    def __init__(self):
        self.data = []
        self.size = 0
        self.capacity = 1
        self.internal_array = [None] * self.capacity

    def resize(self, new_capacity: int) -> None:
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.internal_array[i]
        self.internal_array = new_array
        self.capacity = new_capacity

    def append(self, value: int) -> None:
        if self.size == self.capacity:
            self.resize(self.capacity * 2)
        self.internal_array[self.size] = value
        self.size += 1

    def insert(self, index: int, value: int) -> None:
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds.")
        if self.size == self.capacity:
            self.resize(self.capacity * 2)
        for i in range(self.size, index, -1):
            self.internal_array[i] = self.internal_array[i - 1]
        self.internal_array[index] = value
        self.size += 1

    def delete(self, index: int) -> None:
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds.")
        for i in range(index, self.size - 1):
            self.internal_array[i] = self.internal_array[i + 1]
        self.internal_array[self.size - 1] = None
        self.size -= 1
        if self.size <= self.capacity // 4 and self.capacity > 1:
            self.resize(self.capacity // 2)

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds.")
        return self.internal_array[index]
class Node:
    def __init__(self, value: int):
        """
        Initialize a node with a value.
        """
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        """
        Initialize an empty singly linked list.
        """
        self.head = None
        self.size_count = 0

    def append(self, value: int) -> None:
        """
        Add a node with a value to the end of the linked list.
        """
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size_count += 1

    def insert(self, position: int, value: int) -> None:
        """
        Insert a node with a value at a particular position.
        """
        if position < 0 or position > self.size_count:
            raise IndexError("Position out of bounds.")
        new_node = Node(value)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(position - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
        self.size_count += 1

    def delete(self, value: int) -> None:
        """
        Delete the first node with a specific value.
        """
        current = self.head
        previous = None
        while current:
            if current.value == value:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                self.size_count -= 1
                return
            previous = current
            current = current.next
        raise ValueError("Value not found in the list.")

    def find(self, value: int) -> Node:
        """
        Find a node with a specific value.
        """
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next
        raise ValueError("Value not found in the list.")

    def size(self) -> int:
        """
        Returns the number of elements in the linked list.
        """
        return self.size_count

    def is_empty(self) -> bool:
        """
        Checks if the linked list is empty.
        """
        return self.head is None

    def print_list(self) -> None:
        """
        Prints all elements in the linked list.
        """
        current = self.head
        values = []
        while current:
            values.append(current.value)
            current = current.next
        print(" -> ".join(map(str, values)))

    def reverse(self) -> None:
        """
        Reverse the linked list in-place.
        """
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def get_head(self) -> Node:
        """
        Returns the head node of the linked list.
        """
        return self.head

    def get_tail(self) -> Node:
        """
        Returns the tail node of the linked list.
        """
        current = self.head
        if not current:
            return None
        while current.next:
            current = current.next
        return current


class DoubleNode:
    def __init__(self, value: int, next_node=None, prev_node=None):
        """
        Initialize a double node with value, next, and previous.
        """
        self.value = value
        self.next = next_node
        self.prev = prev_node


class DoublyLinkedList:
    def __init__(self):
        """
        Initialize an empty doubly linked list.
        """
        self.head = None
        self.tail = None
        self.size_count = 0

    def append(self, value: int) -> None:
        """
        Add a node with a value to the end of the linked list.
        """
        new_node = DoubleNode(value)
        if not self.head:  # List is empty
            self.head = new_node
            self.tail = new_node
        else:  # List is not empty
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size_count += 1

    def insert(self, position: int, value: int) -> None:
        """
        Insert a node with a value at a particular position.
        """
        if position < 0 or position > self.size_count:
            raise IndexError("Position out of bounds.")
        new_node = DoubleNode(value)
        if position == 0:  # Insert at head
            if self.head:
                new_node.next = self.head
                self.head.prev = new_node
            self.head = new_node
            if self.size_count == 0:  # List was empty
                self.tail = new_node
        elif position == self.size_count:  # Insert at tail
            self.append(value)
            return
        else:  # Insert in the middle
            current = self.head
            for _ in range(position):
                current = current.next
            new_node.next = current
            new_node.prev = current.prev
            if current.prev:
                current.prev.next = new_node
            current.prev = new_node
        self.size_count += 1

    def delete(self, value: int) -> None:
        """
        Delete the first node with a specific value.
        """
        current = self.head
        while current:
            if current.value == value:
                if current.prev:
                    current.prev.next = current.next
                else:  # Deleting head
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:  # Deleting tail
                    self.tail = current.prev
                self.size_count -= 1
                return
            current = current.next
        raise ValueError("Value not found in the list.")

    def find(self, value: int) -> DoubleNode:
        """
        Find a node with a specific value.
        """
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next
        raise ValueError("Value not found in the list.")

    def size(self) -> int:
        """
        Returns the number of elements in the linked list.
        """
        return self.size_count

    def is_empty(self) -> bool:
        """
        Checks if the linked list is empty.
        """
        return self.size_count == 0

    def print_list(self) -> None:
        """
        Prints all elements in the linked list.
        """
        current = self.head
        values = []
        while current:
            values.append(current.value)
            current = current.next
        print(" <-> ".join(map(str, values)))

    def reverse(self) -> None:
        """
        Reverse the linked list in-place.
        """
        current = self.head
        self.tail = self.head
        prev = None
        while current:
            next_node = current.next
            current.next = prev
            current.prev = next_node
            prev = current
            current = next_node
        self.head = prev

    def get_head(self) -> DoubleNode:

        return self.head

    def get_tail(self) -> DoubleNode:

        return self.tail
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        raise IndexError("dequeue from an empty queue")

    def is_empty(self):
        return len(self.queue) == 0

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        raise IndexError("peek from an empty queue")

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.node_count = 0

    class TreeNode:
        def __init__(self, value: int):
            self.value = value
            self.left = None
            self.right = None

    def insert(self, value: int) -> None:
        def _insert(node, value):
            if node is None:
                return self.TreeNode(value)
            if value < node.value:
                node.left = _insert(node.left, value)
            elif value > node.value:
                node.right = _insert(node.right, value)
            return node

        self.root = _insert(self.root, value)
        self.node_count += 1

    def delete(self, value: int) -> None:
        def _delete(node, value):
            if node is None:
                return None
            if value < node.value:
                node.left = _delete(node.left, value)
            elif value > node.value:
                node.right = _delete(node.right, value)
            else:
                if node.left is None:
                    return node.right
                if node.right is None:
                    return node.left
                min_larger_node = self._find_min(node.right)
                node.value = min_larger_node
                node.right = _delete(node.right, min_larger_node)
            return node

        self.root = _delete(self.root, value)
        self.node_count -= 1

    def search(self, value: int) -> TreeNode:
        def _search(node, value):
            if node is None or node.value == value:
                return node
            if value < node.value:
                return _search(node.left, value)
            return _search(node.right, value)

        return _search(self.root, value)

    def inorder_traversal(self) -> List[int]:
        def _inorder(node):
            return _inorder(node.left) + [node.value] + _inorder(node.right) if node else []

        return _inorder(self.root)

    def preorder_traversal(self) -> List[int]:
        def _preorder(node):
            return [node.value] + _preorder(node.left) + _preorder(node.right) if node else []

        return _preorder(self.root)

    def postorder_traversal(self) -> List[int]:
        def _postorder(node):
            return _postorder(node.left) + _postorder(node.right) + [node.value] if node else []

        return _postorder(self.root)

    def level_order_traversal(self) -> List[int]:
        result = []
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            if current:
                result.append(current.value)
                queue.append(current.left)
                queue.append(current.right)
        return result

    def minimum(self) -> int:
        def _find_min(node):
            while node.left:
                node=node.left
            return node.value

        if self.root is None:
            raise ValueError("The tree is empty")
        return _find_min(self.root)

    def maximum(self) -> int:
        def _find_max(node):
            while node.right:
                node=node.right
            return node.value

        if self.root is None:
            raise ValueError("The tree is empty")
        return _find_max(self.root)

    def size(self) -> int:
        return self.node_count

    def is_empty(self) -> bool:
        return self.node_count == 0

    def height(self) -> int:
        def _height(node):
            if node is None:
                return -1
            return 1 + max(_height(node.left), _height(node.right))
        return _height(self.root)

    def is_valid_bst(self) -> bool:
        def _is_valid(node, min_val, max_val):
            if not node:
                return True
            if not (min_val < node.value < max_val):
                return False
            return _is_valid(node.left, min_val, node.value) and _is_valid(node.right, node.value, max_val)

        return _is_valid(self.root, float('-inf'), float('inf'))


def insertion_sort(lst: List[int]) -> List[int]:
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst


def selection_sort(lst: List[int]) -> List[int]:
    for i in range(len(lst)):
        min_idx = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst


def bubble_sort(lst: List[int]) -> List[int]:
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


def shell_sort(lst: List[int]) -> List[int]:
    gap = len(lst) // 2
    while gap > 0:
        for i in range(gap, len(lst)):
            temp = lst[i]
            j = i
            while j >= gap and lst[j - gap] > temp:
                lst[j] = lst[j - gap]
                j -= gap
            lst[j] = temp
        gap //= 2
    return lst


def merge_sort(lst: List[int]) -> List[int]:
    if len(lst) > 1:
        mid = len(lst) // 2
        left = merge_sort(lst[:mid])
        right = merge_sort(lst[mid:])
        lst = []
        while left and right:
            if left[0] < right[0]:
                lst.append(left.pop(0))
            else:
                lst.append(right.pop(0))
        lst.extend(left or right)
    return lst


def quick_sort(lst: List[int]) -> List[int]:
    if len(lst) <= 1:
        return lst
    pivot = lst[len(lst) // 2]
    left = [x for x in lst if x < pivot]
    middle = [x for x in lst if x == pivot]
    right = [x for x in lst if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
