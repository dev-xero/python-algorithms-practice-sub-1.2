# code based on java implementation

"""queue_ds.py
   Python implementation of a queue data structure
"""

# ---------------------------------------------------------------------------------------------------------


from data_structures.linked_list_ds import Node


# ---------------------------------------------------------------------------------------------------------


class Queue:
    def __init__(self):
        """Setup"""
        self._last = None
        self._first = None
        self._size = 0

    def is_empty(self) -> bool:
        """Returns true if the queue is empty"""
        return self._first is None

    @property
    def size(self) -> int:
        """Returns the size of the queue"""
        return self._size

    def enqueue(self, item: str) -> None:
        """Enqueues an item"""
        new_last = Node()
        new_last.item = item
        new_last.next = None

        if self.is_empty():
            self._first = new_last

        else:
            self._last.next = new_last

        self._last = new_last
        self._size += 1

    def dequeue(self) -> str:
        """Dequeues an item"""
        if self.is_empty():
            raise IndexError("Cannot dequeue from an empty queue")

        old_first = self._first.item
        self._first = self._first.next

        if self.is_empty():
            self._last = None

        self._size -= 1
        return old_first


# ---------------------------------------------------------------------------------------------------------


def main():
    test_queue: Queue = Queue()

    test_queue.enqueue("This")
    test_queue.enqueue("is")
    test_queue.enqueue("a")
    test_queue.enqueue("queue")

    print(test_queue.dequeue())
    print(test_queue.size)


# ---------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    main()
