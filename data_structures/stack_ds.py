# github repository: https://github.com/dev-xero/python-algorithms-practice-sub-1.2

"""stack_ds.py
   Python implementation of a stack data structure
"""

# ---------------------------------------------------------------------------------------------------------


from data_structures.linked_list_ds import Node


# ---------------------------------------------------------------------------------------------------------


class Stack:
    """Stack data structure implementation using linked-lists"""
    def __init__(self):
        """Setup"""
        self._first = None
        self._size = 0

    def push(self, item: str) -> None:
        """Push an item on top of the stack"""
        old_first = self._first
        first = Node()

        first.item = item
        first.next = old_first

        self._first = first
        self._size += 1

    def pop(self) -> str:
        """Pop an item on from the stack"""
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack")

        item = self._first
        self._first = self._first.next
        self._size -= 1

        return item.item

    def is_empty(self) -> bool:
        """Returns true if first is None"""
        return self._first is None

    @property
    def size(self) -> int:
        """Returns the size of the stack"""
        return self._size


# ---------------------------------------------------------------------------------------------------------


def main():
    """Testing"""
    test_stack: Stack = Stack()

    test_stack.push("hello")
    test_stack.push("this")
    test_stack.push("is")
    test_stack.push("a")
    test_stack.push("stack")

    print(test_stack.pop())
    print(test_stack.size)
    print(test_stack.pop())
    print(test_stack.pop())
    print(test_stack.size)
    print(test_stack.pop())
    print(test_stack.pop())
    print(test_stack.pop())
    print(test_stack.pop())


# ---------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    main()
