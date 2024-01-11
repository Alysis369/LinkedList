## Implementation of Linked List in Python
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, head: Node = None, size: int = 0):
        self.__head = Node(0)
        self.size = size
        self.head = head

    @property
    def head(self) -> Node:
        return self.__head.next

    @head.setter
    def head(self, head: Node):
        self.__head.next = head

    def insertAtIndex(self, val, index: int):
        if index > self.size:
            raise IndexError

        cur = self.__head
        for _ in range(index):
            cur = cur.next

        cur.next = Node(val, next=cur.next)

        self.size += 1

    def insertAtBegin(self, val):
        self.insertAtIndex(val, 0)

    def insertAtEnd(self, val):
        self.insertAtIndex(val, self.size)

    def removeAtIndex(self, index: int):
        if index == 0 or index > self.size:
            raise IndexError

        cur = self.__head
        for _ in range(index - 1):
            cur = cur.next

        cur.next = cur.next.next

        self.size -= 1

    def removeAtBegin(self):
        self.removeAtIndex(0)

    def removeAtEnd(self):
        self.removeAtIndex(self.size)

    def updateNode(self, val, index: int):
        if index == 0 or index > self.size:
            raise IndexError

        cur = self.__head
        for _ in range(index):
            cur = cur.next

        cur.val = val

    def removeNode(self, val):
        cur = self.__head
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
                self.size -= 1
                return

            cur = cur.next

        raise Exception("Val not found")

    def reverse(self):
        prev, cur = None, self.head

        while cur:
            cur.next, cur, prev = prev, cur.next, cur

        self.head = prev

    def __len__(self):
        return self.size

    def __iter__(self):
        cur = self.head
        while cur:
            yield self.head
            cur = cur.next

    def __str__(self):
        node_str = ''
        for node in self:
            node_str += f"[{node.val}, next={node.next}],"
        node_str = node_str[0:len(node_str)-1]

        return f"LinkedList({node_str})"


