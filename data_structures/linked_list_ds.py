# github repository: https://github.com/dev-xero/python-algorithms-practice-sub-1.2

"""linked_list_ds.py
   Linked-List data structure implemented in Python
"""

# ---------------------------------------------------------------------------------------------------------


class Node:
    def __init__(self):
        self.item: str | None = None
        self.next = None


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

    print(first.next.next.item)


# ---------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    main()
