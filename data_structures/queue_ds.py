# code based on java implementation

"""queue_ds.py
   Python implementation of a queue data structure
"""

# ---------------------------------------------------------------------------------------------------------


from data_structures.linked_list_ds import Node


# ---------------------------------------------------------------------------------------------------------


class Queue:
    _last: Node | None = None
    _first: Node | None = None
    _size: int

    def is_empty(self) -> bool:
        """Returns true if the queue is empty"""
        return self._first is None

    @property
    def size(self) -> int:
        """Returns the size of the queue"""
        return self._size

    def enqueue(self, item: str) -> None:
        """Enqueues an item"""
        old_last = self._last
        last = Node()

        last.item = item
        last.next = None

        if self.is_empty():
            self._first = last

        else:
            old_last.next = last

        self._size += 1

    def dequeue(self) -> str:
        """Dequeues an item"""
        old_first = self._first.item
        self._first = self._first.next

        if self.is_empty():
            self._last = None

        self._size -= 1
        return old_first


# ---------------------------------------------------------------------------------------------------------


def main():
    print()


# ---------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    main()
