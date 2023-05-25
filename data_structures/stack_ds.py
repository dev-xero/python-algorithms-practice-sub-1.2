# code based on java implementation

"""stack_ds.py
   Python implementation of a stack data structure
"""

# ---------------------------------------------------------------------------------------------------------


from data_structures.linked_list_ds import Node


# ---------------------------------------------------------------------------------------------------------


class Stack:
    """Stack Data Structure Implementation Using Linked Lists"""
    _first = Node()
    _size = 0

    def push(self, item: str) -> None:
        old_first = self._first
        first = Node()

        first.item = item
        first.next = old_first

        self._first = first
        self._size += 1

    def pop(self) -> str:
        item = self._first
        self._first = self._first.next
        self._size -= 1

        return item.item

    def is_empty(self) -> bool:
        return self._size == 0

    @property
    def size(self) -> int:
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


# ---------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    main()
