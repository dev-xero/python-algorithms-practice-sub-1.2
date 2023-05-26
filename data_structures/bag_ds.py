# github repository: https://github.com/dev-xero/python-algorithms-practice-sub-1.2

"""bag_ds.py
   Python implementation of a bag data structure
"""

# ---------------------------------------------------------------------------------------------------------


from data_structures.linked_list_ds import Node


# ---------------------------------------------------------------------------------------------------------


class Bag:
    """Implementation of a bag data structure using linked-lists"""
    def __init__(self):
        """Setup"""
        self._first: Node | None = None
        self._size: int = 0

    def add(self, item: str) -> None:
        old_first = self._first
        first = Node()

        first.item = item
        first.next = old_first

        self._first = first

    def is_empty(self) -> bool:
        """Returns true if the first node is None"""
        return self._first is None

    @property
    def size(self) -> int:
        """Returns the size of the bag"""
        return self._size


# ---------------------------------------------------------------------------------------------------------


def main():
    """Testing"""
    test_bag = Bag()

    print(test_bag.is_empty())

    test_bag.add("this")
    test_bag.add("is")
    test_bag.add("a")
    test_bag.add("bag")

    print(test_bag.size)


# ---------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    main()
