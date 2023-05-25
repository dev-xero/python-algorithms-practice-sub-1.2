# python implementation of a singly linked list

"""linked_list_ds.py
   Linked-List data structure implemented in Python
"""

# ---------------------------------------------------------------------------------------------------------


class Node:
    item: str | None = None
    next = None


# ---------------------------------------------------------------------------------------------------------


def main():
    """Testing"""
    first: Node = Node()
    second: Node = Node()
    third: Node = Node()

    first.item = "first"
    second.item = "second"
    third.item = "third"

    first.next = second
    second.next = third

    print(first.next.next.next)


# ---------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    main()
